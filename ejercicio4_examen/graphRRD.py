import sys
import rrdtool
import time
tiempo_actual = int(time.time())
tiempo_final = tiempo_actual - 86400
tiempo_inicial = tiempo_final -25920000

while 1:
    ret = rrdtool.graph( "examen.png",
                     "--start",'1550613410',
                     "--end","N",
                     "--vertical-label=Paquetes",
                     "DEF:myexam=examen.rrd:ifInNUcastPkts:AVERAGE",
                     "LINE1:myexam#0000FF:non-unicast-packets\r")

    time.sleep(2)