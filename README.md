# Intro

I was having a heck of a time trying to get non-standard baud rates to
work on OSX.  In the end I just wrote a little python script, and it's
fine if you just want to read the output from the tty device.  Please
do let me know if you know of any good tools for OSX that handle
arbitrary baud rates!  For some reason, `screen` totally garbles the
output.

# Installation

`:> pip install -r requirements.txt`

# Usage

`:> python serial_reader.py --baud=<baudrate> <device>`
