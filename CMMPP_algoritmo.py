import numpy as np  # NumPy package for arrays, random number generation, etc

from clases.DeviceMTC import DeviceMTC
from funciones.creardispositivos import creardispositivos

#Variables a modificar
tiempoLimite = 0.02 # segundos, tiempo de paro del algoritmo
deltaTiempo = 0.01 #segundos , diferencial de tiempo entre iteración
numerosDecimalesDeltaTiempo=2 #Si se modifica deltaTiempo modificar también esta veriable

dipositivos_Tipo1 = 1 # número de dispositivos de tipo 1
lambdaRegular_Tipo1=1/60 # la tasa lambda para el estado regular de los dispositivos de tipo 1 (1 paquete cada 60 seg)
dipositivos_Tipo2 = 2 # número de dispositivos de tipo 2
lambdaRegular_Tipo2=1/120 # la tasa lambda para el estado regular de los dispositivos de tipo 2 (0.5 paquete cada 60 seg)

#Inicialización de parámetros y variables
n_Tipo1 = 0 # dispositivo de tipo1 inicial
tiempo = 0 # tiempo inicial
iteraciones=tiempoLimite/deltaTiempo # las iteraciones  que se producirán recorriendo el tiempo k
dispositivos= [] # una lista para guardar las instancias de dipoitivos de distintos tipos

#Se generan las instancias de cada tipo de dipositivos
dispositivos.append(creardispositivos(dipositivos_Tipo1, lambdaRegular_Tipo1,'Control de iluminación'))
dispositivos.append(creardispositivos(dipositivos_Tipo2, lambdaRegular_Tipo2,'Monitoreo de consumo del agua y electricidad'))

##########  Algoritmo CMMPP  #################

for k in range(0,int(iteraciones + 1)): # Ciclo que avanza el tiempo

    print(tiempo)

    for dispositivosaux in dispositivos: # Ciclo que recorre todos los dispositivos
        for dispositivo in dispositivosaux:
            print(dispositivo.tipo)


    tiempo = round(tiempo + deltaTiempo, numerosDecimalesDeltaTiempo) # Función para redondear decimales