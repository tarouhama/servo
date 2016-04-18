#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import sys
import sg90

# GPIO 4, 24番を使用 (PWM 0)
horizontal = sg90.sg90( 4, 0 )
vertical = sg90.sg90( 24, 0 )

while True:
    print "Turn left ..."
    vertical.setdirection( 100, 10 )
    time.sleep(0.5)
    print "Turn right ..."
    vertical.setdirection( -100, -10 )
    time.sleep(0.5)
    horizontal.setdirection( 50, 20 )
    time.sleep(0.1)
    horizontal.setdirection( -50, -20 )
    time.sleep(0.1)
