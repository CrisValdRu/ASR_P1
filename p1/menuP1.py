from updateRRD import createUpdate, analizarTraficoRed

print('------------P1 ASR------------'
      '\nSelecciona un valor:\n'
      '1) CreateRRD\n'
      '2) UpdateRRD\n'
      '3) graphRRD')

opcion=int(input())

if(opcion==2):
    print('\nIngresa una comunidad: ')
    comunidad=input()
    print('Ingresa un host: ')
    host=input()
    print('Ingresa un Object ID: ')
    oid=input()
    createUpdate(comunidad, host, oid)
else:
    analizarTraficoRed()