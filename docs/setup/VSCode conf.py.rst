.. _VSCode conf.py:

==============================
VSCode conf.py file
==============================

In VSCode, edit the ``conf.py`` file in the docs folder.

----

sphinx_rtd_theme
------------------------------

* Use the sphinx_rtd_theme for html display on the ReadTheDocs website.

* The Project information section of ``conf.py`` should have

.. code-block::
    
    import sphinx_rtd_theme

* Change ``html_theme = 'alabaster'`` to ``html_theme = 'sphinx_rtd_theme'``

.. code-block::

    html_theme = 'sphinx_rtd_theme'

* Add ``'sphinx_rtd_theme'`` to the extensions list:

.. code-block::

    extensions = [
        'sphinx_rtd_theme'
    ]

----

sphinx-rtd-theme Theme Options 
------------------------------

* See: https://sphinx-rtd-theme.readthedocs.io/en/latest/configuring.html
* Add the code below to ``conf.py`` with these suggested options:

.. code-block::

    html_theme_options = {
        'logo_only': False,
        'display_version': False,  # False so doc version not shown
        'prev_next_buttons_location': 'both',  # Can be bottom, top, both , or None
        'style_external_links': True,  # True to Add an icon next to external links
        'style_nav_header_background': 'linear-gradientlinear-gradient(to right, blueviolet 15%, limegreen 50%, royalblue 80%)',  # blue
        # Toc options
        'collapse_navigation': False,  # False so nav entries have the [+] icons
        'sticky_navigation': False,  # False so the nav does not scroll
        'navigation_depth': 4,  # -1 for no limit
        'includehidden': True,  # displays toctree that are hidden
        'titles_only': False  # False so page subheadings are in the nav.
    }

----

.. _custom css:

Custom css
------------------------------

* Add the code below to the ``Options for HTML output`` section of ``conf.py`` to use the custom css in the ``_static/css/custom.css`` file.

.. code-block::

    html_css_files = ['css/custom.css']

----

.. _custom logo:

Custom logo
------------------------------

* Add the code below to the ``Options for HTML output`` section of ``conf.py`` to use the custom logo in the ``_static/logo.png`` file.

.. code-block::

    html_logo = '_static/logo.png'

* Add the code below to the ``Options for HTML output`` section of ``conf.py`` to use the custom favicon in the ``_static/favicon.ico`` file.

.. code-block::

    html_favicon = "_static/favicon.ico"


