.. _Work with the targz File:

Working with the ``.tar.gz`` File
###################################

.. tags:: educator, reference

Courses are exported and imported in ``.tar.gz`` files containing OLX (Open
Learning XML), the Open edX markup format for open course exchange. For more
information about OLX, see the `EdX Open Learning XML Guide`_.

To extract and compress ``.tar.gz`` files, if you're using Linux or macOS ::

  # extract
  tar -zxvf example.tar.gz

  # compress
  tar -czvf example.tar.gz /path/to/directory-or-file

If you're using Windows, you'll probably need a 3rd-party tool like `7-zip`_ or
`TarTool`_.

For more, see the following resources:

* `How to Unpack a tar file in Windows
  <http://www.haskell.org/haskellwiki/How_to_unpack_a_tar_file_in_Windows>`_

* `How to extract a gz file <http://www.wikihow.com/Extract-a-Gz-File>`_

* `The gzip Home Page <http://www.gzip.org/>`_

.. _7-zip: http://www.7-zip.org
.. _TarTool: https://github.com/senthilrajasek/tartool

.. seealso::
 

 :ref:`Export a Course` (how-to)

 :ref:`Import a Course` (how-to)

 :ref:`Course Export File Terminology` (reference)

**Maintenance chart**

+--------------+-------------------------------+----------------+--------------------------------+
| Review Date  | Working Group Reviewer        |   Release      |Test situation                  |
+--------------+-------------------------------+----------------+--------------------------------+
|              |                               |                |                                |
+--------------+-------------------------------+----------------+--------------------------------+
