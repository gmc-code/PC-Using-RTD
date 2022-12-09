==============================
Push VSCode changes to GitHub
==============================

| Use VSCode to make changes in your local docs, then push them to Github. 
| RTD will automatically be updated within a few (up to 15) min of changes in GitHub.


GitHub
--------

| Go to the Settings page for your project
| Click Webhooks and then Add webhook
| For Payload URL, use the URL of the integration on Read the Docs, found on the the project's Integrations Admin dashboard page
| For Content type, both application/json and application/x-www-form-urlencoded work
| Select Just the push event
| Finish by clicking Add webhook

