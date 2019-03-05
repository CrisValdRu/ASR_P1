#!/usr/bin/env python

import rrdtool
def createRRDTOOL(nombre,start,step):
    ret = rrdtool.create("rrd/"+nombre,
                        "--start",start,
                        "--step",step,
                        "DS:inoctets:COUNTER:600:U:U",
                        "RRA:AVERAGE:0.5:1:700")

    if ret:
        print (rrdtool.error())

def objectsCreateRRDTOOL(nombre,start,step):
    ret = rrdtool.create("rrd/"+nombre,
                        "--start",start,
                        "--step",step,
                        "DS:inTrafic:COUNTER:600:U:U",
                        "DS:outTrafic:COUNTER:600:U:U",
                        "DS:inPktsError:COUNTER:600:U:U",
                        "DS:outPktsError:COUNTER:600:U:U",
                        "DS:inISMPMsg:COUNTER:600:U:U",
                        "RRA:AVERAGE:0.5:1:700",
                        "RRA:AVERAGE:0.5:1:700",
                        "RRA:AVERAGE:0.5:1:700",
                        "RRA:AVERAGE:0.5:1:700",
                        "RRA:AVERAGE:0.5:1:700")

    if ret:
        print (rrdtool.error())