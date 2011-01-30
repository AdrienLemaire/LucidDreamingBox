#!/usr/local/bin/python
# -*- charset:Utf-8 -*-


import os

activate_this = '/Users/Fandekasp/Envs/dream/bin/activate_this.py'
if os.path.exists(activate_this):
    execfile(activate_this, dict(__file__=activate_this))


import datetime
import subprocess


def plan_waking():
    """configure a system wake in 5 hours"""
    sleep_time = datetime.datetime.now()
    #wake_time = sleep_time + datetime.timedelta(hours=5)
    wake_time = sleep_time + datetime.timedelta(seconds=15)
    wake_str = wake_time.strftime("%m/%d/%y %H:%M:%S")
    cmd = 'pmset schedule wake'.split() + [wake_str]
    print cmd
    subprocess.call(cmd)
    print "OK"


plan_waking()
