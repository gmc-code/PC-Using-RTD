==============================
Python
==============================

Install Python
------------------------------

* Check the version of python installed from the command line.

.. code-block::

    python --version

* Download and install Python from https://www.python.org/downloads/.


----

Create a python Virtual environment
---------------------------------------

| See: https://www.youtube.com/watch?v=APOPm01BVrk
| Rather than installing the python packages in the system wide installation of python, a virtual environment can be created that only has the modules needed for sphinx and read the docs.
| Virtual environments allow easy maintenance of the libraries needed for the project and avoid issues that can happen when multiple dependencies conflict across multiple projects.

| Create a virtual environment for the packages needed for read the docs.
| By default, these will be created in the users directory: ``C:\Users\username\``.
| In examples below, the virtual environment folder will be called: ``rtd_venv310``, but any suitable name can be used.

| Create a virtual environment with the default system python:

.. code-block::

    python -m venv rtd_venv310
    
| If there are different versions of python installed, use the full path to the version required to create the virtual environment.
| <username> used in the paths below will be different for each user.
| e.g. ``C:\Users\username\AppData\Local\Programs\Python\Python310\python.exe``
| Create a virtual environment using a specific installed version of python:

.. code-block::

    "C:\Users\username\AppData\Local\Programs\Python\Python310\python.exe" -m venv rtd_venv310

| Activate the virtual environment:

.. code-block::
    
    "C:\Users\username\rtd_venv310\Scripts\activate.bat"

----

Using the python Virtual environment in VSCode
---------------------------------------------

| VSCode allows the use of different python environments.
| To use the python python Virtual environment in VSCode:

    #. Choose **View: Command Palette**. 
    #. Into the drop down search field, type: **Python : Select Interpreter**
    #. Choose the one listed that refers to the newly created **rtd_venv310**.

----

.. _Python requirements:

Install python packages via requirements.txt
-----------------------------------------------

| Place a file, called ``requirements.txt``, into the virtual environment folder.
| Into the file, place the text below, containing the suggested python modules for working with sphinx.
| There is no need to include the optional modules below unless they are going to be useful.

.. code-block::
    
    # for sphinx to work
    sphinx==5.0.2
    sphinx_rtd_theme==1.0.0
    sphinx-copybutton==0.5.0
    docutils<0.18  # must be between 0.14 and <0.18 for sphinx

    # for vscode
    rstcheck==6.0.0.post1
    esbonio==0.13.0
    
    # optional useful sphinx extensions
    sphinx-design==0.2.0
    sphinx-togglebutton==0.3.1
    
    # optional for interactive jupyter
    jupyter-sphinx==0.4.0
    sphinx-thebe==0.1.2 # requires sphinx==4.5.0


  
| Install requirements using the full path to a requirements.txt file placed in the virtual environment:

.. code-block::
    
    pip install -r "C:\Users\username\rtd_venv310\requirements.txt"

----

Updating python packages in a requirements file
------------------------------------------------------------

| After setting up a project, there may be a need to update the packages required that are listed in the ``requirements.txt`` file.

| From the command line change directory, ``cd`` to the folder with the ``requirements.txt`` file and use:

.. code-block::
    
    cd rtd_venv310
    pip install --upgrade -r requirements.txt

* ``-U`` can be used instead of ``--upgrade``

.. code-block::

    pip install -U -r requirements.txt


* To check the installed version numbers and other info about a package, check the output from typing in the VSCode terminal:

.. code-block::

    pip show sphinx
    pip show sphinx_rtd_theme
    pip show sphinx-copybutton
    pip show docutils

* To get all the installed version numbers, check the output from typing in the VSCode terminal:

.. code-block::

    pip list

* To see if there are updates available, check the output from typing in the VSCode terminal:

.. code-block::

    pip list -o

----

Updating python packages
------------------------------

| This is not recommended, but is here for reference purposes. To update all packages in a Windows environment to the latest version available in the Python Package Index (PyPI), use pip in conjunction with Windows PowerShell.
| Open a command shell by typing ``powershell`` in the Search Box of the Windows Task bar.
| Enter:

.. code-block::
    
    pip freeze | %{$_.split('==')[0]} | %{pip install --upgrade $_}

----

Uninstalling all python packages
----------------------------------

| This is not recommended, but is here for reference purposes. 
| To remove all installed python packages, leaving just the built in modules, from the command line:

.. code-block::

    pip freeze | xargs pip uninstall -y

