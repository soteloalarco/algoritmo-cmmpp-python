import numpy as np  # NumPy package for arrays, random number generation, etc
import pandas as pd
import itertools as iter

from clases.GeneradorAlarma import GeneradorAlarmas
from funciones.funcionesdispositivos import creardispositivos
from funciones.funcionesdispositivos import calcularPnk
from funciones.miscelaneo import distanciaList

######################################################
#Variables a modificar
tiempoLimite = 500 # segundos, tiempo de paro del algoritmo
deltaTiempo = 0.01 #segundos , diferencial de tiempo entre iteración
numerosDecimalesDeltaTiempo=2 #Si se modifica deltaTiempo modificar también esta veriable

### Control de iluminación
dipositivos_Tipo1 = 300 # número de dispositivos de tipo 1,
lambdaRegular_Tipo1=1/60 # la tasa lambda para el estado regular de los dispositivos de tipo 1 (1 paquete cada 60 seg)
lambdaAlarma_Tipo1=1/60 # la tasa a la que se producen eventos de alarma para este tipo de dispositivos (1 evento cada 500 seg)
velPropagacionAlarma_Tipo1= 500 # m/s Velocidad de propagación de alarma
modeloEspacial_Tipo1=0 # Propagación espacial de alarma, 0 Decaying exponential 1 raised-cosine Window
constanteEspacial1_Tipo1= 0.1 # alpha para Decaying exponential, W para raised-cosine Window
constanteEspacial2_Tipo1=0 # ignorar para Decaying exponential, dth para raised-cosine Window

### Monitoreo de consumo del agua y electricidad
dipositivos_Tipo2 = 300 # número de dispositivos de tipo 2
lambdaRegular_Tipo2=1/120 # la tasa lambda para el estado regular de los dispositivos de tipo 2 (0.5 paquete cada 60 seg)
lambdaAlarma_Tipo2=1/60 # la tasa a la que se producen eventos de alarma para este tipo de dispositivos (1 evento cada 200 seg)
velPropagacionAlarma_Tipo2= 600 # m/s Velocidad de propagación de alarma
modeloEspacial_Tipo2=0 # Propagación espacial de alarma, 0 Decaying exponential 1 raised-cosine Window
constanteEspacial1_Tipo2= 0.1 # alpha para Decaying exponential, W para raised-cosine Window
constanteEspacial2_Tipo2=0 # ignorar para Decaying exponential, dth para raised-cosine Window

### Detección de terremotos
dipositivos_Tipo3 = 300 # número de dispositivos de tipo 3
lambdaRegular_Tipo3=1/180 # la tasa lambda para el estado regular de los dispositivos de tipo 2 (0.5 paquete cada 60 seg)
lambdaAlarma_Tipo3=1/60 # la tasa a la que se producen eventos de alarma para este tipo de dispositivos (1 evento cada 350 seg)
velPropagacionAlarma_Tipo3= 100 # m/s Velocidad de propagación de alarma
modeloEspacial_Tipo3=0 # Propagación espacial de alarma, 0 Decaying exponential 1 raised-cosine Window
constanteEspacial1_Tipo3= 0.1 # alpha para Decaying exponential, W para raised-cosine Window
constanteEspacial2_Tipo3=0 # ignorar para Decaying exponential, dth para raised-cosine Window

######################################################
#Inicialización de parámetros y variables
n_Tipo1 = 0 # dispositivo de tipo1 inicial
tiempo = 0 # tiempo inicial
iteraciones=tiempoLimite/deltaTiempo # las iteraciones  que se producirán recorriendo el tiempo k
dispositivos= [] # una lista para guardar las instancias de dipoitivos de distintos tipos
generadoresAlarmas=[] # una lista para guardar los genradores de eventos de alarmas, uno para cada tipo de dispositivo

#Se generan las instancias de cada tipo de dipositivos y sus generadores de alarmas
dispositivos.append(creardispositivos(dipositivos_Tipo1, lambdaRegular_Tipo1,'Control de iluminación',tiempo))
generadoresAlarmas.append(GeneradorAlarmas(lambdaAlarma_Tipo1,velPropagacionAlarma_Tipo1,tiempo,modeloEspacial_Tipo1,constanteEspacial1_Tipo1,constanteEspacial2_Tipo1,[0,0]))
dispositivos.append(creardispositivos(dipositivos_Tipo2, lambdaRegular_Tipo2,'Monitoreo de consumo del agua y electricidad',tiempo))
generadoresAlarmas.append(GeneradorAlarmas(lambdaAlarma_Tipo2,velPropagacionAlarma_Tipo2,tiempo,modeloEspacial_Tipo2,constanteEspacial1_Tipo2,constanteEspacial2_Tipo2,[0,0]))
dispositivos.append(creardispositivos(dipositivos_Tipo3, lambdaRegular_Tipo3,'Detección de terremotos',tiempo))
generadoresAlarmas.append(GeneradorAlarmas(lambdaAlarma_Tipo3,velPropagacionAlarma_Tipo3,tiempo,modeloEspacial_Tipo3,constanteEspacial1_Tipo3,constanteEspacial2_Tipo3,[0,0]))

##########  Algoritmo CMMPP  #################

for k in range(0,int(iteraciones + 1)): # Ciclo que avanza el tiempo

    for dispositivosaux,generadorAlarma in iter.zip_longest(dispositivos,generadoresAlarmas): # Ciclo que recorre los distintos tipos de dispositivos y sus geenradores de alarmas

        generadorAlarma.generarAlarma(tiempo) # se genera una nueva alarma en una posición aleatoria si la actual ya sucedió

        theta = np.random.beta(3, 4, 1)  # variable aleatoria beta para determinar Theta_n[k] = theta[k] * delta_n , una distinta por cada aplicacion

        for dispositivo in dispositivosaux: # Ciclo que recorre cada uno de los dispositivos del mismo tipo
            Pnk= calcularPnk(tiempo,generadorAlarma.siguienteArribo,distanciaList(generadorAlarma.posicion,dispositivo.posicion),generadorAlarma.velocidad,generadorAlarma.modeloEspacial,generadorAlarma.constanteEspacial1,generadorAlarma.constanteEspacial2,dispositivo.m_Pu,dispositivo.m_Pc,deltaTiempo) # parte A del diagrama  /assets/CMMPP_diagrama.jpg
            dispositivo.actualizarestado(Pnk) # parte B del diagrama
            dispositivo.generararribo(tiempo) # parte C del diagrama



    tiempo = round(tiempo + deltaTiempo, numerosDecimalesDeltaTiempo) # Función para redondear decimales


def takeSecond(elem):
    return elem[0]
arriboOrdenado = dispositivo.registroCompletoArribos.sort(key=takeSecond)


for arribo in dispositivo.registroCompletoArribos:
    estadoAux= "normal" if arribo[3]==0 else "alarma"
    print ("Instante: " + str(arribo[0]) +"     Identificador: " +str(arribo[2])+ ":"+str(arribo[1])+"      Estado: "+ estadoAux+"         Tamaño paquete:  "+str(arribo[4]))

#Registro de todos los eventos
ListaEventos = dispositivo.registroCompletoArribos
# Creación de un Dataframe apartir de una lista
df_eventos=pd.DataFrame(ListaEventos)
# Guardado de datos en archivo con extensión .csv
df_eventos.to_csv("ArchivoEventos.csv")
# Recuperación de archivo
df_eventos_rec = pd.read_csv("ArchivoEventos.csv", index_col=0)
# Convertir de DataFrame a Lista
ListaEventosrec = df_eventos_rec.values.tolist()