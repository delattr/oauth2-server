# OAuth2 Authorization server

A simple API which creates a user by using email and password only.


## Authorization

Login first and create a new application to get **client ID** and **client secret**.

A callback  is required for **Authorization Grant Type** : *authorization-code*

(e.g: https://<span></span>getpostman.com/oauth2/callback/)

#### URLs

Access token URL: http://<span></span>host.com/o/token/

Authorization URL: http://<span></span>host.com/o/authorize/


## Resource
Requires token authoriztion

API endpoints:
- GET **/api/v1/user/** - Returns list all users.
- GET **/api/vi/user/*user-email-addresse***/ - Returns user details.
- POST **/api/v1/create/** - Create User. *email* and *password* fields are required.

## Deployement
https://polar-beyond-91477.herokuapp.com/

## Requirements
- python 3.6
- django 2.2
- djangorestframework 3.9
- django-oauth-toolkit 1.2
- django-cors-middleware 1.4



