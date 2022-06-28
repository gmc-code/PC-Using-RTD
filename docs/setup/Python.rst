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

Virtual environment
---------------------

| See: https://www.youtube.com/watch?v=APOPm01BVrk
| Create  a virtual environment for the packages needed for read the docs.

| If there are different version of python installed use the full path to the version requried to cereate the virtual environment.
| e.g. "C:\Users\username\AppData\Local\Programs\Python\Python39\python.exe"
| e.g. "C:\Users\username\AppData\Local\Programs\Python\Python310\python.exe"


| Create  a virtual environment.

.. code-block::

    "C:\Users\username\AppData\Local\Programs\Python\Python39\python.exe" -m venv rtd_venv39
    or
    "C:\Users\username\AppData\Local\Programs\Python\Python310\python.exe" -m venv rtd_venv310

| Activate the virtual environment

.. code-block::
    
    "C:\Users\username\rtd_venv39\Scripts\activate.bat"

| Install requirements using the full path to a requirements file placed in the virtual environment

.. code-block::
    
    pip install -r "C:\Users\username\rtd_venv39\requirements.txt"


| Suggested python modules to install in the virtual environment for working with sphinx:

    * sphinx==4.5.0 # current is sphinx==5.0.2
    * sphinx_rtd_theme==1.0.0
    * sphinx-copybutton==0.5.0
    * docutils<0.18  # must be between 0.14 and <0.18 for sphinx
    * notebook==6.4.12
    * jupyter-sphinx==0.4.0
    * sphinx-thebe==0.1.2 # requires sphinx==4.5.0
    * rstcheck
    * esbonio

----

Updating python packages in a requirements file
------------------------------------------------------------

| After setting up a project, there may be a need to update the packages required that are listed in the ``requirements.txt`` file.
| Suggested python modules for working with sphinx:

    * sphinx==5.0.2
    * sphinx_rtd_theme==1.0.0
    * sphinx-copybutton==0.5.0

| From the command line change directory, ``cd`` to the folder with the ``requirements.txt`` file and use:

.. code-block::
    
    cd docs
    pip install --upgrade -r requirements.txt

----

Updating python packages
------------------------------

| This is not recommended, but is here for reference purposes. To update all packages in a Windows environment to the latest version available in the Python Package Index (PyPI), use pip in conjunction with Windows PowerShell.
| Open a command shell by typing ``powershell`` in the Search Box of the Windows Task bar.
| Enter:

.. code-block::
    
    pip freeze | %{$_.split('==')[0]} | %{pip install --upgrade $_}


