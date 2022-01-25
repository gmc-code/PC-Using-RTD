==============================
Git
==============================

| Git is a Distributed Version Control System (DVCS).
| It can be used to track code history, work on different branches of the code, and sync remote and local versions of the code. 
| Git is a command line tool that can be integrated into other software such as VSCode.
| GitHub hosts repositories and it deeply integrated with Git.
| See: https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control


----

Install Git
------------------------------

Download and install git version 2.34.1 (or newer) from https://git-scm.com/. Use all defaults.

----

Check installed version of Git
---------------------------------

From the terminal in VSCode or from the command prompt, check the version of Git that is installed.

Press :kbd:`Win` + :kbd:`X` + :kbd:`C` to open the Command prompt. 

From the cmd prompt: ::

    git --version

----

Set Git Name & Email
------------------------------

When you install Git, set your user name and email address. 
This is important because every Git commit uses this information, 
and it's used in the commits you create.

Press :kbd:`Win` + :kbd:`X` + :kbd:`C` to open the Command prompt. 

From the cmd prompt: ::

    git config --global user.name "my-github-name"
    git config --global user.email "my-github-email-@address"

From the cmd prompt, check or confirm your settings with: ::

    git config --list

----

Git in VSCode
------------------------------

Visual Studio Code has git support built in.

For use of git in VSCode see: https://code.visualstudio.com/docs/editor/versioncontrol

For an into video for use in VSCode see: https://www.youtube.com/watch?v=wMqukSKYcvU

The main features are:

* See the diff of the file you are editing in the gutter.
* The Git Status Bar (lower left) shows the current branch, dirty indicators, incoming and outgoing commits.
* You can do the most common git operations from within the editor:

    * Initialize a repository.
    * Clone a repository.
    * Create branches and tags.
    * Stage and commit changes.
    * Push/pull/sync with a remote branch.
    * Resolve merge conflicts.
    * View diffs.


----

Git in PyCharm
------------------------------

Git can also be used in other IDEs for python such as PyCharm.

See: https://www.jetbrains.com/help/idea/using-git-integration.html

For use of git in PyCharm see: https://www.youtube.com/watch?v=-_g3QITLaQA



