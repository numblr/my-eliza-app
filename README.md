# Template repository for a minimal App

## Applicaton

< FLOW CHART OF THE APP >

## Applicaton structure

Describe repository content (folder structure)

## EMISSOR

The application collects interaction data in EMISSOR format.
There is a single scenario created in *app/py-app/app.py*
for each run of the application.

## Adding components

1. Add the component as *git* submodule:


    git submodule add -b main --name cltl-eliza https://github.com/leolani/cltl-eliza.git cltl-eliza
    git submodule update --init --recursive

1. Add the component to
    - *makefile*: Add the folder name of the component to the *project_dependencies* list
    - *app/makefile*: Add the folder name of the component to the *project_dependencies* list
    - *app/requirements.txt*: Add it with the package name and eventual [optional depencdenies](https://setuptools.pypa.io/en/latest/userguide/dependency_management.html#optional-dependencies) (see the *setup.py* of the component). 

1. Setup and start the component in *app/py-app/app.py*. For convenience follow
   the pattern to create a *Container* and add it to the ApplicationContaienr, see e.g. (see e.g. the [Leolani app](https://github.com/leolani/cltl-leolani-app/blob/main/py-app/app.py)).
1. Add the necessary configuration section(s) in *app/py-app/config/default.config* ((see the documentation of the component or e.g. the [Leolani app](https://github.com/leolani/cltl-leolani-app/blob/main/py-app/config/default.config), *do not include intentions*))
1. In the configuration, connect the input and output of the component to existing components by configuring the desired topic names. 
1. Add required dependencies of the component to *cltl-requirements/requirements.txt* (see the documentation or *setup.py* of the added component).
