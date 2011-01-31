#!/usr/local/bin/python
# -*- charset:Utf-8 -*-


import os

activate_this = '/Users/Fandekasp/Envs/dream/bin/activate_this.py'
if os.path.exists(activate_this):
    execfile(activate_this, dict(__file__=activate_this))

from appscript import app
import datetime
import logging
import random
import subprocess
from threading import Timer

# constants
LOG_DIR = '/Users/Fandekasp/Documents/Programming/Python/LucidDreamingBox/'

# logging
log_file = os.path.join(LOG_DIR, "dream.log")
logging.basicConfig(filename=log_file, level=logging.DEBUG)
logger = logging.getLogger('wake')


def launch_itunes():
    """Select a track from the iTunes "Best rates" Playlist"""
    iTunes = app("iTunes")
    list_tracks = iTunes.playlists["Best rates"].tracks.get()
    track_to_play = random.choice(list_tracks)
    INTERVAL = 5
    logger.info("iTunes called")
    logger.debug("%s will be played in %d seconds" %
            (track_to_play.name.get(), INTERVAL))
    Timer(INTERVAL, track_to_play.play, ()).start()


def launch_dream_latex():
    """Open vim, fill it with a latex template, then gives focus"""
    cmd = "/usr/local/bin/mvim /Users/Fandekasp/Documents/testdream.tex --cmd"
    logger.info("Vim called")
    logger.debug(cmd.split() + [':se lines=40 columns=80'])
    subprocess.call(cmd.split() + [':se lines=40 columns=80'])


now = datetime.datetime.now()
logger.info("wake script called at %s" % now.strftime("%H:%M:%S"))
if 5 <= now.hour <= 10:
    """If it's the morning"""
    launch_itunes()
    launch_dream_latex()
