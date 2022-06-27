==============================
Python
==============================

Install Python
------------------------------

* Check the version of python installed from the command line::

    python --version

* Download and install Python from https://www.python.org/downloads/.


----

Virtual environment
---------------------

| See: https://www.youtube.com/watch?v=APOPm01BVrk
| Create  a virtual environment for the packages needed for read the docs.

| If there are different version of python installed use the full path to the version requried to cereate teh virtual environment.
| e.g. "C:\Users\username\AppData\Local\Programs\Python\Python39\python.exe"
| e.g. "C:\Users\username\AppData\Local\Programs\Python\Python310\python.exe"


| Create  a virtual environment::

    "C:\Users\username\AppData\Local\Programs\Python\Python39\python.exe" -m venv rtd_venv39

| Activate the virtual environment::
    
       "C:\Users\username\rtd_venv39\Scripts\activate.bat"


----

Updating python packages in requirements file
------------------------------------------------------------

* After setting up a project, there may be a need to update the packages required that are listed in the ``requirements.txt`` file. 
* From the command line change directory, ``cd`` to the folder with the ``requirements.txt`` file and use::

    cd docs
    pip install --upgrade -r requirements.txt

----

Updating python packages
------------------------------

This is not recommended, but is here for reference purposes. To update all packages in a Windows environment to the latest version available in the Python Package Index (PyPI), use pip in conjunction with Windows PowerShell: Open a command shell by typing ‘powershell’ in the Search Box of the Windows Task bar.
Enter::

    pip freeze | %{$_.split('==')[0]} | %{pip install --upgrade $_}

    
