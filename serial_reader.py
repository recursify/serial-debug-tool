#!/usr/bin/env python

from argparse import ArgumentParser
import sys
import serial
from datetime import datetime

def run(device, baud, prefix=None):
    with serial.Serial(device, baud, timeout=0.1) as ser:
        while True:
            line = ser.readline()
            if not line:
                continue
            if prefix:
                line = prefix() + line
            sys.stdout.write(line)

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('device',
                        help='serial device, typically /dev/tty.usbserial-*')
    parser.add_argument('--baud', dest='baud', type=int, default=74880)
    parser.add_argument('-t', '--timestamp', dest='timestamp', action='store_true',
                        help="Add timestamp to start of each line")
    args = parser.parse_args()
    prefix = None
    if args.timestamp:
        prefix = lambda: datetime.now().strftime("[%H:%M:%S.%f] ")
    run(args.device, args.baud, prefix)
