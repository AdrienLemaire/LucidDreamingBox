#!/usr/local/bin/python
# -*- charset:Utf-8 -*-


import os

activate_this = '/Users/Fandekasp/Envs/dream/bin/activate_this.py'
if os.path.exists(activate_this):
    execfile(activate_this, dict(__file__=activate_this))

from appscript import app
import random
from threading import Timer


def launch_itunes():
    """Select a track from the iTunes "Best rates" Playlist"""
    iTunes = app("iTunes")
    list_tracks = iTunes.playlists["Best rates"].tracks.get()
    track_to_play = random.choice(list_tracks)
    INTERVAL = 5
    Timer(INTERVAL, track_to_play.play, ()).start()
    print "OK2"

launch_itunes()
