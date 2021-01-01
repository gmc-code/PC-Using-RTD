Git Commands
=================

Install Git
--------------
Download and install git from https://git-scm.com/. Use all defaults.

Set Git Name & Email
------------------------
When you install Git, set your user name and email address. 
This is important because every Git commit uses this information, 
and it’s used in the commits you create.

Press :kbd:`⊞Win` + :kbd:`X` + :kbd:`C` to open the Command prompt. 

From the cmd prompt: ::

    git config --global user.name "my-github-name"
    git config --global user.email "my-github-email-@address"

From the cmd prompt, confirm your settings with: ::

    git config --list


Git Help
----------
Help formats: ::

    git config --Help
    git help config


Existing project on local machine
----------------------------------
To initialize a repository from existing code, first change the command line directory to the project folder: ::
    
    cd "C:\Users\gmccarthy\microbit for online\PC-using-RTD"

Sometimes you may already be in a subfolder and just need to go up to the parent folder::

    cd ..

To Initialize the repository: ::
    
    git init


Remove the git tracking (delete hidden .git folder)
-----------------------------------------------------------
* Use rmdir /Q/S foldername  or rd /Q/S foldername
* /Q -- Quiet mode, won't prompt for confirmation to delete folders.
* /S -- Run the operation on all folders of the selected path.
* foldername -- The absolute path or relative folder name 
* So from within the repository folder ::

    RD /Q/S .git

 




















Clone remote project to work on
----------------------------------
