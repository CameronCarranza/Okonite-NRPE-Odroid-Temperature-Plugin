#!/usr/bin/python
__name__ = 'Okonite - NRPE Odroid Temperature Plugin'
__author__ = 'Cameron Carranza'
__email__ = 'c.carranza@okonite.com'
__date__ = 'Dec 30, 2014'
__license__ = 'GPL'
import subprocess
import sys
# Open File
monitor_file = "/sys/class/thermal/thermal_zone0/temp"
f = open(monitor_file, 'r')
temp = int(f.read())

# Linux Temperature Conversion (i.e. 56000 -> 56.0 Degrees Celcius)
def linux_temp_convert(x):
    temp_str = str(x)
    if len(temp_str) == 5:
        temp_float = float(temp_str[0:2] + "." + temp_str[2:])
        final = str(temp_float) + " Degress Celcius"
        return final

    elif len(temp_str) == 6:
        temp_float = float(temp_str[0:3] + "." + temp_str[3:])
        final = str(temp_float) + " Degrees Celcius"
        return final

# Check Temperature
if 40000 <= temp <= 98000:
    print "OK - Temp is {}".format(linux_temp_convert(temp))
    sys.exit(0)
elif 98000 < temp <= 104000:
    print "WARNING - Temp is {}".format(linux_temp_convert(temp))
    sys.exit(1)
elif temp > 104000:
    subprocess.Popen("killall chromium-browser", shell=True)
    print "CRITICAL - Temp is {}".format(linux_temp_convert(temp))
    sys.exit(2)
else:
    print "UNKNOWN - Temp is {}".format(temp)
    sys.exit(3)
f.close()