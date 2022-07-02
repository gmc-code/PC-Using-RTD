==============================
Sphinx
==============================

Sphinx is a documentation generator. This means that it takes source files in plain text, and generates HTML files. In our case, it takes plain text files in reStructuredText format, and outputs HTML.

----

Installations
-----------------------------

| Sphinx and some useful extentions can be installed individually or via a requirements.txt file.
| For installing all in one go via a requirements.txt file steps: :ref:`Python requirements`.


* See https://pypi.org/project/Sphinx/
  
----

Suggested Sphinx extensions
-----------------------------

Sphinx and the following suggested extensions can be installed individaully or via the requirements.txt file.

* For sphinx-rtd-theme go to: https://pypi.org/project/sphinx-rtd-theme/
* For sphinx-copybutton go to: https://pypi.org/project/sphinx-copybutton/
* For sphinx-copybutton css go to:https://github.com/executablebooks/sphinx-copybutton/blob/master/sphinx_copybutton/_static/copybutton.css
  
    sphinx-design==0.2.0
    sphinx-togglebutton==0.3.1
    
----

All pip installed versions
-----------------------------

* Check the installed version of sphinx, sphinx_rtd_theme and sphinx-copybutton with:

.. code-block::
    
    pip list

----

Install Sphinx
------------------------------

* Press :kbd:`Win` + :kbd:`X` + :kbd:`C` to open the Command prompt. 
* From the cmd prompt install the Sphinx library.

.. code-block::
    
    pip install sphinx


* To upgrade include the ``-U`` flag.

.. code-block::
    
    pip install -U sphinx


* Check the installed version with:

.. code-block::
    
    sphinx-build --version

----

Install the Sphinx theme for Read the Docs 
------------------------------------------------------------

* The sphinx_rtd_theme is used by other RTD guides, so it is best to use for consistency of look and feel.
* From the cmd prompt install the Sphinx theme for read the docs.

.. code-block::
    
    pip install sphinx_rtd_theme

* To upgrade include the ``-U`` flag.

.. code-block::
    
    pip install -U sphinx_rtd_theme

* To use ``sphinx_rtd_theme``, make the changes to the conf.py file that are detailed at :ref:`VSCode conf.py`.

----

Install the sphinx-copybutton Extension
------------------------------------------------------------

* The sphinx-copybutton Extension adds a copy button to code blocks.
* From the cmd prompt install the Sphinx Extension: sphinx-copybutton:

.. code-block::
    
    pip install sphinx-copybutton

* To upgrade include the ``-U`` flag:

.. code-block::
    
    pip install -U sphinx-copybutton

* To use ``sphinx-copybutton``, make the changes to the conf.py file that are detailed at :ref:`VSCode conf.py`.

