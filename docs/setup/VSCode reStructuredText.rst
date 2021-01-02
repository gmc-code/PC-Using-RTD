.. _VSCode reStructuredText:

==============================
VSCode reStructuredText
==============================

* Make your doc files in VSCode using reStructuredText .rst files.
* Use reStructuredText formatting syntax in your docs files.
* Some important details are specified below.
* For more details, see: https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html
* For a compact cheat sheet, see: https://docutils.sourceforge.io/docs/user/rst/cheatsheet.txt

index.rst
==============================
* Edit ``index.rst`` to include introductory info at the top.
* Edit ``index.rst`` to list other project .rst file names under table of contents directives.

.. tip::
   index.rst should at least contain the table of contents ``.. toctree::`` directive.

documentation as .rst files
==============================
* Make your doc files in VSCode using reStructuredText .rst files.

.. tip::
   .rst files must contain a fully underlined heading to work properly::

        Heading
        =======


Images
==============================
* Images in a subfolder can be added to .rst files using the directive ``.. image:: images/myimage.png``.

.. tip::
    
    Image path issue

    * It is possible to use ``/../docs/images/`` as the path to an images folder but those images don't display in files in github
    * It is best to use images in each docs subfolder for those .rst file with images instead of trying to use one common folder for all images.
    * eg. ``.. image:: tutorials/images/mytut.jpg`` in the file ``tutorials/mytutinfo.rst``



Sample code
==============================
* Python code blocks can be set out like the example below using the directive ``.. code-block:: python``.
* Python line numbers can be included using the ``:linenos:`` option. ::

    .. code-block:: python
        :linenos:
    
        from microbit import *

        x = 0
        for y in range(0, 5):
            display.set_pixel(x, y, 9)


* This displays as:

.. code-block:: python
    :linenos:

    from microbit import *

    x = 0
    for y in range(0, 5):
        display.set_pixel(x, y, 9)



View docs as html
==============================
There are a few different ways to view how the documentation will look before pushing it to GitHub and viewing it in RTDs.
The first option below displays a preview of the .rst file.
The second and third option require the use of Sphinx to build the html output.

View docs as html in VSCode
------------------------------
* Install the ``HTML preview`` extension in VSCode, then use the Open Preview to the Side icon at the top right of the window to preview an open .rst file.


View docs as html
------------------------------
* Press :kbd:`ctrl` + :kbd:`⇧shift` + :kbd:`\`` to open the VSCode terminal.
* Make sure that the terminal folder is the docs folder.
* eg: C:\\projects\\project-name\\docs

* Build an html version of the docs. ::

    make clean
    make html

* ``make clean`` is need first since Sphinx only rebuilds pages that have changed.

* Open the index file ``_build/html/index.html`` in a web browser to see the docs.
* The html can also be viewed in the browser using the VSCode terminal. ::

    start chrome _build/html/index.html


View docs as html using localhost
------------------------------------------------------------
* Press :kbd:`ctrl` + :kbd:`⇧shift` + :kbd:`\`` to open the VSCode terminal.
* Make sure that the terminal folder is the docs folder.
* eg: C:\\projects\\project-name\\docs

* Build an html version of the docs using the the VSCode terminal. ::

    .\make clean
    .\make html

* Create a local server using the the VSCode terminal. ::

    python -m http.server


* Open the localhost in the browser: http://localhost:8000/_build/html/
* The html can also be viewed in the browser using the the VSCode terminal. ::
    
    start chrome http://localhost:8000/_build/html/


.. tip::
    Sometimes ``.\`` will be needed with ``make`` ::

        .\make clean
        .\make html


