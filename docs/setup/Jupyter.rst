==============================
Jupyter
==============================

This is optional. 

It is possible to use Jupyter in Sphinx files. Jupyter-sphinx is a Sphinx extension that executes embedded code in a Jupyter kernel, and embeds outputs of that code in the document. It has support for rich output such as Latex math. It allows live code execution, and thereby, interactive code blocks.

----

docs/requirements.txt
------------------------------

* Add this text in the requirements file ``docs/requirements.txt``::

    notebook==6.4.7
    jupyter-sphinx==0.3.2

----

Install the jupyter notebook
------------------------------

* See https://pypi.org/project/notebook/

* Check the version of jupyter notebook already installed from the command line::

    pip show notebook

* Install the jupyter notebook from the command line::

    pip install notebook

* Update to the latest version of the jupyter notebook from the command line::

    pip install notebook --upgrade

* To install a specific version, type the package name followed by the required version::

    pip install notebook==6.4.2

----

Install the jupyter-sphinx extension
------------------------------------------------------------

* See: https://jupyter-sphinx.readthedocs.io/en/latest/

* Install the jupyter-sphinx extension from the command line::

    pip install jupyter-sphinx
    
----

VSCode conf.py file
------------------------------

* Add this text in to the file: ``docs/conf.py``::

    import os
    import sys
    sys.path.insert(0, os.path.abspath('../../'))
    package_path = os.path.abspath('../..')
    os.environ['PYTHONPATH'] = ':'.join((package_path, os.environ.get('PYTHONPATH', '')))


* Edit the extensions to add ``jupyter_sphinx`` in the file: ``docs/conf.py``::

    extensions = [
        'jupyter_sphinx',
    ]


* To enable interactive cells, add this text in to the file: ``docs/conf.py``::

    jupyter_sphinx_thebelab_config = {
        'requestKernel': True,
        'binderOptions': {
            'repo': "binder-examples/requirements",
        },
    }

----

Enable Jupyter notebook Interactivity
------------------------------------------------------------

* See: https://jupyter-sphinx.readthedocs.io/en/latest/
* Interactive cells are activated with a button click.
* By default the button is added at the end of the document, but it may also be inserted anywhere using::

    .. thebe-button:: Optional title

----

Usage
------------------------------

* Use the jupyter-execute directive to embed code into the document::

    .. jupyter-execute::

    x = 4
    y = 5
    ans = x * y
    print('x * y = ' + str(ans))


