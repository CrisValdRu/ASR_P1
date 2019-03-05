from createRRD import createRRDTOOL, objectsCreateRRDTOOL
from graphRRD import graficar, graficarRRD, graficarObjectsRRD
from updateRRD import updateRRD, actualizarRRD, actualizarObjectsRRD
import time
import sys

repetir = True
while repetir:
    print('------------P1 ASR------------'
        '\nSelecciona un valor:\n'
        '1) Crear Archivo RRD\n'
        '2) Actualizar Archivo RRD\n'
        '3) Graficar\n'
        '4) Actualizar y Graficar\n'
        '5) Actualizar y Graficar 5 objetos MIB')

    opcion=int(input())

    if(opcion==1):
        print('Ingresa un nombre para el archivo: ')
        nombre=input()
        createRRDTOOL(nombre+".rrd",'N','10')
    elif(opcion==2):
        print('\nIngresa el nombre del archivo rrd: ')
        archivo=input()
        print('Ingresa una comunidad: ')
        comunidad=input()
        print('Ingresa un host: ')
        host=input()
        print('Ingresa un Object ID: ej 1.3.6.1.2.1.2.2.1.10.3')
        oid=input()
        updateRRD(archivo,comunidad,host,oid)
    elif (opcion==3):
        print('\nIngresa el nombre del archivo rrd: ')
        archivo=input()
        graficar(archivo)
    elif (opcion==4):
        print('\nIngresa el nombre del archivo rrd: ')
        archivo=input()
        print('Ingresa una comunidad: ')
        comunidad=input()
        print('Ingresa un host: ')
        host=input()
        print('Ingresa un Object ID: (1.3.6.1.2.1.2.2.1.10.3)')
        oid=input()
        con=0
        while (con < 600):
            actualizarRRD(archivo,comunidad,host,oid)
            if(con%5==0):
                graficarRRD(archivo)
            time.sleep(1)
            con+=1
            if(con == 599):
                print("Desea seguir monitoreando? Y/N: ")
                res=input()
                if(res=='Y' or res=='y' or res=="Yes"):
                    con = 0
                else:
                    con = 600
    elif (opcion==5):
        print('\nIngresa el nombre del archivo rrd: ')
        archivo=input()
        print('Ingresa una comunidad: ')
        comunidad=input()
        print('Ingresa un host: ')
        host=input()

        objectsCreateRRDTOOL(archivo+".rrd",'N','10')

        #print('Ingresa un Object ID: (1.3.6.1.2.1.2.2.1.10.3)')
        #oid=input()
        con=0
        while (con < 600):
            actualizarObjectsRRD(archivo,comunidad,host)
            if(con%5==0):
                graficarObjectsRRD(archivo)
            time.sleep(1)
            con+=1
            if(con == 599):
                print("Desea seguir monitoreando? Y/N: ")
                res=input()
                if(res=='Y' or res=='y' or res=="Yes"):
                    con = 0
                else:
                    con = 600
    else:
        createRRDTOOL("examen.rrd",'1551252880','10')
        createUpdate('grupo_4cm1', 'localhost', '1.3.6.1.2.1.2.2.1.3.1', '161')

    print("Desea hacer otra operacion? Y/N: ")
    res=input()
    if(res=='Y' or res=='y' or res=="Yes"):
        repetir=True
    else:
        repetir=False