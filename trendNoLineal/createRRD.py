#!/usr/bin/env python

import rrdtool

def createNoLineal(nombre):
    ret = rrdtool.create("rrd/"+nombre,
                     "--start",'N',
                     "--step",'60',
                     "DS:inoctets:COUNTER:600:U:U",
                     "RRA:AVERAGE:0.5:1:100",#indexRRA=1
              #RRA:HWPREDICT:rows:alpha:beta:seasonal period[:rra - num]
                     "RRA:HWPREDICT:300:0.1:0.0035:50:3",#indexRRA=2
                     #-->RRA:HWPREDICT:filasArchivo:valorAlpha(0->1):valorBeta:numeroElementosEnDondeSeRepiteLaSerie:index
              #RRA:SEASONAL:seasonal period:gamma:rra-num
                     "RRA:SEASONAL:50:0.1:2",#indexRRA=3
              #RRA:DEVSEASONAL:seasonal period:gamma:rra-num
                     "RRA:DEVSEASONAL:50:0.1:2",#indexRRA=4
              #RRA:DEVPREDICT:rows:rra-num
                     "RRA:DEVPREDICT:300:4",#indexRRA=5
              #RRA:FAILURES:rows:threshold:window length:rra-num
                     "RRA:FAILURES:300:7:9:4")#indexRRA=6

    #HWPREDICT rra-num is the index of the SEASONAL RRA.
    #SEASONAL rra-num is the index of the HWPREDICT RRA.
    #DEVPREDICT rra-num is the index of the DEVSEASONAL RRA.
    #DEVSEASONAL rra-num is the index of the HWPREDICT RRA.
    #FAILURES rra-num is the index of the DEVSEASONAL RRA.