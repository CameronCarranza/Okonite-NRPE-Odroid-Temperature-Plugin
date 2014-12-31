Okonite - NRPE Odroid Temperature Plugin
========================================

NRPE Plugin for Odroid Units run through Nagios(3) for the Odroid Units I use to power our Digital Signage system. The Critical state kills chromium-browser (which is running fullscreen for the digital signage system) to allow a cooldown, rather than allowing a heat shutoff by the odroid itself.

These units are run in an industrial environment without any protection (yet), and as such, it is important to monitor the temperature of the small fans to catch any dust buildup before permanent damage could be caused.

|Temperature Range|Status|
| --------------- |:-------------:|
|40-98ºC          |OK!|
|98-104ºC         |WARNING!|
|104ºC or Greater |CRITICAL! & Chromium Process Shutdown|

Example output through Nagios3.

<img src="http://i.imgur.com/bRnuVHa.png"/>
