import sys
import rrdtool
import time

def graficarNoLineal1(archivo):
        title="Deteccion de comportamiento anomalo"
        fname="rrd/"+archivo+".rrd"
        endDate = rrdtool.last(fname) #ultimo valor del XML
        begDate = endDate - 40000
        DatosAyer=begDate - 86400
        FinAyer=endDate - 86400
        scale = 8
        rrdtool.tune(fname, '--alpha', '0.9')
        rrdtool.tune(fname, '--beta', '0.0035')
        rrdtool.tune(fname, '--gamma', '0.1')
        ret = rrdtool.graph("png/predAC.png",
                                '--start', str(begDate), '--end', str(endDate), '--title=' + title,
                                "--vertical-label=Bytes/s",
                                '--slope-mode',
                                "DEF:obs=" + fname + ":inoctets:AVERAGE",
                                "DEF:obsAyer=" + fname + ":inoctets:AVERAGE:start="+str(DatosAyer)+":end="+str(FinAyer),
                                "DEF:pred=" + fname + ":inoctets:HWPREDICT",
                                "DEF:dev=" + fname + ":inoctets:DEVPREDICT",
                                "DEF:fail=" + fname + ":inoctets:FAILURES",
                                'SHIFT:obsAyer:86400',
                        #"RRA:DEVSEASONAL:1d:0.1:2",
                        #"RRA:DEVPREDICT:5d:5",
                        #"RRA:FAILURES:1d:7:9:5""
                                "CDEF:scaledobs=obs,"+str(scale)+",*",
                                "CDEF:scaledobsAyer=obsAyer,"+str(scale)+",*",
                                "CDEF:upper=pred,dev,2,*,+",
                                "CDEF:lower=pred,dev,2,*,-",
                                "CDEF:scaledupper=upper,"+str(scale)+",*",
                                "CDEF:scaledlower=lower,"+str(scale)+",*",
                                "CDEF:scaledpred=pred,"+str(scale)+",*",
                        "TICK:fail#FDD017:1.0: Fallas",
                        "AREA:scaledobsAyer#9C9C9C:Ayer",
                        "LINE3:scaledobs#00FF00:In traffic",
                        "LINE1:scaledpred#FF00FF:Prediccion",
                        #"LINE1:outoctets#0000FF:Out traffic",
                        "LINE1:scaledupper#ff0000:Upper Bound Average bits in",
        "LINE1:scaledlower#0000FF:Lower Bound Average bits in")

def graficarNoLineal(archivo,alfa):
        title="Deteccion de comportamiento anomalo, valor de Alpha "+str(alfa)
        rrdname="rrd/"+archivo+".rrd"
        endDate = rrdtool.last(rrdname) #ultimo valor del XML
        begDate = endDate - 86000

        rrdtool.tune(rrdname, '--alpha', str(alfa))
        ret = rrdtool.graph("png/netPalphaBajoFallas.png",
                                '--start', str(begDate), '--end', str(endDate), '--title=' + title,
                                "--vertical-label=Bytes/s",
                                '--slope-mode',
                                "DEF:obs=" + rrdname + ":inoctets:AVERAGE",
                                "DEF:outoctets=" + rrdname + ":outoctets:AVERAGE",
                                "DEF:pred=" + rrdname + ":inoctets:HWPREDICT",
                                "DEF:dev=" + rrdname + ":inoctets:DEVPREDICT",
                                "DEF:fail=" + rrdname + ":inoctets:FAILURES",

                        #"RRA:DEVSEASONAL:1d:0.1:2",
                        #"RRA:DEVPREDICT:5d:5",
                        #"RRA:FAILURES:1d:7:9:5""
                                "CDEF:scaledobs=obs,8,*",
                                "CDEF:upper=pred,dev,2,*,+",
                                "CDEF:lower=pred,dev,2,*,-",
                                "CDEF:scaledupper=upper,8,*",
                                "CDEF:scaledlower=lower,8,*",
                                "CDEF:scaledpred=pred,8,*",
                        "TICK:fail#FDD017:1.0:Fallas",
                        "LINE3:scaledobs#00FF00:In traffic",
                        "LINE1:scaledpred#FF00FF:Prediccion\\n",
                        #"LINE1:outoctets#0000FF:Out traffic",
                        "LINE1:scaledupper#ff0000:Upper Bound Average bits in\\n",
                        "LINE1:scaledlower#0000FF:Lower Bound Average bits in")