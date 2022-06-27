.. _VSCode Project Folder and Sphinx:

============================================================
VSCode Project Folder and Sphinx
============================================================

Create docs folder
------------------------------

* Create a project folder with the same name that will be used in GitHub for the repository name. See :ref:`GitHub new repo`
* Open a project folder from within VSCode.
* Press :kbd:`ctrl` + :kbd:`shift` + :kbd:`\`` to open the VSCode terminal. ` 
* From the VSCode terminal, create a docs folder within the project folder.
  
.. code-block::

        mkdir docs


* eg: C:/projects/project-name/docs
* From the VSCode terminal, change directory to the docs folder e.g.
  
.. code-block::

    cd docs

----

Sphinx-quickstart
------------------------------

* For more info on Sphinx, see: https://www.sphinx-doc.org/en/master/usage/quickstart.html
* From the VSCode terminal, run from within the docs folder:

.. code-block::

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

The top-level ``docs`` directory in the main project directory. Inside of this is:

``index.rst``:
    This is the index file for the documentation. It contains a Table of Contents that will link to all other pages of the documentation.

``conf.py``:
    This is used for customization of Sphinx.

``Makefile & make.bat``:
    This is the main interface for local development, and shouldn't be changed.

``_build``:
    The directory that your output files go into when ``make html`` is run.

``_static``:
    The directory to include all your static files, like css and logo images.

``_templates``:
    To override Sphinx templates to customize look and feel.


