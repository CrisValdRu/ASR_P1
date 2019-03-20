import sys
import rrdtool
import time




def graficarRRD(nombre):
        ret = rrdtool.graph( "png/"+nombre+".png",
                "--start",'1551649830',
                "--end","N",
                "--vertical-label=Bytes/s",
                "DEF:inoctets=rrd/"+nombre+".rrd:inoctets:AVERAGE",
                "AREA:inoctets#00FF00:"+nombre)

def graficarMinimosCuadrados (nombre):
        ultima_lectura = int(rrdtool.last("rrd/"+nombre+".rrd"))
        tiempo_final = ultima_lectura
        #tiempo_inicial = tiempo_final-600
        tiempo_inicial = 1539658453
        ret = rrdtool.graphv( "png/"+nombre+"MinCua.png",
                "--start",str(tiempo_inicial),
                "--end",str(tiempo_final+4000),
                "--title=Uso de CPU",
                "--color", 
                "ARROW#009900",
                '--vertical-label', "Uso de CPU (%)",
                
                '--lower-limit', '0',
                '--upper-limit', '100',

                "DEF:outTrafic=rrd/"+nombre+".rrd:CPUload:AVERAGE",

                "VDEF:m=outTrafic,LSLSLOPE",
                "VDEF:b=outTrafic,LSLINT",
                "VDEF:CPUmax=outTrafic,MAXIMUM",
                "CDEF:tendencia=outTrafic,POP,m,COUNT,*,b,+",
                "CDEF:limites=tendencia,90,100,LIMIT",
                "VDEF:limite1=limites,FIRST",
                "VDEF:limite2=limites,LAST",

                

                "VDEF:CPUlast=outTrafic,LAST",
                "PRINT:CPUlast:%6.2lf %S",

                #"AREA:outTrafic#005500:Carga de cpu",
                "HRULE:90#00FF00",
                "AREA:limites#FFBB0077",
                #"AREA:limite1#00000077:limite1",
                #"AREA:tendencia#FFBB0077",
                #"LINE2:tendencia#FFBB00",
                "AREA:outTrafic#005500:Carga de cpu",
                "LINE1:tendencia#FFBB00:dashes=3:Tendencia",
                #"AREA:limite1#FFFFFF",
                
                
                "GPRINT:limite1:  limite 1 %c :strftime",
                "GPRINT:limite1:  limite 1 %6.2lf %S",
                #"GPRINT:limite2:  \nlimite2 %c \\n:strftime",
                #"GPRINT:limite2:  limite2 %6.2lf %S"
                
                )
        #print(ret['print[0]'])
        ultimo_valor=float(ret['print[0]'])
        return ultimo_valor

def graficarObjectsRRD(nombre):
        ultima_lectura = int(rrdtool.last("rrd/"+nombre+".rrd"))
        tiempo_final = ultima_lectura
        tiempo_inicial = tiempo_final-600
        ret = rrdtool.graphv( "png/"+nombre+".png",
                "--start",str(tiempo_inicial),
                "--end",str(tiempo_final),
                "--title=Uso de CPU",
                "--color", 
                "ARROW#009900",
                '--vertical-label', "Uso de CPU (%)",
                
                '--lower-limit', '0',
                '--upper-limit', '100',

                "DEF:outTrafic=rrd/"+nombre+".rrd:outoctets:AVERAGE",
                "CDEF:umbral25=outTrafic,25,LT,0,outTrafic,IF",
                "CDEF:umbral50=outTrafic,50,LT,0,outTrafic,IF",
                "CDEF:umbral75=outTrafic,75,LT,0,outTrafic,IF",

                "VDEF:m=outTrafic,LSLSLOPE",
                "VDEF:b=outTrafic,LSLINT",
                "CDEF:tendencia=outTrafic,POP,m,COUNT,*,b,+",


                #"CDEF:tendenciaPred=tendencia,90,LT,0,tendencia,IF",
                #"CDEF:tendenciaMin=outTrafic,POP,m,COUNT,*,b,+,3,-",
                #"CDEF:tendenciaMax=outTrafic,POP,m,COUNT,*,b,+,3,+",

                "VDEF:CPUlast=outTrafic,LAST",
                "VDEF:CPUmin=outTrafic,MINIMUM",
                "VDEF:CPUavg=outTrafic,AVERAGE",
                "VDEF:CPUmax=outTrafic,MAXIMUM",
                "VDEF:CPUSTDEV=outTrafic,STDEV",

                "GPRINT:CPUlast:%6.2lf %SLAST",
                "GPRINT:CPUmin:%6.2lf %SMIN",
                "GPRINT:CPUavg:%13.0lf%SAVG",
                "GPRINT:CPUmax:%6.2lf %SMAX",
                "GPRINT:CPUSTDEV:%6.2lf %SSTDEV",
                "PRINT:CPUlast:%6.2lf %S",
                #"PRINT:tendenciaPred:%6.2lf %S",

                "AREA:outTrafic#005500:Carga de cpu",
                "AREA:umbral25#00FF00:Tráfico de carga mayor que min",
                "AREA:umbral50#FFBB00:Tráfico de carga mayor que avg",
                "AREA:umbral75#FF0000:Tráfico de carga mayor que max",
                "HRULE:63#00FF00:Umbral ready",
                "HRULE:78#FFBB00:Umbral set",
                "HRULE:85#FF0000:Umbral go"
                #"LINE1:tendenciaMin#00FF00",
                #"LINE1:tendenciaMax#FF0000",
                )
        #print(ret['print[0]'])
        ultimo_valor=[float(ret['print[0]']),float(63),float(78),float(85)]
        return ultimo_valor

        


def graficar(nombre):
        con = 0
        ret = rrdtool.graph( "png/"+nombre+".png",
                "--start",'1551649830',
                "--end","N",
                "--vertical-label=Bytes/s",
                "DEF:inoctets=rrd/"+nombre+".rrd:inoctets:AVERAGE",
                "AREA:inoctets#00FF00:"+nombre)

        while con<600:
                ret = rrdtool.graph( "png/"+nombre+".png",
                         "--start",'1551649830',
                         "--end","N",
                         "--vertical-label=Bytes/s",
                         "DEF:inoctets=rrd/"+nombre+".rrd:inoctets:AVERAGE",
                         "AREA:inoctets#00FF00:"+nombre)

                time.sleep(5)
                con+=5
                if(con == 595):
                        print("Desea seguir graficando? Y/N: ")
                        res=input()
                        if(res=='Y' or res=='y' or res=="Yes"):
                                con = 0
                        else:
                                con = 600
        