#!/usr/bin/python

import sys
import getopt


def usage():
    print("Usage:%s [-h|-o|-c] [--help|--output] args....." % sys.argv[0])


if __name__ == "__main__":
    try:
        opts, args = getopt.getopt(sys.argv[1:], "ho:t", ["help", "output=", "test"])

        print("options:",opts)

        print("args:",args)

        for opt, arg in opts:
            if opt in ("-h", "--help"):
                usage()
                sys.exit(1)
            elif opt in ("-t", "--test"):
                print("for test option")
            else:
                print("%s ==> %s" % (opt, arg))
    except getopt.error as err:
        print(str(err))
        usage()
        sys.exit(2)
