#! /usr/bin/python

import datetime
import getopt
import platform
import re
import sys
import logging

__version__ = '0.1.0'
_options = [
    'help',
    'version',
]
_short_options = 'hv'

logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

def print_help():
    print("  Usage: %s [OPTION] logcat.txt" % sys.argv[0])
    sys.exit()

def print_version():
    print("  JJ logcat analyzer:")
    print("    version: %s" % __version__)
    print("    platform: %s" % platform.platform())
    print("    python: %s" % sys.version.split('\n')[0])
    sys.exit()

def parse_logcat(line):
    print(line)
    m = re.match('([0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}.[0-9]{3}) ([0-9]+)-([0-9]+) ([A-Z])/([a-zA-Z-]+):', line)
    if m:
        date_time = m.group(1)
        pid = int(m.group(2))
        tid = int(m.group(3))
        level = m.group(4)
        tag = m.group(5)
        print("date_time:%s" % (date_time))
        
        dt = datetime.datetime.strptime(date_time, '%Y-%m-%d %H:%M:%S.%f')
        print("dt:%s ts:%f" % (dt, float(dt.strftime('%s.%f'))))
        # print("dt:%s ts:%f" % (dt, dt.timestamp))
        
        print("pid:%d tid:%d" % (pid, tid))
        print("level:%s tag:%s" % (level, tag))
    else:
        # TODO: append to previous line
        pass

def analyze(filepath):
    logger.debug("analyze %s" % (filepath))
    with open(filepath, 'r') as f:
        # print(f.read())
        while True:
            l = f.readline()
            if not l:
                break
            parse_logcat(l)

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], _short_options, _options)
    except getopt.GetoptError as e:
        logger.warn("err - %s " % (e))

    if not opts and not args:
        print_help()
    else:
        for opt, arg in opts:
            if opt in ('-h', '--help'):
                print_help()
            elif opt in ('-v', '--version'):
                print_version()
        analyze(args[0])

if __name__ == '__main__':
    main()
