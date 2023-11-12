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
* For sphinx-design go to: https://pypi.org/project/sphinx_design/
* For sphinx-togglebutton go to: https://pypi.org/project/sphinx-togglebutton/

----

Dependencies
--------------

| As of Sept 1 2023, sphinx-rtd-theme 1.3.0 supports sphinx 7.0
| For latest updates and dependencies see: https://sphinx-rtd-theme.readthedocs.io/en/stable/changelog.html


.. code-block::
    
    pip install Sphinx==7.2.6
    pip install sphinx-copybutton==0.5.2
    pip install sphinx-rtd-theme==1.3.0
    pip install sphinx-togglebutton==0.3.2
    pip install sphinx_design==0.5.0

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
    
    pip install sphinx==7.2.6


* To upgrade include the ``-U`` flag.

.. code-block::
    
    pip install -U sphinx==7.2.6


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

----

Install the sphinx-togglebutton Extension
------------------------------------------------------------

* The sphinx-togglebutton Extension adds the ability to Collapse Sphinx admonitions (notes, warnings, etc) so that their content is hidden until users click a toggle button.
* From the cmd prompt install the Sphinx Extension: sphinx-togglebutton:

.. code-block::
    
    pip install sphinx-togglebutton

* To upgrade include the ``-U`` flag:

.. code-block::
    
    pip install -U sphinx-togglebutton

* To use ``sphinx-togglebutton``, make the changes to the conf.py file that are detailed at :ref:`VSCode conf.py`.

----

Install the sphinx_design Extension
------------------------------------------------------------

* The sphinx_design Extension adds drop downs and tabs:

.. code-block::
    
    pip install sphinx_design

* To upgrade include the ``-U`` flag:

.. code-block::
    
    pip install -U sphinx_design

* To use ``sphinx_design``, make the changes to the conf.py file that are detailed at :ref:`VSCode conf.py`.
