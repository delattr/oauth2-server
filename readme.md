# OAuth2 Authorization server

A simple API which creates a user by using email and password only.

### Client

- POST **/api/v1/create/** - Create User

  Required fields: *email, password*



### Authorization

- GET **/accounts/o/token/** - Access token URL

  Login and create a new application to get **client ID** and **client secret**.

### Resource
Requires token authoriztion
- GET **/api/v1/user/** - Returns list all users
- GET **/api/vi/user/*user-email-addresse***/ - Returns user detail

## Deployement
https://polar-beyond-91477.herokuapp.com/

## Requirements
- python 3.6
- django 2.2
- djangorestframework 3.9
- django-oauth-toolkit 1.2




