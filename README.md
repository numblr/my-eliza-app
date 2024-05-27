# Template repository for a minimal App

## Applicaton

< FLOW CHART OF THE APP >

## Applicaton structure

Describe repository content (folder structure)

## EMISSOR

The application collects interaction data in EMISSOR format.
There is a single scenario created in *app/py-app/app.py*
for each run of the application.

## Build your own application

### Setup the application

1. Clone this repository.


    git clone --recurse-submodules https://github.com/leolani/cltl-template-app.git <YOUR FOLDER NAME>

1. Change the *origin* to your own online *git* repository:


    git remote set-url origin <YOUR REPOSITORY URL>
    git push -u origin main

1. Add custom components and code in *src/* or add them as *git* submodule as described below.

### Adding components

1. Add the component as *git* submodule, e.g *cltl-eliza*:


    git submodule add -b main --name cltl-eliza https://github.com/leolani/cltl-eliza.git cltl-eliza
    git submodule update --init --recursive

1. Add the component to
    - *makefile*: Add the folder name of the component to the *project_dependencies* list, e.g. `cltl-eliza`.
    - *app/makefile*: Add the folder name of the component to the *project_dependencies* list, e.g. `cltl-eliza`.
    - *app/requirements.txt*: Add it with the package name and eventual
      [optional depencdenies](https://setuptools.pypa.io/en/latest/userguide/dependency_management.html#optional-dependencies)
      (see the *setup.py* of the component), e.g. `cltl.eliza[impl,service]`.

1. Setup and start the component in *app/py-app/app.py*. For convenience follow
   the pattern to create a *Container* and add it to the ApplicationContaienr, see e.g. the `ElizaContainer` in
   [Leolani app](https://github.com/leolani/cltl-leolani-app/blob/main/py-app/app.py)).
1. If the service of the component provides REST endpoints via a Flask app, add it in the `main()` function of
   *app/py-app/app.py*.
1. Add the necessary configuration section(s) in *app/py-app/config/default.config* (see the documentation of the
   component or e.g.
   the [Leolani app](https://github.com/leolani/cltl-leolani-app/blob/main/py-app/config/default.config)), e.g.
   the `[cltl.eliza]` section.
1. In the configuration, connect the input and output of the component to existing components by configuring the desired
   topic names, e.g. `cltl.topic.text_in` and `cltl.topic.text_out`.
1. Add required dependencies of the component to *cltl-requirements/requirements.txt* (see the documentation or
   *setup.py* of the added component), e.g. none for Eliza.
