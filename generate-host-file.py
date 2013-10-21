#!/usr/bin/env python
# generate-host-file.py: convert bind configuration into host file format
#
#   Copyright 2013 Sudaraka Wijesinghe <sudaraka.org/contact>
#
#   Creative Commons Attribution 3.0 Unported License.
#

if '__main__' == __name__:
    try:
        conf_file = open('block-list.conf', 'r')

        # start the read loop
        while 1:
            line = conf_file.readline()

            # stop reading on EOF
            if '' == line:
                break

            # skip comments and blank lines
            if '\n' == line or '//' == line[:2]:
                continue

            print line[line.find('"') + 1:line.find('{')].replace('"', '') \
                + '127.0.0.1'

        conf_file.close()
    except:
        pass
