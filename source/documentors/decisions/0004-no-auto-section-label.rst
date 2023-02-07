Don't Use Auto Section Label
############################

Status
******

**Accepted**

Context
*******

``sphinx.ext.autosectionlabel`` automatically creates labels for every section
of every page in the project.  This can reduce manual work and can increase
consistency.  However, with this feature enabled, there are a couple of
downsides.

* We must enable ``autosectionlabel_prefix_document`` or we would not be allowed
  to have any two sections that share the same name.  Eg.  There couldn't be two
  decision docs with a ``Context`` section.  This would result in an error
  (technically a warning but we treat all warnings as errors to miss some very
  important warnings.)
* Even with document prefixing, you can't have the same section name between two
  different sections in the same document.  We run into this with our release
  notes where both the ``Author Experience`` and ``Learner Experience`` sections
  might talk about the same feature (``Open Response Assessments`` for example).
* The errors that occur from the automatic labels are confusing and hard to
  debug if you aren't already familiar with auto labeling.

Decision
********

* We will not use the `autosectionlabel` extension to create labels.  Instead
  we'll expect writers to manually create labels for any topics they wish to
  cross link to.
