.. _VSCode special files:

==============================
VSCode special files
==============================

Add files
------------------------------

* Add the ``.gitignore`` file using the VSCode terminal. Run from within the **project** folder.

.. code-block::

    type nul > .gitignore
    type nul > .readthedocs.yaml

* Add the files below using the VSCode terminal. Run from within the **docs** folder.

.. code-block::

    type nul > requirements.txt
    type nul > .gitignore
    
* Add the ``_templates/breadcrumbs.html`` file using the VSCode terminal. Run from within the **docs** folder.

.. code-block::

    type nul > _templates/breadcrumbs.html


.. tip::

    If using windows powershell as the terminal, adding files from the terminal can be done using the following:
    ``ni filename``
    e.g. ni requirements.txt 

----

docs/requirements.txt
------------------------------

* Use a requirements file ``docs/requirements.txt`` to specify the version of Sphinx and extensions to sphinx for read the docs.
* See: https://docs.readthedocs.io/en/stable/guides/specifying-dependencies.html
  
* Use this text in the requirements file with the version numbers you are using:
* As of Sep 2023, read the docs uses python 3.11.

.. code-block:: 

    Sphinx==7.2.6
    sphinx-copybutton==0.5.2
    sphinx-rtd-theme==1.3.0
    sphinx-togglebutton==0.3.2
    sphinx_design==0.5.0

* If the version numbers are left off, read the docs will fetch the latest version that is compatible with the version of python it is using.
* There is no need to include explicitly docutils, since it will be taken care of along withe the Sphinx requirement. 

.. code-block::

    sphinx
    sphinx_rtd_theme
    sphinx-copybutton

    # useful sphinx extensions
    sphinx-design
    sphinx-togglebutton

    # for interactive jupyter 
    notebook
    jupyter-sphinx
    sphinx-thebe

----

docs/.readthedocs.yaml
------------------------------

* Use a config file ``.readthedocs.yaml`` so that the requirements file can be used.
* Get the file contents from the main example at: https://docs.readthedocs.io/en/stable/config-file/v2.html
* This sets some of the advanced settings for read the docs that would otherwise be accessed by Admin:Advance Settings in Read The Docs.
* e.g the setting to Build PDF or ePub are controlled in the .yaml file.

----

docs/.gitignore
------------------------------

* Use a ``docs/.gitignore`` file so that the build folder is ignored when pushing the docs to the github repo.
* Set the contents of the file ``.gitignore``:

.. code-block::

    _build

----

.gitignore
------------------------------

* To prevent the .vscode folder from being pushed to GitHub, use a ``.gitignore`` file in the project folder.
* To release any .vscode files that may have been previously cached by git use in the VSCode terminal: ``git rm -r --cached .vscode``.
* Set the contents of the file ``.gitignore``:

.. code-block::

    **/.vscode

* See https://git-scm.com/docs/gitignore for use of ``.gitignore``.

----

Fixing .gitignore that isn't working
---------------------------------------

There could be several reasons why your `.gitignore` file is not working as expected such as **Files already tracked by Git**: `.gitignore` only ignores untracked files. If the files are already being tracked by Git, you need to remove them from the repository and add them back, this time respecting the rules in your `.gitignore`. You can do this with the following commands:

.. code-block::

    git rm -rf --cached .
    git add .

----

breadcrumbs.html
------------------------------

* Use a ``docs/_templates/breadcrumbs.html`` to remove the top right ``Edit on GitHub`` button in RTDs that links to the github repo.
* Set the contents of the file ``breadcrumbs.html``.

.. code-block::

    {%- extends "sphinx_rtd_theme/breadcrumbs.html" %}

    {% block breadcrumbs_aside %}
    {% endblock %}

* See https://docs.readthedocs.io/en/latest/guides/remove-edit-buttons.html

----

Custom css
------------------------------

* Add a folder ``css`` to the ``_static`` folder.

.. code-block::

    mkdir _static/css

* Add a ``custom css`` file containing any css that will override the theme css.

.. code-block::

    type nul > _static/css/custom.css

* As per :ref:`custom css`; add the code below to the ``Options for HTML output`` section of ``conf.py`` file to use the custom css.

.. code-block::

    html_css_files = ['css/custom.css']

* See: :download:`custom.css <../_static/css/custom.css>`.
* This contains custom css including that used in these docs for inline reST and the copy button extension used for code blocks.
* See more details at: https://docs.readthedocs.io/en/latest/guides/adding-custom-css.html

----

Custom logos
------------------------------

* Add a ``logo.png`` file to the ``_static`` folder, with width <= 200 pixels. To save room, use a height <=50 pixels.>

* As per :ref:`custom logo`; add the code below to the ``Options for HTML output`` section of ``conf.py`` file to use the custom logo.

.. code-block::

    html_logo = '_static/logo.png'

* Add a ``favicon.ico`` file to the ``_static`` folder, with size 32 x 32 pixels.

* As per :ref:`custom logo`; add the code below to the ``Options for HTML output`` section of ``conf.py`` file to use the custom logo.

.. code-block::

    html_favicon = "_static/favicon.ico"

* See https://www.sphinx-doc.org/en/master/usage/configuration.html

