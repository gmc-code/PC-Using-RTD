==============================
Python
==============================

Install Python
------------------------------

* Check the version of python installed from the command line.

.. code-block::

    python --version

* Download and install Python from https://www.python.org/downloads/.
* Check the checkbox to update the path variable when installing.
* Manually update path if it wasn't automatically done during installation.
* In windows search enter "edit the system environment variables" to edit the environment variables. 
* Edit the path variable to include the path to the installed python version.
* Restart is usually needed to update the system path.
  
----

Create a python Virtual environment
---------------------------------------

| See: https://www.youtube.com/watch?v=APOPm01BVrk
| Rather than installing the python packages in the system wide installation of python, a virtual environment can be created that only has the modules needed for sphinx and read the docs.
| Virtual environments allow easy maintenance of the libraries needed for the project and avoid issues that can happen when multiple dependencies conflict across multiple projects.

| Create a virtual environment for the packages needed for read the docs.
| By default, these will be created in the users directory: ``C:\Users\USERNAME\``.
| In examples below, the virtual environment folder will be called: ``VENVNAME``, but any suitable name can be used.

| Create a virtual environment with the default system python:

.. code-block::

    python -m venv VENVNAME
    
| If there are different versions of python installed, use the full path to the version required to create the virtual environment.
| <USERNAME> used in the paths below will be different for each user.
| e.g. ``C:\Users\USERNAME\AppData\Local\Programs\Python\Python312\python.exe``
| Create a virtual environment using a specific installed version of python:

.. code-block::

    "C:\Users\USERNAME\AppData\Local\Programs\Python\Python312\python.exe" -m venv VENVNAME

| Activate the virtual environment:

.. code-block::
    
    "C:\Users\USERNAME\VENVNAME\Scripts\activate.bat"

----

Using the python Virtual environment in VSCode
---------------------------------------------

| VSCode allows the use of different python environments.
| To use the python python Virtual environment in VSCode:

    #. Choose **View: Command Palette**. 
    #. Into the drop down search field, type: **Python : Select Interpreter**
    #. Choose the one listed that refers to the newly created **VENVNAME**.

----

Update pip
-----------------------------------------------

| To upgrage pip run:

.. code-block::

    python.exe -m pip install --upgrade pip

----

.. _Python requirements:

Install python packages via requirements.txt
-----------------------------------------------

| Place a file, called ``requirements.txt``, into the virtual environment folder.
| Into the file, place the text below, containing the suggested python modules for working with sphinx.
| There is no need to include the optional modules below, other than Sphinx, unless they are going to be useful.

.. code-block::
    
    Sphinx==7.2.6
    sphinx-copybutton==0.5.2
    sphinx-rtd-theme==1.3.0
    sphinx-togglebutton==0.3.2
    sphinx_design==0.5.0

| Alternatively, install each package indiviaually as needed:

.. code-block::
    
    pip install Sphinx==7.2.6
    pip install sphinx-copybutton==0.5.2
    pip install sphinx-rtd-theme==1.3.0
    pip install sphinx-togglebutton==0.3.2
    pip install sphinx_design==0.5.0
    
    
| Install requirements using the full path to a requirements.txt file placed in the virtual environment:

.. code-block::
    
    pip install -r "C:\Users\USERNAME\VENVNAME\requirements.txt"

| If the terminal prompt is already in the path ``"C:\Users\USERNAME\"`` then use this:

.. code-block::

    pip install -r "VENVNAME\requirements.txt"

| If the terminal prompt is already in the path ``"C:\Users\USERNAME\VENVNAME\"`` then use this:

.. code-block::

    pip install -r "requirements.txt"

----

Updating python packages in a requirements file
------------------------------------------------------------

| After setting up a project, there may be a need to update the packages required that are listed in the ``requirements.txt`` file.

| From the command line change directory, ``cd`` to the folder with the ``requirements.txt`` file and use:

.. code-block::
    
    cd VENVNAME
    pip install --upgrade -r requirements.txt

* ``-U`` can be used instead of ``--upgrade``

.. code-block::

    pip install -U -r requirements.txt


* To check the installed version numbers and other info about a package, check the output from typing in the VSCode terminal:

.. code-block::

    pip show sphinx
    pip show sphinx_rtd_theme
    pip show sphinx-copybutton
    pip show sphinx-togglebutton
    pip show sphinx_design
    pip show docutils

    
* To get all the installed version numbers, check the output from typing in the VSCode terminal:

.. code-block::

    pip list

* To see if there are updates available, check the output from typing in the VSCode terminal:

.. code-block::

    pip list -o

----

Save package list to requirements file
------------------------------------------------------------

| After setting up a project, there may be a need to create a new the virtual environment with a new verion of python, but with all the libraries in the the virtual environment 

| A ``requirements.txt`` file can be saved and used to create a new venv:

.. code-block::
    
    pip freeze > requirements.txt

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

----

Update virtual Venvironment python in place
----------------------------------------------------

| To update Python in a virtual environment, you can run this code from a terminal which has the latest version of python installed:

.. code-block::

    python -m venv --upgrade "C:\Users\USERNAME\VENVNAME"

----

Update virtual Venvironment by reinstalling it
----------------------------------------------------

| To update Python in a virtual environment, you can follow these steps:
| Make sure you have a `requirements.txt` file that lists all the packages you need.

1. **Deactivate** the virtual environment if it's currently active. You can do this by typing `deactivate` in your terminal and pressing Enter.
2. **Navigate** ot the directory in the terminal. e.g. `cd C:/Users/USERNAME/` 
3. **Delete** the virtual environment. Be careful with this step as it will remove all the packages installed in the virtual environment. You can do this by typing `Remove-Item -Path VENVNAME -Recurse` in your powershell terminal and pressing Enter. 
4. **Create** a new virtual environment with the updated Python version. You can do this by typing `python -m venv VENVNAME` in your terminal and pressing Enter. 
5. **Activate** the new virtual environment. You can do this by typing `C:\Users\USERNAME\VENVNAME\Scripts\activate.bat` in your terminal and pressing Enter.
6. **Install** the required packages. Place a `requirements.txt` file that lists all the packages you need. You can do this by typing `pip install -r requirements.txt` in your terminal and pressing Enter. 

.. code-block::

    deactivate
    cd C:\Users\USERNAME
    Remove-Item -Path VENVNAME -Recurse
    python -m venv VENVNAME
    C:\Users\USERNAME\VENVNAME\Scripts\activate.bat
    cd C:\Users\USERNAME\VENVNAME
    pip install -r requirements.txt


