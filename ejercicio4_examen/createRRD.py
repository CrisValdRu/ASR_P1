#!/usr/bin/env python

import rrdtool
ret = rrdtool.create("examen.rrd",
                     "--start",'N',
                     "--step",'60',
                     "DS:ifInNUcastPkts:COUNTER:600:U:U",
                     "RRA:AVERAGE:0.5:1:100")
""""
La letra N permite obtener la hora actual del sistema
y convertirla a formato POSIX
"""
if ret:
    print (rrdtool.error())
