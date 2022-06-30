==============================
Read the docs (RTD)
==============================

Sign up to RTD
------------------------------

* Sign up or login at https://readthedocs.org/

----

Connect to GitHub
------------------------------

Connect to github via settings so that all github projects are listed in RTD:

* Go to https://readthedocs.org/accounts/social/connections/
* Click connect to github

----

Import GitHub project
------------------------------

* Go to https://readthedocs.org/dashboard/
* Click: Import project or choose the project from the list (if previously imported)
* Click refresh to show all GitHub repositories
* Click on a plus sign for a repo
* Name and URL are automatic
* Advanced: enter "master" as branch for latest.
* Click Build to build it in RTD.

----

Integrations - GitHub Webhooks 
------------------------------

| Read the Docs provides integrations, mainly using webhooks. Integrations are configured GitHub, and with each change to your repository, Read the Docs is notified and a build is triggered.
| See: https://docs.readthedocs.io/en/stable/webhooks.html
  
* Go to https://readthedocs.org/dashboard/
* Click the project in the list (previously imported)
* Click Admin to show the settings
* Click Integrations.
* Click Add integration.
* Choose GitHub incoming webhook.
  
----

RTD Advanced Settings
------------------------------

* Go to https://readthedocs.org/dashboard/
* Click on Admin
* Click on Advanced Settings
* Scroll to the bottom to check or uncheck **Enable PDF build** 
* These settings should be set in the .yaml config file.

----

RTD Documentation
------------------------------

* For detailed RTD info go to https://docs.readthedocs.io/en/stable/

