#!/usr/bin/env python

import rrdtool
def createRRDTOOL(nombre,start,step):

    ret = rrdtool.create(nombre,
                        "--start",start,
                        "--step",step,
                        "DS:inoctets:COUNTER:600:U:U",
                        "RRA:AVERAGE:0.5:1:700")

    if ret:
        print (rrdtool.error())