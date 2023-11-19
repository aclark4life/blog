|

SELinux: 0, Alex Clark: 1
=========================

|

.. image:: /images/selinux-0-alex-clark-1.jpg
    :align: center
    :class: blog-image

|

Introduction
------------

I don’t like to give up on a technical challenge, particularly when the progress is slow-but-consistent. It’s only when I know I can’t make any discernible progress easily or at all that I can force myself to give up. 

Sound familiar? I wrote about a `similar encounter six years ago <https://blog.aclark.net/2017/06/26/saml-1-alex-clark-0.html>`_!

The task at hand
----------------

Now the task at hand is running Samba on Rocky Linux 9. For years I ran File Sharing on a 2012 Mac Pro running Sierra and recent circumstances led me to replace that server with an HP Envy laptop with 11G RAM. It's a surprisingly good server!

.. image:: /images/server-2023.jpg

It's been a lot of fun building out the services on this laptop running Rocky Linux 9, including:

- Jenkins
- RedHat Cockpit
- Microsoft Remote Desktop 

Having Samba fail mysteriously was not fun, and I should have known better than to go down any rabbit hole without first considering SE Linux, but what can I say? I've been out of the game for a while. Eventually I prevailed and this is the story of that encounter.

Attempts
--------

If you Google or ChatGPT "Samba on Rocky Linux" you'll get steered toward something like:

```
sudo dnf install xrdp
```

Followed by some firewall instructions and if you are lucky, some SE Linux instructions. If you are unlucky you will proceed with:

```
sudo systemctl enable smb
sudo systemctl start smb
```

After which you can delight in `sudo systemctl status smb`:

```
parkwoodstudios➜  ~  ᐅ  sudo systemctl status smb
● smb.service - Samba SMB Daemon
     Loaded: loaded (/usr/lib/systemd/system/smb.service; enabled; preset: disabled)
     Active: active (running) since Sat 2023-11-18 15:04:46 EST; 23h ago
       Docs: man:smbd(8)
             man:samba(7)
             man:smb.conf(5)
   Main PID: 1655 (smbd)
     Status: "smbd: ready to serve connections..."
      Tasks: 4 (limit: 72791)
     Memory: 51.0M
        CPU: 3.761s
     CGroup: /system.slice/smb.service
             ├─1655 /usr/sbin/smbd --foreground --no-process-group
             ├─1880 /usr/sbin/smbd --foreground --no-process-group
             ├─1881 /usr/sbin/smbd --foreground --no-process-group
             └─3992 /usr/sbin/smbd --foreground --no-process-group

Nov 18 15:04:46 parkwoodstudios systemd[1]: Starting Samba SMB Daemon...
Nov 18 15:04:46 parkwoodstudios smbd[1655]: [2023/11/18 15:04:46.273770,  0] ../../source3/smbd/server.c:1741(main)
Nov 18 15:04:46 parkwoodstudios smbd[1655]:   smbd version 4.17.5 started.
Nov 18 15:04:46 parkwoodstudios smbd[1655]:   Copyright Andrew Tridgell and the Samba Team 1992-2022
Nov 18 15:04:46 parkwoodstudios systemd[1]: Started Samba SMB Daemon.
```

Light Bulb
----------

|

Conclusion
----------

|
