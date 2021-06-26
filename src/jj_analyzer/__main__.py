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

def analyze(file):
    logger.debug("analyze %s" % (file))

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
