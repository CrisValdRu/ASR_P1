import sys
import rrdtool
import time
tiempo_actual = int(time.time())
tiempo_final = tiempo_actual - 1550970720
tiempo_inicial = tiempo_final -25920000

def graficarRRD(nombre):
        ret = rrdtool.graph( "png/"+nombre+".png",
                "--start",'1551649830',
                "--end","N",
                "--vertical-label=Bytes/s",
                "DEF:inoctets=rrd/"+nombre+".rrd:inoctets:AVERAGE",
                "AREA:inoctets#00FF00:"+nombre)

def graficarObjectsRRD(nombre):
        ret = rrdtool.graph( "png/"+nombre+".png",
                "--start",'1551762120',
                "--end","N",
                "--vertical-label=Bytes/s",
                "DEF:inTrafic=rrd/"+nombre+".rrd:inTrafic:AVERAGE",
                "DEF:outTrafic=rrd/"+nombre+".rrd:outTrafic:AVERAGE",
                "DEF:inPktsError=rrd/"+nombre+".rrd:inPktsError:AVERAGE",
                "DEF:outPktsError=rrd/"+nombre+".rrd:outPktsError:AVERAGE",
                "DEF:inISMPMsg=rrd/"+nombre+".rrd:inISMPMsg:AVERAGE",
                "LINE1:inTrafic#000022:inTrafic",
                "LINE1:outTrafic#005500:outTrafic",
                "LINE1:inPktsError#FF0022:inPktsError",
                "LINE1:outPktsError#AA0022:outPktsError",
                "LINE1:inISMPMsg#00FF00:inISMPMsg")

def graficar(nombre):
        con = 0
        ret = rrdtool.graph( "png/"+nombre+".png",
                "--start",'1551649830',
                "--end","N",
                "--vertical-label=Bytes/s",
                "DEF:inoctets=rrd/"+nombre+".rrd:inoctets:AVERAGE",
                "AREA:inoctets#00FF00:"+nombre)

        while con<600:
                ret = rrdtool.graph( "png/"+nombre+".png",
                         "--start",'1551649830',
                         "--end","N",
                         "--vertical-label=Bytes/s",
                         "DEF:inoctets=rrd/"+nombre+".rrd:inoctets:AVERAGE",
                         "AREA:inoctets#00FF00:"+nombre)

                time.sleep(5)
                con+=5
                if(con == 595):
                        print("Desea seguir graficando? Y/N: ")
                        res=input()
                        if(res=='Y' or res=='y' or res=="Yes"):
                                con = 0
                        else:
                                con = 600
        