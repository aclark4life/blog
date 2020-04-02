Project Makefile Open for Business
==================================

.. feed-entry::
   :date: 2016-11-23

**Makefile for Python Web Development & Related Projects**

A while back I was asked to speak to the Configuration Management Working Group of DC:

.. image:: /images/project-makefile-tweet.png
    :align: center
    :class: blog-image
    :target: https://twitter.com/CMWorkingGrp/status/773228143939293185

From that moment on, it was on: an excuse to finish and talk about the ``Makefile`` I'd been dragging around *formerly since January* and informerly much longer.

Finishing the Makefile
----------------------

I started writing slides on the `impressive slides.com <http://slides.com/aclark/project-makefile>`_ then I realized I had to finished the Makefile to finish the slides. This mostly involved deciding on target names and testing target execution.

Finishing the Slides
--------------------

As I mentioned above, slides.com is *very* nice. I had hoped to be able to build the slides myself with reveal.js, but in lieu of JavaScript skills I settled on using the slides.com editor. Later I exported and converted them to PDF with pandoc, which was not as nice (through no fault of pandoc, I'm sure; I just wish I could get a better PDF copy from the slides.com HTML export.)

Closed for Business
-------------------

For month after month as I continued to tweak, the project-makefile repository README contained the following::

    **DO NOT USE THIS**

    At some point I started using a ``Makefile`` in my Python projects.
    This repository contains that ``Makefile``.

    **shrug**

Open for Business
-----------------

Now it contains this::

    Installation
    ------------

    ::

        curl -O https://raw.githubusercontent.com/aclark4life/project-makefile/master/Makefile


    Usage
    -----

    ::

        make ablog
        make ablog-build
        make ablog-clean
        make ablog-init
        make ablog-install
        make ablog-serve
        make black
        make bo
        make ce
        make commit
        make commit-edit
        make commit-push
        make cp
        make d
        make db-init
        make deploy-default
        make django-app-clean
        make django-app-init
        make django-db-drop
        make django-db-init
        make django-debug
        make django-graph
        make django-init
        make django-install
        make django-loaddata-default
        make django-migrate
        make django-migrations-default
        make django-serve-default
        make django-settings
        make django-shell
        make django-static
        make django-su
        make django-test
        make eb-create
        make eb-deploy
        make eb-init
        make flake
        make freeze
        make git-branches
        make git-commit
        make git-commit-auto-push
        make git-commit-edit
        make git-commit-edit-push
        make git-prune
        make git-push
        make git-push-up
        make graph
        make grunt
        make grunt-file
        make grunt-init
        make grunt-install
        make grunt-serve
        make h
        make help
        make heroku
        make heroku-debug-off
        make heroku-debug-on
        make heroku-django-migrate
        make heroku-init
        make heroku-maint-off
        make heroku-maint-on
        make heroku-push
        make heroku-remote-add
        make heroku-shell
        make heroku-web-off
        make heroku-web-on
        make install
        make lint
        make loaddata
        make make
        make migrate
        make migrations
        make npm-init
        make npm-install
        make npm-run
        make p
        make pack
        make package
        make package-check-manifest
        make package-init
        make package-lint
        make package-pyroma
        make package-readme
        make package-release
        make package-release-test
        make package-test
        make pdf
        make pip-freeze-default
        make pip-install
        make pip-install-test
        make pip-upgrade-default
        make pipenv
        make push
        make python-black
        make python-clean
        make python-flake
        make python-lint
        make python-pipenv
        make python-serve
        make python-virtualenv
        make python-virtualenv-2-7
        make python-virtualenv-3-6
        make python-virtualenv-3-7
        make python-wc
        make python-yapf
        make readme
        make redhat-update
        make release
        make release-test
        make review
        make serve
        make sphinx-build
        make sphinx-init
        make sphinx-install
        make sphinx-serve
        make static
        make su
        make test
        make ubuntu-update
        make usage
        make vagrant
        make vagrant-clean
        make vagrant-down
        make vagrant-init
        make vagrant-up
        make vagrant-update
        make virtualenv
        make virtualenv-2
        make vm
        make webpack-init
        make webpack-install
        make webpack-run


Now I invite everyone to use and contribute!

- https://github.com/aclark4life/project-makefile

|
