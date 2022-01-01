|

First Post
==========

.. feed-entry::
   :date: 2007-03-16

|

.. image:: /images/look-at-me.jpg
    :align: center
    :class: blog-image

|

I have decided to start a blog. Why? Because Plone allows me to do so. But also:

- I have been reading a lot of |planet_plone| lately and they have inspired me to write my own.
- I want to interact with other Plone users.
- I want to use new technology.

To that end, this post is about my `build tools <http://svn.plone.org/svn/collective/newzope>`_. But first I'll note the current, likely better, alternatives:

- `Buildout <http://www.buildout.org>`_
- `Buildit <https://agendaless.com/software/Members/chrism/software/buildit/>`_
- `Instance Manager <https://old.plone.org/products/instance-manager>`_

I used Buildout for the first time at the `Baarn UI Sprint 2007 <https://old.plone.org/events/sprints/past-sprints/baarn-ui-sprint-2007>`_ and I've also used Chris McDonough's Buildit. There are even more to choose from, but for now I enjoy typing:

::

    newzope test-site ProductA ProductB ProductC

and having a working instance a few seconds later with Product{A,B,C} installed.

|

.. |planet_plone| raw:: html

   <a href="https://planet.plone.org" target="_blank">Plone blogs</a>
