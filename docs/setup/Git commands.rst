Git Commands
=================
See: https://www.youtube.com/watch?v=HVsySz-h9r4&list=PL-osiE80TeTuRUfjRe54Eea17-YfnOOAx


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


2 scenarios:
--------------------
#. Existing project on local machine
#. Clone remote project to work on


1. Initialize the repository on local machine
---------------------------------------------
To initialize a repository from existing code, first change the command line directory to the project folder: ::
    
    cd "C:\Users\gmccarthy\microbit for online\PC-using-RTD"

Sometimes you may already be in a subfolder and just need to go up to the parent folder::

    cd ..

To Initialize the repository: ::
    
    git init

To check the status of the git: ::

    git status

Ignore files
---------------
Add the ``.gitignore`` file from within the **project** folder. ::

    type nul > .gitignore

Edit the ``.gitignore`` file to list on each line any files of folders to be ignored by git.


Add files to Staging Area
---------------------------------
To add a single file from within the **project** folder to the staging area: ::

    git add filename
    
To add all files within the **project** folder to the staging area: ::

    git add -A

To check the status of the git: ::

    git status


Remove files from Staging Area
---------------------------------
To remove a single file from within the **project** folder from the staging area: ::

    git rm --cached filename

    or

    git reset filename

To remove all files from within a subfolder within the **project** folder from the staging area: ::

    git rm -r --cached foldername
    

To remove all files within the **project** folder from the staging area: ::

    git reset


Commit files from Staging Area
---------------------------------
To commit files from staging area: ::

    git commit -m "First commit"

To check commits: ::

    git log
       
To add files to staging area and commit at once: ::

    git commit -a -m "Second commit"




2. Clone remote project to work on
------------------------------------------
Clone a git repository to a local folder. ::

    git clone <url> <destination>
    
Use a dot for the destination to use the working directory as the destination. ::

    git clone https://github.com/gmc-code/PC-Using-RTD.git .

Use a foldername within the working directory as the destination. ::

    git clone https://github.com/gmc-code/PC-Using-RTD.git "clonedrepo"


View information about remote repository
------------------------------------------
To list info about the repository: ::
    git remote -v

To list all the local and remote branches in the repo: ::
    
    git branch -a


View information changes made 
------------------------------------------
To list info about the repository: ::
    git diff


Commit changes to files
---------------------------------
To commit files from staging area: ::

    git diff
    git add -A
    git status
    git commit -m "changes made"


Push commit to remote repo
---------------------------------
Pull from remote first to include other users changes then push: ::

    git pull origin master
    git push origin master










Remove the git tracking (delete hidden .git folder)
-----------------------------------------------------------
* Use RMDIR /Q/S foldername  or RD /Q/S foldername
* /Q -- Quiet mode, won't prompt for confirmation to delete folders.
* /S -- Run the operation on all folders of the selected path.
* foldername -- The absolute path or relative folder name 
* So from within the repository folder ::

    RD /Q/S .git
