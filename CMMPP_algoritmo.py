import numpy as np  # NumPy package for arrays, random number generation, etc

from clases.DeviceMTC import DeviceMTC
from funciones.funcionesdispositivos import creardispositivos

#Variables a modificar
tiempoLimite = 0.02 # segundos, tiempo de paro del algoritmo
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
dispositivos.append(creardispositivos(dipositivos_Tipo1, lambdaRegular_Tipo1,'Control de iluminación'))
dispositivos.append(creardispositivos(dipositivos_Tipo2, lambdaRegular_Tipo2,'Monitoreo de consumo del agua y electricidad'))
dispositivos.append(creardispositivos(dipositivos_Tipo3, lambdaRegular_Tipo3,'Detección de terremotos'))

##########  Algoritmo CMMPP  #################

for k in range(0,int(iteraciones + 1)): # Ciclo que avanza el tiempo
    print(tiempo)

    theta = np.random.beta(3, 4, 1) # variable aleatoria beta para determinar Theta_n[k] = theta[k] * delta_n

    for dispositivosaux in dispositivos: # Ciclo que recorre todos los dispositivos
        for dispositivo in dispositivosaux:
            print(dispositivo.tipo)
            Pnk= dispositivo.calcular_Pnk(theta)  # parte A del diagrama  /assets/CMMPP_diagrama.jpg
            print(Pnk)
            dispositivo.actualizarestado(Pnk)


    tiempo = round(tiempo + deltaTiempo, numerosDecimalesDeltaTiempo) # Función para redondear decimales