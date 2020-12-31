.. _GitHub new repo:

GitHub new repo
==============================
* Create a fee account at github if you don't already have one.
* Create new repo at github: https://github.com/ or at https://github.com/mygithubname?tab=repositories. 
* Name the new repo the same name as the project folder. See :ref:`VSCode Project Folder and Sphinx`
* e.g. https://github.com/mygithubname/myrepo
* Do not create a readme at this time.
* Copy the "create a new repository on the command line" code for use later::

    echo "# myrepo" >> README.md
    git init
    git add README.md
    git commit -m "first commit"
    git branch -M master
    git remote add origin https://github.com/mygithubname/myrepo.git
    git push -u origin master


README.md


GitHub settings
----------------------
* Set Repository default branch to ``master`` (``main`` is used by some).
* https://github.com/settings/repositories


Initialize GitHub in VSCode
--------------------------------
In VSCode, initialize git locally by following the steps:

Manually, step by step:

* click on the ``source control icon`` on the left sidebar
* click ``initialise git repository`` 
* type in ``"initial commit"`` as the message
* click the ``tick icon`` to commit changes

  
Alternatively, hook up remote branch in the VSCode terminal. Run from within the docs folder.::

    echo "# myrepo" >> README.md
    git init
    git add README.md
    git commit -m "first commit"
    git branch -M master
    git remote add origin https://github.com/mygithubname/myrepo.git
    git push -u origin master

.. note::

    README.rst can be used instead of README.md since GitHub also interprets .rst files.


    
VSCode GitHub updates
----------------------------
* click on the ``source control icon`` on the left sidebar
* type in ``"doc update"`` or specific details as the message in the Source Control section.
* click the ``tick icon`` to commit changes
* The Source Control Repositories section has icons and dropdowns for key commands.
* To push the changes to GitHub, click the icon between the branch icon and tick icon that shows the Push message when hovering over it.

VSCode GitHub controls
--------------------------
* Press :kbd:`ctrl` + :kbd:`⇧shift` + :kbd:`P` to open the Command Palette. 
* Start typing “Git” to see the various commands.


See more: https://docs.microsoft.com/en-us/learn/modules/introduction-to-github-visual-studio-code/

