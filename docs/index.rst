.. PC-Using-RTD documentation master file, created by sphinx-quickstart, 2020.
   It should at least contain the root `toctree` directive.

PC-Using-RTD 
=================

These docs provide a simple instruction list for setting up automatic updating of your project documentation hosted at ReadTheDocs.

Overall Process
=================
VSCode -> reStructuredText -> Sphinx -> GitHub -> ReadTheDocs

#. In VSCode, create plain text source files in reStructuredText (.rst) format.
#. Set up Sphinx to translate the .rst files into HTML (and PDF) file formats. 
#. In VSCode, push the documentation changes to a GitHub repository. 
#. Then the docs hosted at ReadTheDocs will have a webhook to GitHub so it updates automatically.


.. toctree::
   :maxdepth: 3
   :caption: Steps:
   :numbered:

   setup/Requirements.rst
   setup/Python.rst
   setup/Sphinx.rst
   setup/VSCode.rst 
   setup/VSCode Project Folder and Sphinx.rst
   setup/VSCode reStructuredText.rst
   setup/VSCode special files.rst
   setup/VSCode conf.py.rst
   setup/Git.rst
   setup/GitHub new repo.rst
   setup/Read the docs (RTD).rst
   setup/Push VSCode changes to GitHub.rst

An alternate approach can be followed in the techwritingmatters tutorial which has 4 youtube videos.
https://techwritingmatters.com/documenting-with-sphinx-tutorial-intro-overview#Structure_of_the_Tutorial
It starts by cloning a new GitHub repository to the computer. It is Mac based. It uses a text editor instead of VSCode.

The above steps are suitable for one author using the master branch only. 
For collaboration and the use of feature branches for development see the command line interface (CLI) commands details below:

.. toctree::
   :maxdepth: 3
   :caption: More on Git:
   :numbered:

   setup/Git commands.rst

