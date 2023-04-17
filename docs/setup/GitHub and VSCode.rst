.. _GitHub new repo:

==============================
GitHub and VSCode
==============================

The info below is for the simplest approach where there is only the master branch locally which is being maintained and pushed to the github repository.

For github advice see: https://docs.github.com/en/get-started/importing-your-projects-to-github/importing-source-code-to-github/adding-locally-hosted-code-to-github

----

GitHub account
------------------------------

* Create a fee account at github if you don't already have one.

----

VSCode starting from **creating a new empty repository**
------------------------------------------------------------

* Sign in at github
* Create new repo at github: https://github.com/ or at https://github.com/mygithubname?tab=repositories. 
* Name the new repo the same name as the project folder stored locally on your computer. 
* See :ref:`VSCode Project Folder and Sphinx`
* e.g. https://github.com/mygithubname/myrepo
* Do not create a readme file at this time.
* Do not select a licence at this time.
* Adding a read me or selecting a licence will cause an initial commit and will not show the code to use to create the git on your local amchine.
* Copy the "create a new repository on the command line" code for use later.

.. code-block::

    echo "# myrepo" >> README.md
    git init
    git add README.md
    git commit -m "first commit"
    git branch -M master
    git remote add origin https://github.com/mygithubname/myrepo.git
    git push -u origin master

----

GitHub settings
------------------------------

* Set Repository default branch to ``master`` (``main`` is preferred branch name post 2020).
* https://github.com/settings/repositories

----

Initialize GitHub in VSCode
------------------------------

In VSCode, initialize git locally by following the steps:

Manually, step by step:

* Click on the ``source control icon`` on the left sidebar.
* Click ``initialise git repository``.
* Type in ``"initial commit"`` as the message.
* Click the ``tick icon`` to commit changes.


Alternatively, hook up remote branch in the VSCode terminal. 
Run from within the main VScode folder that the docs folder is within.

.. code-block::

    echo "<# myrepo>" >> README.md
    git init
    git add README.md
    git commit -m "first commit"
    git branch -M master
    git remote add origin https://github.com/mygithubname/myrepo.git
    git push -u origin master

.. note::

    README.rst can be used instead of README.md since GitHub also interprets .rst files.

----

Initialize GitHub in VSCode starting from **an existing repository**
-----------------------------------------------------------------------

In VSCode, run from within the main VScode folder that the docs folder is within.

.. code-block::

    git remote add origin https://github.com/mygithubname/myrepo.git
    git branch -M master
    git push -u origin master

----

VSCode GitHub updates
------------------------------

* Click on the ``source control icon`` on the left sidebar
* Type in ``"doc update"`` or specific details as the message in the Source Control section.
* Click the ``tick icon`` to commit changes
* The Source Control Repositories section has icons and dropdowns for key commands.
* To push the changes to GitHub, click the icon between the branch icon and tick icon that shows the Push message when hovering over it.

----

VSCode GitHub controls
------------------------------

* Press :kbd:`ctrl` + :kbd:`shift` + :kbd:`P` to open the Command Palette. 
* Start typing "Git" to see the various commands.


See more: https://docs.microsoft.com/en-us/learn/modules/introduction-to-github-visual-studio-code/

Recommended youtube: 
https://www.youtube.com/watch?v=3Tn58KQvWtU&list=PLpPVLI0A0OkLBWbcctmGxxF6VHWSQw1hi

https://www.youtube.com/watch?v=ghL-KlAhBnc uses the command palette in VSCode more.

----

VSCode Git staging and commits
------------------------------------------------------------

* Click on the ``source control icon`` on the left sidebar
* Any changes to files or new files will be listed under **Changes**. 
* ``U`` stands for untracked (new files not yet added to staging area). 
* ``M`` stands for modified.
* ``D`` stands for delete (which can result from a name change to a file).
  
----

Changes and Staged Changes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Click a file to see the ``git diff`` visualization in split columns, showing changes since the last commit.
* Click the clipboard icon to open the file in VSCode
* Click the left loop arrow icon to discard changes to the file since the last commit.
* Click the plus icon to add the file to the stage area. It will be listed under **Staged Changes**.

----

Commits
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Type in specific details as the message in the Source Control section.
* Click the ``tick icon`` to commit changes
* If there are no staged files (Only Changes is shown), then all files are staged and committed.
* If there are some files that have been staged (Staged Changes is shown), then only the staged files will be committed.

----

VSCode starting from **Cloning a repository**
------------------------------------------------------------

* For steps involved in starting by cloning a repository see: https://www.youtube.com/watch?v=sz2EM-gkEs0&list=PLpPVLI0A0OkLBWbcctmGxxF6VHWSQw1hi&index=2
* If the repository is not a restructuredtext project with .rst files, ``sphinx-quickstart`` may need to be run once the repo is cloned to the local machine.

