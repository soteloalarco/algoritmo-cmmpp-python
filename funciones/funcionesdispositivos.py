import numpy as np  # NumPy package for arrays, random number generation, etc
import math as math
from clases.DeviceMTC import DeviceMTC
from funciones.miscelaneo import distanciaList

def creardispositivos( numeroDispositivos, lambdaRegular_Tipo,tipo,tiempo,color,marcador):
    dispositivos = []
    for disp in range(0, numeroDispositivos):  # Generamos la cantidad indicada de dispositivos de cada tipo
        # TODO: crear una función para asignar la posición en la célula en un círculo
        dispositivos.append(
            DeviceMTC(lambdaRegular_Tipo, np.random.uniform(0, 100, 1)-50, np.random.uniform(0, 100, 1)-50, 0,tipo,tiempo,disp,[],0,color,marcador))

    return dispositivos
#TODO hacer el deltaTiempo Global
def funDeltaCustom(x,deltaTiempo):
    if(0<=x<deltaTiempo):
        return 1
    else:
        return 0

def calcularThetak(tiempoActual, tiempoAlarma,distancia,velocidad,deltaTiempo): #Theta_n[k] = theta[k] * delta_n
    print('distancia al sig evento ' + str(distancia))
    print('tiempo sig evento ' + str(tiempoAlarma))

    aux = (tiempoActual-tiempoAlarma-(distancia/velocidad))
    return funDeltaCustom(aux,deltaTiempo)

def calculardn(distancia,modelo,constanteEspacial1,constanteEspacial2): #Theta_n[k] = theta[k] * delta_n
    if(modelo==0):
        return math.exp(-constanteEspacial1*distancia)
    #TODO programar else de modelo raised-cosine window

def calcularPnk(tiempoActual,alarmas,velocidad,modelo,constanteEspacial1,constanteEspacial2,Pu,Pc,deltaTiempo): #Proceso maestro
    # alarma=[idAlarma,tiempoAparicion,tiempoLLegada,posicionAlarma,self.posicion]
    Pnk=[] # Pn[k]= Theta_n[k]*Pc + (1-Theta_n[k]*Pu)
    nuevaAlarma=[]  # despues de borrar los eventos que se resuelvan, esta sera la lista a sustituir en el dispositivo
    for alarma in alarmas: # Se verifican todas las alarmas pendientes
        distancia= distanciaList(alarma[3],alarma[4])
        thetak=calcularThetak(tiempoActual,alarma[1],distancia,velocidad,deltaTiempo) #Theta_n[k] = theta[k] * delta_n
        dn= calculardn(distancia,modelo,constanteEspacial1,constanteEspacial2)
        thetank = thetak*dn
        if(thetak==0): # si en esta ventana de tiempo la alarma no llega al dispositivo aun se agrega a la nueva lista
                nuevaAlarma.append(alarma)
        print('thetak ' + str(thetak))
        print('dn ' + str(dn))
        Pnk.append((1 - thetank) * Pu + thetank * Pc)   # Pn[k]= Theta_n[k]*Pc + (1-Theta_n[k]*Pu)

    return [Pnk,nuevaAlarma]

