.. PC-Using-RTD documentation master file, created by sphinx-quickstart, 2020, updated 2022.
    It should at least contain the root `toctree` directive.

==============================
PC-Using-RTD 
==============================

These docs provide a simple instruction list for setting up automatic updating of your project documentation hosted at ReadTheDocs.

**Overall Process**

Python -> Sphinx -> VSCode -> reStructuredText -> GitHub -> ReadTheDocs

#. Using Python, set up Sphinx to translate the .rst files into HTML (and PDF) file formats. 
#. In VSCode, create plain text source files in reStructuredText (.rst) format.
#. In VSCode, push the documentation changes to a GitHub repository. 
#. Set up ReadTheDocs to automatically update via a webhook to GitHub.


.. toctree::
    :maxdepth: 3
    :caption: 📚 Table of Contents:
    :numbered:

    setup/Introduction.rst
    setup/Python.rst
    setup/Sphinx.rst
    setup/Jupyter.rst
    setup/VSCode.rst 
    setup/VSCode Project Folder and Sphinx.rst
    setup/VSCode reStructuredText.rst
    setup/VSCode make html and pdf.rst
    setup/VSCode special files.rst
    setup/VSCode conf.py.rst
    setup/Git.rst
    setup/GitHub and VSCode.rst
    setup/Read the docs (RTD).rst
    setup/VSCode to GitHub to RTDs.rst

----

An alternate approach can be followed in the techwritingmatters tutorial which has 4 youtube videos.
https://techwritingmatters.com/documenting-with-sphinx-tutorial-intro-overview#Structure_of_the_Tutorial
It starts by cloning a new GitHub repository to the computer. It is Mac based. It uses a text editor instead of VSCode.

The above steps are suitable for one author using the master branch only. 
For collaboration and the use of feature branches for development see the command line interface (CLI) commands details below:

.. toctree::
    :maxdepth: 3
    :caption: More on Git:
    :numbered:

    setup/Git CLI.rst

