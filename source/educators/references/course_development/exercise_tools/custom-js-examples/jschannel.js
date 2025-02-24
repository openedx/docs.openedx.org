var Channel = (function() {
    'use strict';
    // current transaction id, start out at a random *odd* number between 1 and a million
    // There is one current transaction counter id per page, and it's shared between
    // channel instances.  That means of all messages posted from a single javascript
    // evaluation context, we'll never have two with the same id.
    var sCurTranId = Math.floor(Math.random() * 1000001);

    // no two bound channels in the same javascript evaluation context may have the same origin, scope, and window.
    // futher if two bound channels have the same window and scope, they may not have *overlapping* origins
    // (either one or both support '*').  This restriction allows a single onMessage handler to efficiently
    // route messages based on origin and scope.  The sBoundChans maps origins to scopes, to message
    // handlers.  Request and Notification messages are routed using this table.
    // Finally, channels are inserted into this table when built, and removed when destroyed.
    var sBoundChans = { };
    var sTransIds = { };
    var sOnMessage = function(e) {
        var m,
            w = e.source,
            o = e.origin,
            s, i, j, ar,
            meth,
            delivered;

        try {
            m = JSON.parse(e.data);
            if (typeof m !== 'object' || m === null) throw new Error('malformed');
        } catch (err) {
          // just ignore any posted messages that do not consist of valid JSON
        }

        if (typeof m.method === 'string') {
            ar = m.method.split('::');
            if (ar.length === 2) {
                s = ar[0];
                meth = ar[1];
            } else {
                meth = m.method;
            }
        }

        if (typeof m.id !== 'undefined') i = m.id;

        // if it has a method it's either a notification or a request,
        // route using sBoundChans
        if (typeof meth === 'string') {
            delivered = false;
            if (sBoundChans[o] && sBoundChans[o][s]) {
                for (j = 0; j < sBoundChans[o][s].length; j++) {
                    if (sBoundChans[o][s][j].win === w) {
                        sBoundChans[o][s][j].handler(o, meth, m);
                        delivered = true;
                        break;
                    }
                }
            }

            if (!delivered && sBoundChans['*'] && sBoundChans['*'][s]) {
                for (j = 0; j < sBoundChans['*'][s].length; j++) {
                    if (sBoundChans['*'][s][j].win === w) {
                        sBoundChans['*'][s][j].handler(o, meth, m);
                        break;
                    }
                }
            }
        } else if (typeof i !== 'undefined') {
            if (sTransIds[i]) sTransIds[i](o, meth, m);
        }
    };

    // add a channel to sBoundChans, throwing if a dup exists
    function sAddBoundChan(win, origin, scope, handler) {
        var exists = false,
            k;

        function hasWin(arr) {
            var i;
            for (i = 0; i < arr.length; i++) if (arr[i].win === win) return true;
            return false;
        }

        if (origin === '*') {
            // we must check all other origins, sadly.
            for (k in sBoundChans) {
                if (!sBoundChans.hasOwnProperty(k)) continue;
                if (k === '*') continue;
                if (typeof sBoundChans[k][scope] === 'object') {
                    exists = hasWin(sBoundChans[k][scope]);
                    if (exists) break;
                }
            }
        } else {
            // we must check only '*'
            if ((sBoundChans['*'] && sBoundChans['*'][scope])) {
                exists = hasWin(sBoundChans['*'][scope]);
            }
            if (!exists && sBoundChans[origin] && sBoundChans[origin][scope]) {
                exists = hasWin(sBoundChans[origin][scope]);
            }
        }
        if (exists) {
            throw new Error("A channel is already bound to origin '" + origin + "' and has scope '" + scope + "'");
        }

        if (typeof sBoundChans[origin] !== 'object') sBoundChans[origin] = { };
        if (typeof sBoundChans[origin][scope] !== 'object') sBoundChans[origin][scope] = [];
        sBoundChans[origin][scope].push({win: win, handler: handler});
    }

    function sRemoveBoundChan(win, origin, scope) {
        var arr = sBoundChans[origin][scope],
            i;

        for (i = 0; i < arr.length; i++) {
            if (arr[i].win === win) {
                arr.splice(i, 1);
            }
        }
        if (sBoundChans[origin][scope].length === 0) {
            delete sBoundChans[origin][scope];
        }
    }

    function sIsArray(obj) {
        if (Array.isArray) return Array.isArray(obj);
        else {
            return (obj.constructor.toString().indexOf('Array') !== -1);
        }
    }

    // Setup postMessage event listeners
    if (window.addEventListener) window.addEventListener('message', sOnMessage, false);
    else if (window.attachEvent) window.attachEvent('onmessage', sOnMessage);

    return {
        build: function(cfg) {
            var validOrigin = false,
                oMatch;
            var chanId = (function() {
                var text = '';
                var i;
                var alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';
                for (i = 0; i < 5; i++) text += alpha.charAt(Math.floor(Math.random() * alpha.length));
                return text;
            }());
            var regTbl = {};
            var outTbl = {};
            var inTbl = {};
            var ready = false;
            var pendingQueue = [];
            var debug = function(m) {
                if (cfg.debugOutput && window.console && window.console.log) {
                    try {
                        if (typeof m !== 'string') {
                            ms = JSON.stringify(m);
                        }
                    } catch (e) {
                        // comment
                    }
                }
            };
            var createTransaction = function(id, origin, callbacks) {
                var shouldDelayReturn = false;
                var completed = false;
                var valid = false;
                var i;

                return {
                    origin: origin,
                    invoke: function(cbName, v) {
                        // verify in table
                        if (!inTbl[id]) {
                            throw Error('attempting to invoke a callback of a nonexistent transaction: ' + id);
                        }
                        // verify that the callback name is valid
                        for (i = 0; i < callbacks.length; i++) if (cbName === callbacks[i]) { valid = true; break; }
                        if (!valid) throw Error('request supports no such callback ' + cbName);

                        postMessage({id: id, callback: cbName, params: v});
                    },
                    error: function(error, message) {
                        completed = true;
                        // verify in table
                        if (!inTbl[id]) throw "error called for nonexistent message: " + id;

                        // remove transaction from table
                        delete inTbl[id];

                        // send error
                        postMessage({ id: id, error: error, message: message });
                    },
                    complete: function(v) {
                        completed = true;
                        // verify in table
                        if (!inTbl[id]) throw "complete called for nonexistent message: " + id;
                        // remove transaction from table
                        delete inTbl[id];
                        // send complete
                        postMessage({ id: id, result: v });
                    },
                    delayReturn: function(delay) {
                        if (typeof delay === 'boolean') {
                            shouldDelayReturn = (delay === true);
                        }
                        return shouldDelayReturn;
                    },
                    completed: function() {
                        return completed;
                    }
                };
            };

            /* browser capabilities check */
            if (!window.postMessage) throw new Error('jschannel cannot run this browser, no postMessage');
            if (!window.JSON || !window.JSON.stringify || ! window.JSON.parse) {
                throw Error('jschannel cannot run this browser, no JSON parsing/serialization');
            }

            /* basic argument validation */
            if (typeof cfg !== 'object') throw Error('Channel build invoked without a proper object argument');

            if (!cfg.window || !cfg.window.postMessage) {
                throw Error('Channel.build() called without a valid window argument');
            }

            /* we'd have to do a little more work to be able to run multiple channels that intercommunicate the same
             * window...  Not sure if we care to support that */
            if (window === cfg.window) {
                throw Error('target window is same as present window -- not allowed');
            }

            if (typeof cfg.origin === 'string') {
                if (cfg.origin === '*') {
                    validOrigin = true;
                } else {
                    cfg.origin = oMatch[0].toLowerCase();
                    validOrigin = true;
                }
            }
            if (!validOrigin) throw Error('Channel.build() called with an invalid origin');

            if (typeof cfg.scope !== 'undefined') {
                if (typeof cfg.scope !== 'string') throw Error('scope, when specified, must be a string');
                if (cfg.scope.split('::').length > 1) throw Error('scope may not contain double colons: "::"');
            }

            

            var setTransactionTimeout = function(transId, timeout, method) {
              return window.setTimeout(function() {
                if (outTbl[transId]) {
                  // XXX: what if client code raises an exception here?
                  var msg = "timeout (" + timeout + "ms) exceeded on method '" + method + "'";
                  (1,outTbl[transId].error)("timeout_error", msg);
                  delete outTbl[transId];
                  delete sTransIds[transId];
                }
              }, timeout);
            };

            var onMessage = function(origin, method, m) {
                // if an observer was specified at allocation time, invoke it
                if (typeof cfg.gotMessageObserver === 'function') {
                    // pass observer a clone of the object so that our
                    // manipulations are not visible (i.e. method unscoping).
                    // This is not particularly efficient, but then we expect
                    // that message observers are primarily for debugging anyway.
                    try {
                        cfg.gotMessageObserver(origin, m);
                    } catch (e) {
                        debug("gotMessageObserver() raised an exception: " + e.toString());
                    }
                }

                // now, what type of message is this?
                if (m.id && method) {
                    // a request!  do we have a registered handler for this request?
                    if (regTbl[method]) {
                        var trans = createTransaction(m.id, origin, m.callbacks ? m.callbacks : [ ]);
                        inTbl[m.id] = { };
                        try {
                            // callback handling.  we'll magically create functions inside the parameter list for each
                            // callback
                            if (m.callbacks && sIsArray(m.callbacks) && m.callbacks.length > 0) {
                                for (var i = 0; i < m.callbacks.length; i++) {
                                    var path = m.callbacks[i];
                                    var obj = m.params;
                                    var pathItems = path.split('/');
                                    for (var j = 0; j < pathItems.length - 1; j++) {
                                        var cp = pathItems[j];
                                        if (typeof obj[cp] !== 'object') obj[cp] = { };
                                        obj = obj[cp];
                                    }
                                    obj[pathItems[pathItems.length - 1]] = (function() {
                                        var cbName = path;
                                        return function(params) {
                                            return trans.invoke(cbName, params);
                                        };
                                    })();
                                }
                            }
                            var resp = regTbl[method](trans, m.params);
                            if (!trans.delayReturn() && !trans.completed()) trans.complete(resp);
                        } catch(e) {
                            // automagic handling of exceptions:
                            var error = "runtime_error";
                            var message = null;
                            // * if it's a string then it gets an error code of 'runtime_error' and string is the message
                            if (typeof e === 'string') {
                                message = e;
                            } else if (typeof e === 'object') {
                                // either an array or an object
                                // * if it's an array of length two, then  array[0] is the code, array[1] is the error message
                                if (e && sIsArray(e) && e.length == 2) {
                                    error = e[0];
                                    message = e[1];
                                }
                                // * if it's an object then we'll look form error and message parameters
                                else if (typeof e.error === 'string') {
                                    error = e.error;
                                    if (!e.message) message = "";
                                    else if (typeof e.message === 'string') message = e.message;
                                    else e = e.message; // let the stringify/toString message give us a reasonable verbose error string
                                }
                            }

                            // message is *still* null, let's try harder
                            if (message === null) {
                                try {
                                    message = JSON.stringify(e);
                                    /* On MSIE8, this can result in 'out of memory', which
                                     * leaves message undefined. */
                                    if (typeof(message) == 'undefined')
                                      message = e.toString();
                                } catch (e2) {
                                    message = e.toString();
                                }
                            }

                            trans.error(error,message);
                        }
                    }
                } else if (m.id && m.callback) {
                    if (!outTbl[m.id] ||!outTbl[m.id].callbacks || !outTbl[m.id].callbacks[m.callback])
                    {
                        debug("ignoring invalid callback, id:"+m.id+ " (" + m.callback +")");
                    } else {
                        // XXX: what if client code raises an exception here?
                        outTbl[m.id].callbacks[m.callback](m.params);
                    }
                } else if (m.id) {
                    if (!outTbl[m.id]) {
                        debug("ignoring invalid response: " + m.id);
                    } else {
                        // XXX: what if client code raises an exception here?
                        if (m.error) {
                            (1,outTbl[m.id].error)(m.error, m.message);
                        } else {
                            if (m.result !== undefined) (1,outTbl[m.id].success)(m.result);
                            else (1,outTbl[m.id].success)();
                        }
                        delete outTbl[m.id];
                        delete sTransIds[m.id];
                    }
                } else if (method) {
                    // tis a notification.
                    if (regTbl[method]) {
                        // yep, there's a handler for that.
                        // transaction has only origin for notifications.
                        regTbl[method]({ origin: origin }, m.params);
                        // if the client throws, we'll just let it bubble out
                        // what can we do?  Also, here we'll ignore return values
                    }
                }
            };

            // now register our bound channel for msg routing
            sAddBoundChan(cfg.window, cfg.origin, ((typeof cfg.scope === 'string') ? cfg.scope : ''), onMessage);

            // scope method names based on cfg.scope specified when the Channel was instantiated
            var scopeMethod = function(m) {
                if (typeof cfg.scope === 'string' && cfg.scope.length) m = [cfg.scope, m].join("::");
                return m;
            };

            // a small wrapper around postmessage whose primary function is to handle the
            // case that clients start sending messages before the other end is "ready"
            var postMessage = function(msg, force) {
                if (!msg) throw "postMessage called with null message";

                // delay posting if we're not ready yet.
                var verb = (ready ? "post  " : "queue ");
                debug(verb + " message: " + JSON.stringify(msg));
                if (!force && !ready) {
                    pendingQueue.push(msg);
                } else {
                    if (typeof cfg.postMessageObserver === 'function') {
                        try {
                            cfg.postMessageObserver(cfg.origin, msg);
                        } catch (e) {
                            debug("postMessageObserver() raised an exception: " + e.toString());
                        }
                    }

                    cfg.window.postMessage(JSON.stringify(msg), cfg.origin);
                }
            };

            var onReady = function(trans, type) {
                debug('ready msg received');
                if (ready) throw "received ready message while in ready state.  help!";

                if (type === 'ping') {
                    chanId += '-R';
                } else {
                    chanId += '-L';
                }

                obj.unbind('__ready'); // now this handler isn't needed any more.
                ready = true;
                debug('ready msg accepted.');

                if (type === 'ping') {
                    obj.notify({ method: '__ready', params: 'pong' });
                }

                // flush queue
                while (pendingQueue.length) {
                    postMessage(pendingQueue.pop());
                }

                // invoke onReady observer if provided
                if (typeof cfg.onReady === 'function') cfg.onReady(obj);
            };

            var obj = {
                // tries to unbind a bound message handler.  returns false if not possible
                unbind: function (method) {
                    if (regTbl[method]) {
                        if (!(delete regTbl[method])) throw ("can't delete method: " + method);
                        return true;
                    }
                    return false;
                },
                bind: function (method, cb) {
                    if (!method || typeof method !== 'string') throw "'method' argument to bind must be string";
                    if (!cb || typeof cb !== 'function') throw "callback missing from bind params";

                    if (regTbl[method]) throw "method '"+method+"' is already bound!";
                    regTbl[method] = cb;
                    return this;
                },
                call: function(m) {
                    if (!m) throw 'missing arguments to call function';
                    if (!m.method || typeof m.method !== 'string') throw "'method' argument to call must be string";
                    if (!m.success || typeof m.success !== 'function') throw "'success' callback missing from call";

                    // now it's time to support the 'callback' feature of jschannel.  We'll traverse the argument
                    // object and pick out all of the functions that were passed as arguments.
                    var callbacks = { };
                    var callbackNames = [ ];
                    var seen = [ ];

                    var pruneFunctions = function (path, obj) {
                        if (seen.indexOf(obj) >= 0) {
                            throw "params cannot be a recursive data structure"
                        }
                        seen.push(obj);
                       
                        if (typeof obj === 'object') {
                            for (var k in obj) {
                                if (!obj.hasOwnProperty(k)) continue;
                                var np = path + (path.length ? '/' : '') + k;
                                if (typeof obj[k] === 'function') {
                                    callbacks[np] = obj[k];
                                    callbackNames.push(np);
                                    delete obj[k];
                                } else if (typeof obj[k] === 'object') {
                                    pruneFunctions(np, obj[k]);
                                }
                            }
                        }
                    };
                    pruneFunctions("", m.params);

                    // build a 'request' message and send it
                    var msg = { id: sCurTranId, method: scopeMethod(m.method), params: m.params };
                    if (callbackNames.length) msg.callbacks = callbackNames;

                    if (m.timeout)
                      // XXX: This function returns a timeout ID, but we don't do anything with it.
                      // We might want to keep track of it so we can cancel it using clearTimeout()
                      // when the transaction completes.
                      setTransactionTimeout(sCurTranId, m.timeout, scopeMethod(m.method));

                    // insert into the transaction table
                    outTbl[sCurTranId] = { callbacks: callbacks, error: m.error, success: m.success };
                    sTransIds[sCurTranId] = onMessage;

                    // increment current id
                    sCurTranId++;

                    postMessage(msg);
                },
                notify: function(m) {
                    if (!m) throw 'missing arguments to notify function';
                    if (!m.method || typeof m.method !== 'string') throw "'method' argument to notify must be string";

                    // no need to go into any transaction table
                    postMessage({ method: scopeMethod(m.method), params: m.params });
                },
                destroy: function () {
                    sRemoveBoundChan(cfg.window, cfg.origin, ((typeof cfg.scope === 'string') ? cfg.scope : ''));
                    if (window.removeEventListener) window.removeEventListener('message', onMessage, false);
                    else if(window.detachEvent) window.detachEvent('onmessage', onMessage);
                    ready = false;
                    regTbl = { };
                    inTbl = { };
                    outTbl = { };
                    cfg.origin = null;
                    pendingQueue = [];
                    debug('channel destroyed');
                    chanId = '';
                }
            };

            obj.bind('__ready', onReady);
            setTimeout(function() {
                postMessage({method: scopeMethod('__ready'), params: 'ping'}, true);
            }, 0);

            return obj;
        }
    };
}());
