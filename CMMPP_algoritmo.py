import numpy as np  # NumPy package for arrays, random number generation, etc
import pandas as pd

from clases.DeviceMTC import DeviceMTC
from funciones.funcionesdispositivos import creardispositivos

#Variables a modificar
tiempoLimite = 100 # segundos, tiempo de paro del algoritmo
deltaTiempo = 0.01 #segundos , diferencial de tiempo entre iteración
numerosDecimalesDeltaTiempo=2 #Si se modifica deltaTiempo modificar también esta veriable

dipositivos_Tipo1 = 3 # número de dispositivos de tipo 1, Control de iluminación
lambdaRegular_Tipo1=1/60 # la tasa lambda para el estado regular de los dispositivos de tipo 1 (1 paquete cada 60 seg)
dipositivos_Tipo2 = 2 # número de dispositivos de tipo 2, Monitoreo de consumo del agua y electricidad
lambdaRegular_Tipo2=1/120 # la tasa lambda para el estado regular de los dispositivos de tipo 2 (0.5 paquete cada 60 seg)
dipositivos_Tipo3 = 1 # número de dispositivos de tipo 3, Detección de terremotos
lambdaRegular_Tipo3=1/180 # la tasa lambda para el estado regular de los dispositivos de tipo 2 (0.5 paquete cada 60 seg)

#Inicialización de parámetros y variables
n_Tipo1 = 0 # dispositivo de tipo1 inicial
tiempo = 0 # tiempo inicial
iteraciones=tiempoLimite/deltaTiempo # las iteraciones  que se producirán recorriendo el tiempo k
dispositivos= [] # una lista para guardar las instancias de dipoitivos de distintos tipos

#Se generan las instancias de cada tipo de dipositivos
dispositivos.append(creardispositivos(dipositivos_Tipo1, lambdaRegular_Tipo1,'Control de iluminación',tiempo))
dispositivos.append(creardispositivos(dipositivos_Tipo2, lambdaRegular_Tipo2,'Monitoreo de consumo del agua y electricidad',tiempo))
dispositivos.append(creardispositivos(dipositivos_Tipo3, lambdaRegular_Tipo3,'Detección de terremotos',tiempo))

##########  Algoritmo CMMPP  #################

for k in range(0,int(iteraciones + 1)): # Ciclo que avanza el tiempo
    print(tiempo)

    for dispositivosaux in dispositivos: # Ciclo que recorre todos los dispositivos
        theta = np.random.beta(3, 4, 1)  # variable aleatoria beta para determinar Theta_n[k] = theta[k] * delta_n , una distinta por cada aplicacion
        for dispositivo in dispositivosaux:
            print(dispositivo.tipo)
            Pnk= dispositivo.calcular_Pnk(theta)  # parte A del diagrama  /assets/CMMPP_diagrama.jpg
            print(Pnk)
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
df_eventos_rec = pd.read_csv("prueba1.csv", index_col=0)
# Convertir de DataFrame a Lista
ListaEventosrec = df_eventos_rec.values.tolist()