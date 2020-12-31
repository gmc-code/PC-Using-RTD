.. _VSCode Project Folder and Sphinx:

VSCode Project Folder and Sphinx
==================================

Create docs folder
---------------------
* Create a project folder with the same name that will be used in GitHub for the repository name. See :ref:`GitHub new repo`
* Open a project folder from within VSCode.
* Press :kbd:`ctrl` + :kbd:`⇧shift` + :kbd:`\`` to open the VSCode terminal. 
* From the VSCode terminal, create a docs folder within the project folder::

    mkdir docs


* eg: C:\\Users\\myname\\project-name\\docs
* From the VSCode terminal, change directory to the docs folder e.g.::

    cd docs

sphinx-quickstart
---------------------
* From the VSCode terminal, run from within the docs folder: ::

    sphinx-quickstart

* Use defaults by pressing enter at each prompt apart from:

    * Enter Name of project
    * Enter Author name


* Several subfolders are created.
* These key files are created:

    * conf.py
    * index.rst
    * Makefile
    * make.bat

For more info on Sphinx, see: https://www.sphinx-doc.org/en/master/usage/quickstart.html

