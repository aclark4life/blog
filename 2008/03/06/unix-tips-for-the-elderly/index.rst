|

UNIX Tips for the Elderly
=========================

|

.. feed-entry::
   :date: 2008-03-06

|

.. image:: /images/huh.png
    :align: center

|

.. raw:: html

    <style>
    pre.prompt:before { content: '$ ' }
    </style>

I often want to do something to a bunch of files on the filesystem.

E.g.

.. raw:: html

    <pre class="prompt">
    find Music/ | xargs -J % echo 'Do something to ' %
    </pre>

The problem is that sometimes the filenames have spaces in them which will cause:

.. raw:: html

    <pre class="prompt">
    find Music/ | xargs -J % 'Do something to ' %
    </pre>

::

    xargs: unterminated quote

Useless.

Replace Beginning & End of Line with Quotes
-------------------------------------------

The best fix I've managed to come up with is to replace the beginning and end of the line with quotes to make the shell happy.

E.g.

.. raw:: html

    <pre class="prompt">
    find Music/ | sed -e 's/^/"/' -e 's/$/"/'
    </pre>

::

    "Music//iTunes/iTunes Music/Yael Naïm/Yael Naïm/03 New Soul.m4a"

So now I can do things like:

.. raw:: html

    <pre class="prompt">
    find Music/ | sed 's/^/"/' | sed 's/$/"/' | xargs -J % ls -d %
    </pre>

::

    Music//iTunes/iTunes Music/Yael Naïm/Yael Naïm/03 New Soul.m4a

Or:

.. raw:: html

    <pre class="prompt">
    find Music/ | sed 's/^/"/' | sed 's/$/"/' | xargs -J % file %
    </pre>

::

    Music//iTunes/iTunes Music/Yael Naïm/Yael Naïm/03 New Soul.m4a: ISO Media, MPEG v4 system, iTunes AAC-LC

|
