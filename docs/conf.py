# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html


# -- Project information -----------------------------------------------------


import sphinx_rtd_theme
project = 'PC-Using-RTD'
copyright = '2020-1, GMC'
author = 'GMC'

# -- General configuration ---------------------------------------------------
# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx_rtd_theme',
    'sphinx_copybutton'
]


# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
# source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.
# See the documentation for a list of builtin themes.
html_theme = 'sphinx_rtd_theme'

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
# html_title = None
html_title = "PC-Using-RTD"

# Use custom css
html_css_files = ['css/custom.css']

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# -- sphinx-rtd-theme Theme Options ------------------------------------------
# See: https://sphinx-rtd-theme.readthedocs.io/en/latest/configuring.html
html_theme_options = {
    'logo_only': False,  # False so text is shown
    'display_version': False,  # False so doc version not shown
    'prev_next_buttons_location': 'both',  # Can be bottom, top, both , or None
    'style_external_links': True,  # True to Add an icon next to external links
    # 'style_nav_header_background': 'blue',
    'style_nav_header_background': 'linear-gradient(to right, blueviolet 15%, limegreen 50%, royalblue 80%)',
    # Toc options
    'collapse_navigation': False,  # False so nav entries have the [+] icons
    'sticky_navigation': False,  # False so the nav does not scroll
    'navigation_depth': 4,  # -1 for no limit
    'includehidden': True,  # displayes toctree that are hidden
    'titles_only': False  # False so page subheadings are in the nav.
}

# -- RTDs logos -------------------------------------------------
html_favicon = "_static/favicon.ico"
html_logo = "_static/logo.png"


# -- Options for LaTeX output ------------------------------------------------
# see https://sphinxguide.readthedocs.io/en/latest/sphinx_basics/settings.html for latex code


latex_engine = 'xelatex'  # pdflatex'
latex_elements = {
    # need to use svgcolour names for title and tip border
    'passoptionstopackages': r'\PassOptionsToPackage{svgnames}{xcolor}',
    #
    # The paper size ('letterpaper' or 'a4paper').
    #
    'papersize': 'a4paper',
    'releasename': " ",
    # Sonny, Lenny, Glenn, Conny, Rejne, Bjarne and Bjornstrup
    'fncychap': '\\usepackage[Rejne]{fncychap}',
    # 'fncychap': '\\usepackage{fncychap}',
    'fontpkg': '\\usepackage{amsmath,amsfonts,amssymb,amsthm}',

    'figure_align': 'htbp',
    # The font size ('10pt', '11pt' or '12pt').
    #
    'pointsize': '12pt',

    # Additional stuff for the LaTeX preamble.
    #
    'preamble': r'''
        %%%%%%%%%%%%%%%%%%%% preamble %%%%%%%%%%%%%%%%%%
        %%%add number to subsubsection 2=subsection, 3=subsubsection
        %%% below subsubsection is not good idea.
        \setcounter{secnumdepth}{3}
        %
        %%%% Table of content upto 2=subsection, 3=subsubsection
        \setcounter{tocdepth}{2}

        \usepackage{amsmath,amsfonts,amssymb,amsthm}
        \usepackage{graphicx}

        %%% reduce spaces for Table of contents, figures and tables
        %%% it is used "\addtocontents{toc}{\vskip -1.2cm}" etc. in the document
        \usepackage[notlot,nottoc,notlof]{}

        \usepackage{color}
        \usepackage{transparent}
        \usepackage{eso-pic}
        \usepackage{lipsum}
    
        %% spacing between line
        \usepackage{setspace}
        %%%%\onehalfspacing
        %%%%\doublespacing
        \singlespacing

        %%%%%%%%%%% datetime
        \usepackage{datetime}
        \newdateformat{MonthYearFormat}{%
            \monthname[\THEMONTH], \THEYEAR}

        %%% page
        \fancyfoot[LO, LE]{\thepage}

        %%%\renewcommand{\headrulewidth}{0.3pt}
        %%%\renewcommand{\footrulewidth}{0.3pt}

        % \RequirePackage{tocbibind} %%% comment this to remove page number for following
        % \addto\captionsenglish{\renewcommand{\contentsname}{Table of contents}}
        % \addto\captionsenglish{\renewcommand{\chaptername}{Chapter}}


        %%reduce spacing for itemize
        % \usepackage{enumitem}
        % \setlist{nosep}

        %%%%%%%%%%% Quote Styles at the top of chapter  use by reST directive: .. epigraph::
        % \usepackage{epigraph}
        % \setlength{\epigraphwidth}{0.8\columnwidth}
        % \newcommand{\chapterquote}[2]{\epigraphhead[60]{\epigraph{\textit{#1}}{\textbf {\textit{--#2}}}}}
        %%%%%%%%%%% Quote for all places except Chapter
        % \newcommand{\sectionquote}[2]{{\quote{\textit{``#1''}}{\textbf {\textit{--#2}}}}}
    ''',


    'maketitle': r'''
        \pagenumbering{Roman} %%% to avoid page 1 conflict with actual page 1

        \begin{titlepage}
            \centering

            \vspace*{10mm} %%% * is used to give space from top
            \textbf{\Huge {PC-USING-RTD}}

            \vspace{0mm}
            \begin{figure}[!h]
                \centering
                \includegraphics[scale=1.0]{logo.png}
            \end{figure}

            \vspace{0mm}
            \Large \textbf{{GMC}}

            \small Created : Jan 2021

            \vspace*{0mm}
            \small  Last updated : \MonthYearFormat\today

        \end{titlepage}

        \clearpage
        \pagenumbering{roman}
        \tableofcontents
        \clearpage
        \pagenumbering{arabic}

        ''',
    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',

    # Latex colours named see: https://www.latextemplates.com/svgnames-colors
    # sphinx latex see https://www.sphinx-doc.org/en/master/latex.html
    # cautionborder = 3pt,
    # cautionBgColor = {named}{LightCyan}}
    # \usepackage{titlesec}
    # \titleformat{\section}[block]{Large \filcenter}{}{1em}{} %\sffamily
    # \titleformat{\subsection}[hang]{\filright \itshape}{}{1em}{}
    # %\titleformat{\chapter}[hang]{\filright \bfseries}{}{1em}{}
    # InnerLinkColor default {rgb}{0.208, 0.374, 0.486}. linkcolor and citecolor.
    # OuterLinkColor default {rgb}{0.216, 0.439, 0.388}. filecolor, menucolor, and urlcolor.
    # TitleColor default {rgb}{0.126, 0.263, 0.361}. titles(as configured via use of package “titlesec”.)
    # {named}{NavyBlue}

    'sphinxsetup': \
    'hmargin={0.7in,0.7in}, vmargin={0.7in,0.7in}, \
        verbatimwithframe=true, \
        VerbatimBorderColor = {named}{LightGrey}, \
        noteBorderColor = {named}{LightGrey}, \
        hintBorderColor = {named}{LightGrey}, \
        importantBorderColor = {named}{LightGrey}, \
        tipBorderColor = {named}{LightGrey}, \
        warningBorderColor = {named}{LightGrey}, \
        cautionBorderColor = {named}{LightGrey}, \
        errorBorderColor = {named}{LightGrey}, \
        attentionBorderColor = {named}{LightGrey}, \
        dangerBorderColor = {named}{LightGrey}, \
        TitleColor = {named}{NavyBlue}, \
        HeaderFamily=\\rmfamily\\bfseries, \
        InnerLinkColor= {named}{NavyBlue}, \
        OuterLinkColor= {named}{NavyBlue}',

    'tableofcontents': ' ',

}

latex_logo = '_static/logo.png'

# sectioning defaults to chapter when using manual

latex_toplevel_sectioning = 'chapter'

latex_documents = [
    (master_doc, 'PC-USING-RTD.tex', 'PC-USING-RTD',
     'GMC', 'report'),
]
