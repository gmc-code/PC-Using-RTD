==============================
Introduction
==============================

These docs provide a simple instruction list for setting up automatic updating of your project documentation hosted at ReadTheDocs.

**Overall Process**

Python -> Sphinx -> VSCode -> reStructuredText -> GitHub -> ReadTheDocs

#. Using Python, set up Sphinx to translate the .rst files into HTML (and PDF) file formats. 
#. In VSCode, create plain text source files in reStructuredText (.rst) format.
#. In VSCode, push the documentation changes to a GitHub repository. 
#. Set up ReadTheDocs to automatically update via a webhook to GitHub.

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
