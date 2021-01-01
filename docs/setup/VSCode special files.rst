.. _VSCode special files:

VSCode special files
====================================

Add files
---------------
#. Add the ``.gitignore`` file using the VSCode terminal. Run from within the **project** folder. ::

    type nul > .gitignore


#. Add the three files using the VSCode terminal. Run from within the **docs** folder. ::

    type nul > requirements.txt
    type nul > .readthedocs.yml
    type nul > .gitignore
    
#. Add the ``_templates/breadcrumbs.html`` file using the VSCode terminal. Run from within the **docs** folder. ::

    type nul > _templates/breadcrumbs.html


.. tip::
   If using windows powershell as the terminal, adding files from the terminal can be done using the following:
   ``ni filename``
   e.g. ni requirements.txt 



docs/requirements.txt
---------------------------
* Use a requirements file ``docs/requirements.txt`` to specify the version of Sphinx.
* See: https://docs.readthedocs.io/en/stable/guides/specifying-dependencies.html
* Use this text in the requirements file with the version numbers you are using: ::

    sphinx==3.4.1
    sphinx_rtd_theme==0.5.0
    sphinx-copybutton==0.3.1

* To get the installed version numbers, check the output from typing in the VSCode terminal: ::

    pip list

* To see if there are updates available, check the output from typing in the VSCode terminal: ::

    pip list -o


docs/.readthedocs.yml
----------------------------
* Use a config file ``docs/.readthedocs.yml`` so that the requirements file can be used.
* Get the file contents from the main example at: https://docs.readthedocs.io/en/stable/config-file/v2.html


docs/.gitignore
------------------------
* Use a ``docs/.gitignore`` file so that the build folder is ignored when pushing the docs to the github repo.
* Set the contents of the file ``.gitignore``: ::

    _build


.gitignore
----------------
* To prevent the .vscode folder from being pushed to GitHub, use a ``.gitignore`` file in the project folder.
* To release any .vscode files that may have been previously cached by git use in the VSCode terminal: ``git rm -r --cached .vscode``.
* Set the contents of the file ``.gitignore``: ::

    **/.vscode

* See https://git-scm.com/docs/gitignore for use of ``.gitignore``.


breadcrumbs.html
------------------------------------------
* Use a ``docs/_templates/breadcrumbs.html`` to remove the top right ``Edit on GitHub`` button in RTDs that links to the github repo.
* Set the contents of the file ``breadcrumbs.html``::

    {%- extends "sphinx_rtd_theme/breadcrumbs.html" %}

    {% block breadcrumbs_aside %}
    {% endblock %}

* See https://docs.readthedocs.io/en/latest/guides/remove-edit-buttons.html


custom css
----------------------
* Add a folder ``css`` to the ``_static`` folder. ::

    mkdir _static/css

* Add a ``custom css`` file containing any css that will override the theme css.

    type nul > _static/css/custom.css

* As per :ref:`custom css`; add the code below to the ``Options for HTML output`` section of ``conf.py`` file to use the custom css. ::

    html_css_files = ['css/custom.css']

* See: :download:`custom.css <../_static/css/custom.css>`.
* This contains custom css including that used in these docs for inline reST and the copy button extension used for code blocks.
* See more deails at: https://docs.readthedocs.io/en/latest/guides/adding-custom-css.html


custom logos
----------------------

* Add a ``logo.png`` file to the ``_static`` folder, with width <= 200 pixels. To save room, use a height <=50 pixels.>

* As per :ref:`custom logo`; add the code below to the ``Options for HTML output`` section of ``conf.py`` file to use the custom logo. ::

    html_logo = '_static/logo.png'

* Add a ``favicon.ico`` file to the ``_static`` folder, with size 32 x 32 pixels.

* As per :ref:`custom logo`; add the code below to the ``Options for HTML output`` section of ``conf.py`` file to use the custom logo. ::

    html_favicon = "_static/favicon.ico"

* See https://www.sphinx-doc.org/en/master/usage/configuration.html

