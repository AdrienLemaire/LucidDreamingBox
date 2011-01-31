#!/usr/local/bin/python
# -*- charset:Utf-8 -*-


import os

activate_this = '/Users/Fandekasp/Envs/dream/bin/activate_this.py'
if os.path.exists(activate_this):
    execfile(activate_this, dict(__file__=activate_this))

import datetime
import logging
import subprocess

# constants
LOG_DIR = '/Users/Fandekasp/Documents/Programming/Python/LucidDreamingBox/'

# logging
log_file = os.path.join(LOG_DIR, "dream.log")
logging.basicConfig(filename=log_file, level=logging.DEBUG)
logger = logging.getLogger('sleep')


def plan_waking(sleep_time, interval):
    """configure a system wake in 5 hours"""
    wake_time = sleep_time + datetime.timedelta(hours=interval)
    #wake_time = sleep_time + datetime.timedelta(seconds=15)
    wake_str = wake_time.strftime("%m/%d/%y %H:%M:%S")
    logger.info("System will wake up on %s" % wake_str)
    cmd = 'pmset schedule wake'.split() + [wake_str]
    logger.debug(subprocess.call(cmd))


sleep_time = datetime.datetime.now()
logger.info("script launched, sleep_time.hour = %d" % sleep_time.hour)
if 23 <= sleep_time.hour or sleep_time.hour <= 2:
    plan_waking(sleep_time, 5)
elif 5 <= sleep_time.hour <= 10:
    plan_waking(sleep_time, 1)
