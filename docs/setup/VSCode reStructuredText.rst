.. _VSCode reStructuredText:

==============================
VSCode reStructuredText
==============================

Usage
------------------------------

* Make your doc files in VSCode using reStructuredText .rst files.
* Use reStructuredText formatting syntax in your docs files.
* Some important details are specified below.
* For more details, see: https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html
* For a compact cheat sheet, see: https://docutils.sourceforge.io/docs/user/rst/cheatsheet.txt

----

index.rst
------------------------------

* Edit ``index.rst`` to include introductory info at the top.
* Edit ``index.rst`` to list other project .rst file names under table of contents directives.

.. tip::

    index.rst should at least contain the table of contents ``.. toctree::`` directive.

----

Documentation as .rst files
------------------------------

* Make your doc files in VSCode using reStructuredText .rst files.

.. tip::

    .rst files must contain a fully underlined heading to work properly

    .. code-block::
    
        Heading
        =======

    Overlining and underlined a heading also works.

    .. code-block::
    
        =======
        Heading
        =======
        
----

Images
------------------------------

* Images in a subfolder can be added to .rst files using the directive ``.. image:: images/myimage.png``.

.. tip::
    
    Image path issue

    * It is possible to use ``/../docs/images/`` as the path to an images folder but those images don't display in files in github
    * It is best to use images in each docs subfolder for those .rst file with images instead of trying to use one common folder for all images.
    * eg. ``.. image:: tutorials/images/mytut.jpg`` in the file ``tutorials/mytutinfo.rst``

----

Sample code
------------------------------

* Python code blocks can be set out like the example below using the directive ``.. code-block:: python``.
* Python line numbers can be included using the ``:linenos:`` option.



.. code-block::

    .. code-block:: python
        :linenos:

        from microbit import *

        x = 0
        for y in range(0, 5):
            display.set_pixel(x, y, 9)


| This displays as:

.. code-block:: python
    :linenos:

    from microbit import *

    x = 0
    for y in range(0, 5):
        display.set_pixel(x, y, 9)



