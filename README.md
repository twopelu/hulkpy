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

# TO-DO

- Write setup.py (https://docs.python.org/3/distutils/introduction.html)
- Write unit tests (https://docs.python.org/3/library/unittest.html)

----

# Dependencies

Bitbucket lib - https://pypi.org/project/bitbucket-api/

https://bitbucket-api.readthedocs.io/en/latest/index.html

WebView lib - https://pypi.org/project/pywebview/

# References

Bitbucket API - https://developer.atlassian.com/bitbucket/api/2/reference
