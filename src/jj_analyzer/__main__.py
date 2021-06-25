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
_help = """Usage: {} [OPTION]... [URL]...
"""

logger = logging.getLogger("jj")
logger.setLevel(logging.DEBUG)

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], _short_options, _options)
    except getopt.GetoptError as e:
        logger.warn("err - %s " % (e))

    if not opts and not args:
        print(_help)
    else:
        conf = {}
        for opt, arg in opts:
            if opt in ('-h', '--help'):
                print(_help)
            elif opt in ('-V', '--version'):
                logger.info("jj:")
                logger.info("    version: %s", __version__)
                logger.info("    platform: %s", platform.platform())
                logger.info("    python: %s", sys.version.split('\n')[0])

if __name__ == '__main__':
    main()
