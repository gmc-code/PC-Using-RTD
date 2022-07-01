==============================
Jupyter
==============================

This is optional. 

It is possible to use Jupyter in Sphinx files. 

For the ability to edit the python code live and view the ouput there are two options:
    * jupyter-sphinx
    * sphinx-thebe

For the ability to view the ouput from jupyter notebook files use:
    * nbsphinx

For the ability to convert the docs rst files to jupyter notebook files use:
    * sphinxcontrib-jupyter
  
----

-------------------
Jupyter-sphinx
-------------------

Jupyter-sphinx is a Sphinx extension that executes embedded code in a Jupyter kernel, and embeds outputs of that code in the document. It has support for rich output such as Latex math. It allows live code execution, and thereby, interactive code blocks.

It has the drawback that it is not fully compatable with the sphinx-copybutton extension. When both are used together the text "Copy to clipboard" has to be manually deleted form the live python code before it will run properly.

----

Install the jupyter-sphinx extension
--------------------------------------

* See: https://pypi.org/project/jupyter-sphinx/
* See: https://jupyter-sphinx.readthedocs.io/en/latest/

* Install the jupyter-sphinx extension from the command line.

.. code-block::

    pip install jupyter-sphinx
    
----

docs/requirements.txt
------------------------------

* Add this text in the requirements file ``docs/requirements.txt``:

.. code-block::
    
    jupyter-sphinx==0.4.0
    
----

VSCode conf.py file
------------------------------

* Add this text into the file: ``docs/conf.py``.

.. code-block::

    import os
    import sys

    sys.path.insert(0, os.path.abspath('../../'))
    package_path = os.path.abspath('../..')
    os.environ['PYTHONPATH'] = ':'.join((package_path, os.environ.get('PYTHONPATH', '')))


* Edit the extensions to add ``jupyter_sphinx`` in the file: ``docs/conf.py``.

.. code-block::

    extensions = [
        'jupyter_sphinx',
    ]


* To enable interactive cells, add this text into the file: ``docs/conf.py``.

.. code-block::

    jupyter_sphinx_thebelab_config = {
        'requestKernel': True,
        'binderOptions': {
            'repo': "binder-examples/requirements",
        },
    }

----

Usage
----------------

* Use the jupyter-execute directive to embed code into the document.

.. code-block::

    .. jupyter-execute::

        x = 4
        y = 5
        ans = x * y
        print('x * y = ' + str(ans))

----

* Interactive cells are activated with a button click.
* By default the button is added at the end of the document, but it may also be inserted anywhere using:

.. code-block::

    .. thebe-button:: Optional title

----

-------------------
sphinx-thebe
-------------------

| The sphinx-thebe extension makes code cells interactive with a kernel provided by Thebe and Binder.
| The drawback is that is is not compatiable with the latest version of Sphinx. Instead it requires sphinx==4.5.0.

----

Install the sphinx-thebe extension
--------------------------------------

* See: https://pypi.org/project/sphinx-thebe/
* See: https://sphinx-thebe.readthedocs.io/en/latest/

* Install the sphinx-thebe extension from the command line.

.. code-block::

    pip install sphinx-thebe
    
----

docs/requirements.txt
------------------------------

* Add this text in the requirements file ``docs/requirements.txt``:

.. code-block::
    
    sphinx==4.5.0
    sphinx-thebe==0.1.2 

----

VSCode conf.py file
------------------------------

* Edit the extensions to add ``jupyter_sphinx``, in the file: ``docs/conf.py``.

.. code-block::

    extensions = [
        'sphinx_thebe',
    ]

----

Usage
----------------

* Interactive cells are activated with a button click.
* Insert the button anywhere using:
  
.. code-block::

    .. thebe-button:: Activate Jupyter

----

class: thebe
--------------------

* Use the ``:class: thebe`` directive in a python code block to give thebe access to run the code.

.. code-block:: python
    :class: thebe

    def name_age_greeting(name, age):
        age += 1
        return "Hi " + name + ", you are " + str(age) + " years old"

    print(name_age_greeting("Joe", 12))


----

-------------------
nbsphinx
-------------------

| nbsphinx allows the use of jupyter notebook files, ``.ipynb``, with sphinx.

----

Install the nbsphinx extension
--------------------------------------

| See: https://pypi.org/project/nbsphinx/
| See: https://nbsphinx.readthedocs.io/
| See: https://docs.readthedocs.io/en/stable/guides/jupyter.html

* Install the nbsphinx extension from the command line.

.. code-block::

    pip install nbsphinx
    
* To edit .ipynb files in VSCode install the ipykernel package.

----

VSCode Jupyter extension
------------------------------------------------------------

* In VSCode, click the Extensions icon in the left side bar.
* Type ``Jupyter`` into the search box.
* Install the Jupyter extension.
  
* To edit .ipynb files in VSCode install the python ipykernel package.
* See: https://pypi.org/project/ipykernel/
* See: https://ipython.org/
  
.. code-block::
    
    pip install ipykernel

----

docs/requirements.txt
------------------------------

* Add this text in the requirements file ``docs/requirements.txt``:

.. code-block::
    
    nbsphinx==0.8.9 

----

VSCode conf.py file
------------------------------

* Edit the extensions to add ``nbsphinx``, in the file: ``docs/conf.py``.

.. code-block::

    extensions = [
        'nbsphinx',
    ]

----

Usage
----------------

| Edit the index.rst and add the names of .ipynb files to the toctree.

----

------------------------
sphinxcontrib-jupyter
------------------------

| sphinxcontrib-jupyter converts rst files into jupyter notebook files, ``.ipynb``, with sphinx.

----

Install the sphinxcontrib-jupyter extension
--------------------------------------

| See: https://pypi.org/project/sphinxcontrib-jupyter/
| See: https://sphinxcontrib-jupyter.readthedocs.io/en/latest/

* Install the sphinxcontrib-jupyter extension from the command line.

.. code-block::

    pip install sphinxcontrib-jupyter
    
----

VSCode conf.py file
------------------------------

* Edit the extensions to add ``nbsphinx``, in the file: ``docs/conf.py``.

.. code-block::

    extensions = [
        'sphinxcontrib.jupyter',
    ]

----

Usage
----------------

| To build a collection of Jupyter notebooks for the Sphinx Project:
| From the terminal, run:

.. code-block::

    cd docs
    .\make jupyter

