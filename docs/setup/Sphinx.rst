==============================
Sphinx
==============================

Sphinx is a documentation generator. This means that it takes a bunch of source files in plain text, and generates a bunch HTML. For our use case it takes plain text files in reStructuredText format, and outputs HTML.


All pip installed versions
-----------------------------

* Check the installed version of sphinx, sphinx_rtd_theme and sphinx-copybutton with::

    pip list


Install Sphinx
------------------------------

* Press :kbd:`Win` + :kbd:`X` + :kbd:`C` to open the Command prompt. 
* From the cmd prompt install the Sphinx library (v4.1.2 at Aug 2021)::

    pip install sphinx


* To upgrade include the ``-U`` flag::

    pip install -U sphinx



* See https://pypi.org/project/Sphinx/

* Check the installed version with::

    sphinx-build --version

----

Install the Sphinx theme for Read the Docs 
------------------------------------------------------------

* The sphinx_rtd_theme is used by other RTD guides, so it is best to use for consistency of look and feel.
* From the cmd prompt install the Sphinx theme (v0.5.2 at Aug 2021) for read the docs::

    pip install sphinx_rtd_theme

* To upgrade include the ``-U`` flag::

    pip install -U sphinx_rtd_theme


* See https://pypi.org/project/sphinx-rtd-theme/
* To use ``sphinx_rtd_theme``, make the changes to the conf.py file that are detailed at :ref:`VSCode conf.py`.

----

Install the sphinx-copybutton Extension
------------------------------------------------------------

* The sphinx-copybutton Extension adds a copy button to code blocks.
* From the cmd prompt install the Sphinx Extension: sphinx-copybutton (v0.4.0 at Aug 2021)::

    pip install sphinx-copybutton

* To upgrade include the ``-U`` flag::

    pip install -U sphinx-copybutton


* See https://pypi.org/project/sphinx-copybutton/
* To use ``sphinx-copybutton``, make the changes to the conf.py file that are detailed at :ref:`VSCode conf.py`.

