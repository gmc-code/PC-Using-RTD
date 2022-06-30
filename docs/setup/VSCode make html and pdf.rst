.. _VSCode reStructuredText:

==============================
VSCode make html and pdf
==============================

View docs as html
------------------------------

There are a few different ways to view how the documentation will look before pushing it to GitHub and viewing it in RTDs.
The first option below displays a preview of the .rst file.
The second and third option require the use of Sphinx to build the html output.

----

View docs as html in VSCode
------------------------------

* Install the ``reStructuredText`` extension in VSCode, then use the Open Preview to the Side icon at the top right of the window to preview an open .rst file.

----

View docs as html
------------------------------

* Press :kbd:`ctrl` + :kbd:`shift` + :kbd:`\`` to open the VSCode terminal.
* Make sure that the terminal folder is the docs folder.
* eg: C:/projects/project-name/docs

* Build an html version of the docs.

.. code-block::

    make clean
    make html

* ``make clean`` is needed first since Sphinx only rebuilds pages that have changed.

* Open the index file ``_build/html/index.html`` in a web browser to see the docs.
* The html can also be viewed in the browser using the VSCode terminal.

.. code-block::

    start chrome _build/html/index.html

* Add the VSCode extension ``open in browser`` to add the command ``open in default browser`` to the pop up menu when right clicking the html file in VSCode explorer panel.

----

View docs as html using localhost
------------------------------------------------------------

* Press :kbd:`ctrl` + :kbd:`shift` + :kbd:`\`` to open the VSCode terminal.
* Make sure that the terminal folder is the docs folder.
* eg: C:/projects/project-name/docs

* Build an html version of the docs using the the VSCode terminal.

.. code-block::

    make clean
    make html

* Create a local server using the the VSCode terminal.

.. code-block::

    python -m http.server


* Open the localhost in the browser: http://localhost:8000/_build/html/
* The html can also be viewed in the browser using the the VSCode terminal.

.. code-block::
    
    start chrome http://localhost:8000/_build/html/


.. tip::
    Sometimes ``.\`` will be needed with ``make``

.. code-block::

        .\make clean
        .\make html

----

View docs as pdf
------------------------------

Make the latex build then create the pdf from the .tex file.

----

Make latex
------------------------------

* Press :kbd:`ctrl` + :kbd:`shift` + :kbd:`\`` to open the VSCode terminal.
* Make sure that the terminal folder is the docs folder.
* eg: C:/projects/project-name/docs

* Build a latex version of the docs.

.. code-block::

    make clean
    make latex


* Change directory to ``_build/latex``

.. code-block::

    cd _build\latex


* Create the pdf from the .tex file.

.. code-block::

    xelatex PC-Using-RTD.tex

