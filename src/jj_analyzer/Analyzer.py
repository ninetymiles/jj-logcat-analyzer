#! /usr/bin/python

import datetime
import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

class LogcatParser(object):
    
    def __init__(self):
        pass

    def parse(self, dt, pid, tid, level, tag, message):
        print("dt:%s ts:%f" % (dt, float(dt.strftime('%s.%f'))))
        print("pid:%d tid:%d" % (pid, tid))
        print("level:%s tag:%s" % (level, tag))
        print("message:%s" % (message))
        return True
