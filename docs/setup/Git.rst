==============================
Git
==============================

Install Git
==============================
Download and install git version 2.0.0 (or newer) from https://git-scm.com/. Use all defaults.

Set Git Name & Email
==============================
When you install Git, set your user name and email address. 
This is important because every Git commit uses this information, 
and it’s used in the commits you create.

Press :kbd:`Win` + :kbd:`X` + :kbd:`C` to open the Command prompt. 

From the cmd prompt: ::

    git config --global user.name "my-github-name"
    git config --global user.email "my-github-email-@address"

From the cmd prompt, confirm your settings with: ::

    git config --list


Git in VSCode
==============================

Visual Studio Code has git support built in.

For use of git in VSCode see: https://code.visualstudio.com/docs/editor/versioncontrol

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

* With an extension, you can also handle GitHub Pull Requests: https://marketplace.visualstudio.com/items?itemName=GitHub.vscode-pull-request-github.


