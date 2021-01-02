==============================
Git CLI
==============================

For an introduction to command line use of git in the terminal (CLI) see: https://www.youtube.com/watch?v=HVsySz-h9r4&list=PL-osiE80TeTuRUfjRe54Eea17-YfnOOAx

Below are some git CLI commands that might be useful.
For the book that was the basis of the videos, see: https://git-scm.com/book/en/v2

----

Git Help
----------
Help formats: ::

    git config --Help
    git help config

----

2 scenarios:
--------------------
#. Existing project on local machine
#. Clone remote project to work on

----

1. Initialize the repository on local machine
---------------------------------------------
To initialize a repository from existing code, first change the command line directory to the project folder: ::

    cd "C:\repos\PC-using-RTD"

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

    git reset filename

To remove all files from within a subfolder within the **project** folder from the staging area: ::

    git rm -r --cached foldername


To remove all files within the **project** folder from the staging area: ::

    git reset


Add files to Staging Area
---------------------------------
To add a single file from within the **project** folder to the staging area: ::

    git add filename
 
To add all files within the **project** folder to the staging area: ::

    git add -A

To check the status of the git: ::

    git status

Options for adding files: 
git add -A (or --all) does the whole working tree
git add -A mydir/  does the files in that directory
git add mydir/  does the files in that directory (-A is the default)
git add -u (or --update) does only tracked files in the whole working tree (not ignored or new files)
git add -u mydir/ does only tracked files in that directory (not ignored or new files)
git add . is the same as git add -A mydir/ depending on the working directory



Commit files from Staging Area
---------------------------------
To commit files from staging area: ::

    git commit -m "First commit"

To check commits: ::

    git log
 
To add files to staging area and commit at once: ::

    git commit -a -m "Second commit"


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

----


2. Clone remote project to work on
------------------------------------------
Clone a git repository to a local folder. ::

    git clone <url> <destination>

Use a dot for the destination to use the working directory as the destination. ::

    git clone https://github.com/gmc-code/PC-Using-RTD.git .

Use a foldername within the working directory as the destination. ::

    git clone https://github.com/gmc-code/PC-Using-RTD.git "clonedrepo"

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


View changes made 
------------------------------------------
To show changes to files: ::
    git diff


Commit changes to files
---------------------------------
To commit files from staging area: ::

    git diff
    git status
    git add -A
    git status
    git commit -m "changes made"


Push commit to remote repo
---------------------------------
Pull from remote first to include other users changes then push: ::

    git pull origin master

Pull will list changes in remote repo since last pull from it.
Origin is the name of the remote repo and master is the branch.
Push updates the remote branch: ::

    git push origin master


Create branch for desired feature to work in
-----------------------------------------------------
Create new branch: ::

    git branch mygitcmds

List local branches; the working branch will be listed with an asterisk: ::

    git branch

To change to a local branch to work on it: ::

    git checkout mygitcmds

Push branch to remote repo: ::

    git push -u origin mygitcmds

``-u`` associates local with remote branch of same name so ``git pull`` and ``git push`` can be done in future without the other parameters.

To list all the local and remote branches in the repo: ::
 
    git branch -a


Merge a branch
-----------------------------------------------------
Steps to merge ``mygitcmds`` branch to master branch: ::

    git checkout master
    git pull origin master
    git branch --merged
    git merge mygitcmds
    git push origin master


Delete a branch after merging it
-----------------------------------------------------
Steps to delete ``mygitcmds`` branch: ::

    git branch --merged  
    git branch -d mygitcmds
    git branch -a
    git push origin --delete mygitcmds


---


Make changes that have not yet been pushed
-----------------------------------------------------

Remove file from commit not yet pushed
-----------------------------------------------------
Undo changes in a file ``filename``: ::

    git checkout filename


Change commit message not yet pushed
-----------------------------------------------------
Undo commit message: ::

    git commit --amend -m "New message"


Add a file created since last commit but not yet pushed
-----------------------------------------------------------
Add the file first: ::

     git add filename
     git commit --amend


View details of changed files since last commit: ::

    git log --stat

Move commit from master to feature branch not yet pushed
-----------------------------------------------------------
Use this after accidentally make commit to master branch instead of feature branch. Move commit: ::

    git log

Copy the hash of the master branch's last commit that needs moving.

Switch to feature branch: ::
    
    git checkout <featurebranch> 

Copy the hash of last commit that needs moving. 

Copy commit to feature branch: ::

    git cherry-pick <hash>

Check it. ::

    git log

Then return master branch. ::

    git checkout master
    git log

Soft reset
---------------
Then copy hash of initial commit to use in soft reset.  ::

    git reset --soft <hash>
    git log
    git status

The soft reset kept work in modified files as shown by status.

Default reset
---------------
A mixed (default) reset keeps changes but they are left in working area and are not in staging area. ::

    git reset <hash>
    git log
    git status

Hard reset
---------------
A hard reset returns track files back to state at time of the (hash) commit and leaves out changes from files. ::

    git reset --hard <hash>
    git log
    git status


Untracked files left alone from hard rest can be removed: ::

    git clean -df

``-d`` removed untracked directories; ``-f`` is to force changes

The working directory will then be clean as shown by: ::

    git status


Recover from Hard reset
---------------------------
Get a log of commits in order from last commit: ::

    git reflog

Copy a hash and check out that hash and check it using log: ::

    git checkout <hash>
    git log

Make a branch from this detached HEAD state to save the changes: ::

    git branch <new branch>

View branches to check: ::

    git branch


----


Make changes when changes have been pushed
-----------------------------------------------------
Create new commits to undo changes.

Firstly, copy the hash for the commit to remove: ::

    git log

Use the copied hash below: ::

    git revert <hash>

View the commits: ::

    git log

Use the has for the original commit and the reverted commit to compare them: ::

    git diff <hash_original> <hash_reverted>

----


Git Stash
--------------------

Use this when you want to store changes in a feature branch but not commit them yet. ::

    git stash save "<message about context>"

All the changes will appear to be gone, but are stashed. To get a list of stashes: ::

    git stash list

This lists the stash id, the branch and the message. 
To bring back the changes that were stashed: ::

    git stash apply <stashID>

To return to were you were: ::

    git checkout -- .

To apply the first stash and drop or delete the stash: ::

    git stash pop

To drop a stash that is not needed: ::

    git stash drop <stashID>

To drop all stashes: ::

    git stash clear

Git Stash from master to feature branch
-----------------------------------------------------
Steps to take when accidentally working in master branch. ::

    git stash save "feature in master for newfeaturebranch"
    git status
    git diff
    git checkout <newfeaturebranch>
    git stash pop
    git diff
    git add .
    git commit -m "new feature from master"


----


Remove the git tracking (delete hidden .git folder)
-----------------------------------------------------------
* Use RMDIR /Q/S foldername  or RD /Q/S foldername
* /Q -- Quiet mode, won't prompt for confirmation to delete folders.
* /S -- Run the operation on all folders of the selected path.
* foldername -- The absolute path or relative folder name 
* So from within the repository folder ::

    RD /Q/S .git

