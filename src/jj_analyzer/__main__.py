#! /usr/bin/python

import getopt
import platform
import sys
import logging

__version__ = '0.1.0'
_options = [
    'help',
    'version',
]
_short_options = 'hV'

logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

def help():
    print("  Usage: %s logcat.txt" % sys.argv[0])

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], _short_options, _options)
    except getopt.GetoptError as e:
        logger.warn("err - %s " % (e))

    if not opts and not args:
        help()
    else:
        conf = {}
        for opt, arg in opts:
            if opt in ('-h', '--help'):
                help()
            elif opt in ('-V', '--version'):
                print("JJ logcat analyzer:")
                print("  version: %s" % __version__)
                print("  platform: %s" % platform.platform())
                print("  python: %s" % sys.version.split('\n')[0])

if __name__ == '__main__':
    main()
