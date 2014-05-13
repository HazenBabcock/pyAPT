#!/usr/bin/env python
"""
Usage: python tdc001_serial.py [<serial_port>]

Gets the info and position of a TDC001 controller connected to
serial port serial_port (eg. "COM11").
"""

import sys
import time

import pyAPT

# Check for user specified serial port, default to COM11.
serial_port = "COM11"
if (len(sys.argv) == 3):
  serial_port = sys.argv[2]

# Get info.
con = pyAPT.TDC001(serial_port)
info = con.info()
print '\tController info:'
labels=['S/N','Model','Type','Firmware Ver', 'Notes', 'H/W Ver',
        'Mod State', 'Channels']

for idx, ainfo in enumerate(info):
  print '\t%12s: %s'%(labels[idx], bytes(ainfo))

# Get current position.
print '\nPosition:'
print str(con.position()) + " raw = " + str(con.position(raw=True))
print ''
