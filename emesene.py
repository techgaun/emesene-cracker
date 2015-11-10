#!/usr/bin/python

import os
import pwd
import binascii


def coder():
    print """
        Coded By Samar Dhwoj Acharya, 2011
        http://www.techgaun.com
        Tested with emesene1.0

    """


def getpass():
    user = pwd.getpwuid(os.getuid()).pw_name
    emesene_file = "/home/%s/.config/emesene1.0/users.dat" % (user)
    if os.path.exists(emesene_file) is True:
        fp = open(emesene_file, "r")
        for line in fp.readlines():
            line_list = line.split(":")
            line_list[1] = binascii.unhexlify(line_list[1])
            print "%s : %s" % (line_list[0], line_list[1])
        fp.close()
    else:
        print "Could not locate the users.dat file."
coder()
getpass()
