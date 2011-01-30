================
LucidDreamingBox
================


Goal
----
::

    Sleep Hacker, I became interested by Lucid Dreaming in the end of 2010. As
    I want to use my computer to its full potential, I'm going to build a smart
    software to manage everything related to Lucid Dreaming
                                                            - Adrien Lemaire

..


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
- Growl_


Installation
------------
::

    $ pip install -r requirements.txt
    $ brew install sip pyqt growlnotify sleepwatcher
    $ export REP=`pwd`
    $ cd ~/Library/LaunchAgents/; ln -s $REP/LaunchAgents/com.apple.RealityCheck.plist .
    $ cd /usr/local/bin/; ln -s $REP/bin/reality_check .
    $ cd ~/Pictures/; ln -s $REP/Pictures/RealityCheck.jpg .
    $ # modify the PYTHONPATH in com.apple.RealityCheck.plist by yours
    $ # modify the PATH_IMAGE in reality_check by your path.
    $ launchctl load ~/Library/LaunchAgents/com.apple.RealityCheck.plist

* I'll create an installer later *


Configuration
-------------
- For the RealityCheck, I think that the best way to remember it during our
  sleep is to hear a sound. It's unfortunately impossible to play a sound with
  growlnotify, but I was able to configure growl to play a sound for
  growlnotify (Apple->System Preferences->Other->Growl).



.. [1] I'll use launchd to manage the startup scripts. Linux users will have to
   adapt it for init.d

.. _`Python 2.6.X`: http://www.python.org/download/releases/2.6/
.. _Growl: http://growl.info/index.php
