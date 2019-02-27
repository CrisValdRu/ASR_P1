import sys
import rrdtool
import time
tiempo_actual = int(time.time())
tiempo_final = tiempo_actual - 1550970720
tiempo_inicial = tiempo_final -25920000
def graficar():
    while 1:
        ret = rrdtool.graph( "Equipo4_traficoDeRed.png",
                         "--start",'1551289060',
                         "--end","N",
                         "--vertical-label=Bytes/s",
                         "DEF:inoctets=examen.rrd:inoctets:AVERAGE",
                         "AREA:inoctets#00FF00:In traffic")

        time.sleep(10)