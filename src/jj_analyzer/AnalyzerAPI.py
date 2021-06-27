#! /usr/bin/python

import datetime
import logging
import re

import Analyzer

logger = logging.getLogger() 
logger.setLevel(logging.DEBUG)

class AnalyzerAPI(Analyzer):
    
    def __init__(self):
        pass

    def parse(self, dt, pid, tid, level, tag, message):
        print("dt:%s ts:%f" % (dt, float(dt.strftime('%s.%f'))))
        print("pid:%d tid:%d" % (pid, tid))
        print("level:%s tag:%s" % (level, tag))
        print("message:%s" % (message))

        # ExecutorURLConnection$ExecutorURLConnectionRunnable::run API:policy(29)@195164206+
        # ExecutorURLConnection$ExecutorURLConnectionRunnable::run API:policy(29)@195164206-, result:200:20200
        m = re.match('API:([a-zA-Z]+)\([0-9]+\)@[0-9]+\+', message)
        if m:
            print("api+:%s" % m.group(1))

        else:
            m = re.match('API:([a-zA-Z]+)\([0-9]+\)@[0-9]+-', message)
            if m:
                pass

        return True
