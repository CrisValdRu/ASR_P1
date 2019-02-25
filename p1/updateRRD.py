import time
import rrdtool
from getSNMP import consultaSNMP, consultaStrSNMP

total_input_traffic = 0
total_output_traffic = 0

def createUpdate(comunidad, host, oid):
    respuesta = consultaStrSNMP(comunidad, host, oid)
    print(respuesta)
    return 1

def analizarTraficoRed ():
    while 1:
        total_input_traffic = int(
            consultaSNMP('grupo_4cm1','localhost',
                        '1.3.6.1.2.1.2.2.1.10.3'))
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