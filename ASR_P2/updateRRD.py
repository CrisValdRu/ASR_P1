import time
import rrdtool
from getSNMP import consultaSNMP, consultaStrSNMP

total_input_traffic = 0
total_output_traffic = 0

def actualizarRRD (archivo, comunidad, host, oid):
    total_input_traffic = int(consultaSNMP(comunidad,host,oid))
    valor = "N:" + str(total_input_traffic)
    print (valor)
    rrdtool.update("rrd/"+archivo+".rrd", valor)
    rrdtool.dump("rrd/"+archivo+".rrd","xml/"+archivo+".xml")
    #time.sleep(1)
    #if ret:
    #    print (rrdtool.error())
        #time.sleep(300)

def actualizarObjectsRRD (archivo, comunidad, host):
    
    oid="1.3.6.1.4.1.2021.4.6.0"
    total_input_traffic = int(consultaSNMP(comunidad,host,oid))
    oid="1.3.6.1.2.1.25.3.3.1.2.196608"
    total_output_traffic = int(consultaSNMP(comunidad,host,oid))
    
    valor = "N:" + str(total_input_traffic)+ ':' + str(total_output_traffic)
    print (valor)
    rrdtool.update("rrd/"+archivo+".rrd", valor)
    rrdtool.dump("rrd/"+archivo+".rrd","xml/"+archivo+".xml")

def updateRRD (archivo, comunidad, host, oid):
    con = 0
    while con<900:
        total_input_traffic = int(
            consultaSNMP(comunidad,host,oid))

        valor = "N:" + str(total_input_traffic)
        print (valor)
        rrdtool.update("rrd/"+archivo+".rrd", valor)
        rrdtool.dump("rrd/"+archivo+".rrd","xml/"+archivo+".xml")
        time.sleep(1)
        con += 1
        if(con == 899):
            print("Desea seguir monitoreando? Y/N: ")
            res=input()
            if(res=='Y' or res=='y' or res=="Yes"):
                con = 0
            else:
                con = 900

    if ret:
        print (rrdtool.error())
        time.sleep(300)