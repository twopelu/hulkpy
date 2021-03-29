# Hulk

Hulk is a tool written in Python to automate bulk changes in Bitbucket repos.

It helps maintainers to compare repos and apply bulk changes based on a template.

The graphical interface is built using a webview and js and it is cross-platfform.

# Installation

## pipenv

Hulk uses **pipenv** to manage dependencies and isolate environments.

First install pipenv:

`pip install pipenv`

To install dependencies:

`pipenv install`

To enter the environment:

`pipenv shell`

To leave the environment:

`exit()`

# Usage

`python hulk <username> <password>`

----

# Dependencies

Bitbucket lib - https://pypi.org/project/bitbucket-api/

https://bitbucket-api.readthedocs.io/en/latest/index.html

WebView lib - https://pypi.org/project/pywebview/

# References

Bitbucket API - https://developer.atlassian.com/bitbucket/api/2/reference