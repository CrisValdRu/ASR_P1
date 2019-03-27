from createRRD import createNoLineal
from graphRRD import graficarNoLineal1
from updateRRD import actualizarNoLineal
import time
import sys
import rrdtool
from mail import SendMail

repetir = True
while repetir:
    print('------------No Lineal------------'
        '\nSelecciona un valor:\n'
        '1) Crear Archivo RRD\n'
        '2) Actualizar Archivo RRD\n'
        '3) Graficar\n'
        '4) Prediccion Minimos cuadrados\n')

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
        #print('Ingresa un Object ID: ej 1.3.6.1.2.1.2.2.1.10.3')
        #oid=input()
        actualizarNoLineal(archivo, comunidad, host)
    elif (opcion==3):
        print('\nIngresa el nombre del archivo rrd: ')
        archivo=input()
        graficarNoLineal1(archivo)
    elif (opcion==4):
        #print('\nIngresa el nombre del archivo rrd: ')
        #archivo=input()
        #print('Ingresa una comunidad: ')
        #comunidad=input()
        #print('Ingresa un host: ')
        #host=input()
        

        archivo="source3"
        comunidad="grupo_4cm1"
        host="localhost"
        #archivo="examen2"
        #comunidad="variation/linux-full-walk"
        #host="10.100.71.200"
        rrdtool.dump("rrd/"+archivo+".rrd","xml/"+archivo+".xml")
        con=0
        flag=0
        canSend=False
        graficarMinimosCuadrados(archivo)
        
    elif (opcion==5):
        print('\nIngresa el nombre del archivo rrd: ')
        #archivo=input()
        #print('Ingresa una comunidad: ')
        #comunidad=input()
        #print('Ingresa un host: ')
        #host=input()

        archivo="examen2test"
        comunidad="grupo_4cm1"
        host="localhost"
        createRRDTOOL(archivo+".rrd",'N','10')
        #objectsCreateRRDTOOL(archivo+".rrd",'N','10')

        print('Ingresa un Object ID: (1.3.6.1.2.1.2.2.1.10.3)')
        oid=input()
        con=0
        flag=0
        canSend=False

        while (con < 600):
            actualizarObjectsRRD(archivo,comunidad,host,oid)
            if(con%2==0):
                ultimo_valor = graficarObjectsRRD(archivo)
                if (flag==0):
                    if (ultimo_valor[0]>ultimo_valor[1]):
                            canSend=False
                            flag=1
                elif (flag==1):
                        if (ultimo_valor[0]>ultimo_valor[2]):
                                canSend=False
                                flag=2
                        elif (ultimo_valor[0]<ultimo_valor[1]):
                                flag=0
                elif (flag==2):
                        if(ultimo_valor[0]>ultimo_valor[3]):
                                canSend=True
                                flag=3
                        elif(ultimo_valor[0]<ultimo_valor[2]):
                                flag=1
                elif (flag==3):
                        if(ultimo_valor[0]<ultimo_valor[3]):
                                flag=2
                
                if(canSend):
                        print("Va a sobrepasar el umbral")
                        canSend=False
                        SendMail('./png/examen2.png')
                        #sendMailTo("crisvaldru07@outlook.com","Uso del CPU va a sobrepasar el umbral")
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