#!/usr/bin/env python

from argparse import ArgumentParser
import sys
import serial

def run(device, baud):
    with serial.Serial(device, baud, timeout=0.1) as ser:
        while True:
            line = ser.readline()
            if line:
                sys.stdout.write(line)

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('device',
                        help='serial device, typically /dev/tty.usbserial-*')
    parser.add_argument('--baud', dest='baud', type=int, default=74880)
    args = parser.parse_args()
    run(args.device, args.baud)
