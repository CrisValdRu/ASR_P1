import time
import rrdtool
from getSNMP import consultaSNMP
ifInNUcastPkts = 0

while 1:
    ifInNUcastPkts = int(
        consultaSNMP('variation/virtualtable','10.100.71.230',
                     '1.3.6.1.2.1.2.2.1.12.1'))

    valor = "N:" + str(ifInNUcastPkts)
    print (valor)
    rrdtool.update('examen.rrd', valor)
    rrdtool.dump('examen.rrd','examen.xml')
    time.sleep(1)

if ret:
    print (rrdtool.error())
    time.sleep(300)