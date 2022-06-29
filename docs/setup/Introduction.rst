==============================
Introduction
==============================

These docs provide a simple instruction list for setting up automatic updating of your project documentation hosted at ReadTheDocs.

**Overall Process**

VSCode -> reStructuredText -> Sphinx -> GitHub -> ReadTheDocs

#. In VSCode, create plain text source files in reStructuredText (.rst) format.
#. Set up Sphinx to translate the .rst files into HTML (and PDF) file formats. 
#. In VSCode, push the documentation changes to a GitHub repository. 
#. Then the docs hosted at ReadTheDocs will update automatically thanks to a webhook to GitHub.

----

Required software
------------------------------

.. rst-class:: bignums

#. Python
#. Sphinx
#. Sphinx theme for read the docs
#. Sphinx extensions
#. Visual Studio code (VSCode)
#. Visual Studio code reStructuredText (reST) extension
#. Git command line tool
#. Github (free account)
#. ReadTheDocs (RTD) (free account)
