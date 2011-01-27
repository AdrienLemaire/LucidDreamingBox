================
LucidDreamingBox
================


Goal
----
::

    Sleep Hacker, I became interested by Lucid Dreaming in the end of 2010. As
    I want to use my computer to its full potential, I'm going to build a smart
    software to manage everything related to Lucid Dreaming

..

        *- Adrien Lemaire*

In this program, I plan to do:

- Alarm / growl notifications to remember me :

  * cardiac respiration
  * reality check (like watching one’s hand)
  * other stuff to do during the day

- Window to fill one's dream on the morning, format it in LateX format and save
  data for future statistics


What's done yet?
----------------

- startup script to show a growl notification every hours


Prerequisite
------------

- Mac Os X 10.6 [1]_
- `Python 2.6.X`_
- Growl_ (and growlnotify, which is located in the Growl's Extras directory)


Installation
------------
::

    $ pip install -r requirements.txt
    $ #python setup.py install

- Move the file com.apple.RealityCheck.plist to ~/Library/LaunchAgents
- Move the file reality_check to /usr/local/bin
- Move the file RealityCheck.jpg in ~/Pictures

.. [1] I'll use launchd to manage the startup scripts. Linux users will have to
   adapt it for init.d

.. _`Python 2.6.X`: http://www.python.org/download/releases/2.6/
.. _Growl: http://growl.info/index.php
