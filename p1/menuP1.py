from createRRD import createRRDTOOL
from graphRRD import graficar
from updateRRD import createUpdate, analizarTraficoRed, analizarExamen

print('------------P1 ASR------------'
      '\nSelecciona un valor:\n'
      '1) CreateRRD\n'
      '2) UpdateRRD\n'
      '3) todo')

opcion=int(input())

if(opcion==1):
   createRRDTOOL("examen.rrd",'N','10')
elif(opcion==2):
    print('\nIngresa una comunidad: ')
    comunidad=input()
    print('Ingresa un host: ')
    host=input()
    print('Ingresa un Object ID: ')
    oid=input()
    #1.3.6.1.2.1.2.2.1.10.3'
    #createUpdate('grupo_4cm1', 'localhost', '1.3.6.1.2.1.2.2.1.3.1', '161')
    analizarExamen(comunidad,host,oid)
elif (opcion==3):
    graficar()
else:
    createRRDTOOL("examen.rrd",'1551252880','10')
    createUpdate('grupo_4cm1', 'localhost', '1.3.6.1.2.1.2.2.1.3.1', '161')