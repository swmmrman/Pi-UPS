
# Raspberry PI UPS EP-0118 Monitor

This is a basic monitor built around the 52Pi UPS Module for RaspberryPi.  Currently this has only been tested on a RaspberryPi4 8GB, running Manjaro Linux.  This will cover setting up the RTC and Coulometer.\
As most guides do not cover getting i2c enabled, those steps will be included here as well.  You may not need these steps in other operating systems.

## Requirements
* A 52Pi EP-0118
* A RaspberryPi 4
* Python3
* pi-ina219 python module
* 18650 battery or batteries
* Capacity of batteries

## Setup
* Follow the assembly instructions included with with UPS module.  However, I personally recommend installing the batteries after the module is attached to the pi. Use your own judgement here.
* Charge the batteries to full.
* Enable the RTC and ds1307 overlays in the /boot/config.txt
* Add dtparam=i2c_arm=on if not present.
* Disable fake-hwclock as needed.  'sudo pacman -R fake-hwclock', or 'sudo apt remove fake-hwclock'
* For Debian based, 'sudo update-rc.d -f fake-hwclock remove'
* Add 'i2c-dev' to the end of /etc/modules-load.d/raspberrypi.conf
* Optional install i2c-tools

At this point reboot your RaspberryPi.  If all goes well /dev/rtc0 and /dev/12c-1 should be present.

* check if i2c group is present 'grep i2c /etc/group'
* check ownership of /dev/i2c
```console
crw-rw---- 1 root i2c 89, 1 Jan  1 01:01 /dev/i2c-1 
```

If all checks out.  Run from a terminal with 
```bash
python main.py
```

Example output
```console
Watts:          3.1786w
Voltage:        5.1440v
Current:        0.6179a
WH:             0.0085wh
Energy:         0.0017ah
Time:           00:00:9.2
```

* install pi-ina219 'sudo pip install pi-ina219'

