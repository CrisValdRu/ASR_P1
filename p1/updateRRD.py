import time
import rrdtool
from getSNMP import consultaSNMP, consultaStrSNMP

total_input_traffic = 0
total_output_traffic = 0

def createUpdate(comunidad, host, oid, port):
    while 1:
        res=int(consultaStrSNMP(comunidad, host, oid, port))
        respuesta = "N:"+str(res)
        #print('-->'+str(int(respuesta)))
#        flecha='---->'
        print(respuesta)
        rrdtool.update('examen.rrd', 'N:10')
        rrdtool.dump('examen.rrd','examen.xml')

        ret = rrdtool.graph("examen.png",
            "--start", '1551250800',
            "--end", "N",
            "--vertical-label=Bytes/s",
            "DEF:inoctets=examen.rrd:inoctets:AVERAGE",
            "AREA:inoctets#00FF00:In traffic")

        time.sleep(1)
    if ret:
        print (rrdtool.error())
        time.sleep(300)

def analizarTraficoRed ():
    while 1:
        total_input_traffic = int(
            consultaSNMP('variation/virtualtable','10.100.71.200',
                        '1.3.6.1.2.1.2.2.1.12.1'))
        total_output_traffic = int(
            consultaSNMP('grupo_4cm1','localhost',
                        '1.3.6.1.2.1.2.2.1.16.3'))

        valor = "N:" + str(total_input_traffic) + ':' + str(total_output_traffic)
        print (valor)
        rrdtool.update('traficoRED.rrd', valor)
        rrdtool.dump('traficoRED.rrd','traficoRED.xml')
        time.sleep(1)

    if ret:
        print (rrdtool.error())
        time.sleep(300)

def analizarExamen ():
    while 1:
        total_input_traffic = int(
            consultaSNMP('comunidadEquipo4_grupo4cm1','10.100.69.46',
                        '1.3.6.1.2.1.2.2.1.10.3'))

        valor = "N:" + str(total_input_traffic)
        print (valor)
        rrdtool.update('examen.rrd', valor)
        rrdtool.dump('examen.rrd','examen.xml')
        time.sleep(1)

    if ret:
        print (rrdtool.error())
        time.sleep(300)

def analizarExamen (comunidad, host, oid):
    while 1:
        total_input_traffic = int(
            consultaSNMP(comunidad,host,oid))

        valor = "N:" + str(total_input_traffic)
        print (valor)
        rrdtool.update('examen.rrd', valor)
        rrdtool.dump('examen.rrd','examen.xml')
        time.sleep(1)

    if ret:
        print (rrdtool.error())
        time.sleep(300)