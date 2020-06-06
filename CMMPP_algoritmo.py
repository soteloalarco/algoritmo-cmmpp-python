
import pandas as pd
import itertools as iter
from clases.GeneradorAlarma import GeneradorAlarmas
from funciones.funcionesdispositivos import creardispositivos
from funciones.funcionesdispositivos import calcularPnk
from funciones.miscelaneo import distanciaList
import numpy as np


######################################################
#Variables a modificar
tiempoLimite = 1 # segundos, tiempo de paro del algoritmo
deltaTiempo = 0.1 #segundos , diferencial de tiempo entre iteración
numerosDecimalesDeltaTiempo=1 #Si se modifica deltaTiempo modificar también esta veriable
tiposDispositivos=3 # Cantidad total de dispositivos a caracterizar a continuación
radiocelula=50 # radio de la célula en metros
modelodisopsitivos=0 # 0 para PPP y 1 para uniforme
repeticiones=1 # repeticiones de la rutina CCMMPP

### Control de iluminación
dipositivos_Tipo1 = 0.5 # intensidad de dispositivos/m^2, o cantidad total si el modelo de distribución  (modelodispositivos) es uniforme
lambdaRegular_Tipo1=1/40 # la tasa lambda para el estado regular de los dispositivos de tipo 1 (1 paquete cada 60 seg)
lambdaAlarma_Tipo1=1/20 # la tasa a la que se producen eventos de alarma para este tipo de dispositivos (1 evento cada 500 seg)
velPropagacionAlarma_Tipo1= 500 # m/s Velocidad de propagación de alarma
modeloEspacial_Tipo1=0 # Propagación espacial de alarma, 0 Decaying exponential 1 raised-cosine Window
constanteEspacial1_Tipo1= 0.007 # alpha para Decaying exponential, W para raised-cosine Window
constanteEspacial2_Tipo1=0 # ignorar para Decaying exponential, dth para raised-cosine Window
#animacion
color_Tipo1= 'b'
marcador_Tipo1= 'd'

### Monitoreo de consumo del agua y electricidad
dipositivos_Tipo2 = 0.2 # intensidad de dispositivos/m^2, o cantidad total si el modelo de distribución es uniforme
lambdaRegular_Tipo2=1/60 # la tasa lambda para el estado regular de los dispositivos de tipo 2 (0.5 paquete cada 60 seg)
lambdaAlarma_Tipo2=1/1000 # la tasa a la que se producen eventos de alarma para este tipo de dispositivos (1 evento cada 200 seg)
velPropagacionAlarma_Tipo2= 500 # m/s Velocidad de propagación de alarma
modeloEspacial_Tipo2=1 # Propagación espacial de alarma, 0 Decaying exponential 1 raised-cosine Window
constanteEspacial1_Tipo2= 200 # alpha para Decaying exponential, W para raised-cosine Window
constanteEspacial2_Tipo2=80 # ignorar para Decaying exponential, dth para raised-cosine Window
#animacion
color_Tipo2= 'r'
marcador_Tipo2= '*'

### Detección de terremotos
dipositivos_Tipo3 = 30 # intensidad de dispositivos/m^2, o cantidad total si el modelo de distribución es uniforme
lambdaRegular_Tipo3=1/180 # la tasa lambda para el estado regular de los dispositivos de tipo 2 (0.5 paquete cada 60 seg)
lambdaAlarma_Tipo3=1/50 # la tasa a la que se producen eventos de alarma para este tipo de dispositivos (1 evento cada 350 seg)
velPropagacionAlarma_Tipo3= 3000 # m/s Velocidad de propagación de alarma
modeloEspacial_Tipo3=0 # Propagación espacial de alarma, 0 Decaying exponential 1 raised-cosine Window
constanteEspacial1_Tipo3= 0.007 # alpha para Decaying exponential, W para raised-cosine Window
constanteEspacial2_Tipo3=0 # ignorar para Decaying exponential, dth para raised-cosine Window
#animacion
color_Tipo3= 'k'
marcador_Tipo3= '^'

######################################################
#Inicialización de parámetros y variables

areaCelula= np.pi * radiocelula ** 2  # area de la célula
#Iniciamos la creación de dispositivos según la distribución seleccionada
#Dispositivos tipo 1
if(modelodisopsitivos==0):
    cantidad_Tipo1= np.random.poisson(dipositivos_Tipo1 * areaCelula)  # Poisson número de dispoitivos de tipo1
else:
    cantidad_Tipo1=dipositivos_Tipo1 # si no se trata de un PPP se generarán los dispositivos especifiados
theta_Tipo1 = 2 * np.pi * np.random.uniform(0, 1, cantidad_Tipo1)
rho_Tipo1 = radiocelula * np.sqrt(np.random.uniform(0, 1, cantidad_Tipo1))
# Convertimos las coordenadas polares a cartesianas
xx_Tipo1 = theta_Tipo1 * np.cos(theta_Tipo1)
yy_Tipo1 = theta_Tipo1 * np.sin(theta_Tipo1)
posiciones_Tipo1=[xx_Tipo1,yy_Tipo1] # Esta lista se usará para asignar posiciones a los dispositivos que se crearán
#Dispositivos tipo 2
if(modelodisopsitivos==0):
    cantidad_Tipo2= np.random.poisson(dipositivos_Tipo2 * areaCelula)  # Poisson número de dispoitivos de tipo1
else:
    cantidad_Tipo2=dipositivos_Tipo2 # si no se trata de un PPP se generarán los dispositivos especifiados
theta_Tipo2 = 2 * np.pi * np.random.uniform(0, 1, cantidad_Tipo2)
rho_Tipo2 = radiocelula * np.sqrt(np.random.uniform(0, 1, cantidad_Tipo2))
# Convertimos las coordenadas polares a cartesianas
xx_Tipo2 = theta_Tipo2 * np.cos(theta_Tipo2)
yy_Tipo2 = theta_Tipo2 * np.sin(theta_Tipo2)
posiciones_Tipo2=[xx_Tipo2,yy_Tipo2]# Esta lista se usará para asignar posiciones a los dispositivos que se crearán
#Dispositivos tipo 3
if(modelodisopsitivos==0):
    cantidad_Tipo3= np.random.poisson(dipositivos_Tipo3 * areaCelula)  # Poisson número de dispoitivos de tipo1
else:
    cantidad_Tipo3=dipositivos_Tipo3 # si no se trata de un PPP se generarán los dispositivos especifiados
theta_Tipo3 = 2 * np.pi * np.random.uniform(0, 1, cantidad_Tipo3)
rho_Tipo3 = radiocelula * np.sqrt(np.random.uniform(0, 1, cantidad_Tipo3))
# Convertimos las coordenadas polares a cartesianas
xx_Tipo3 = theta_Tipo3 * np.cos(theta_Tipo3)
yy_Tipo3 = theta_Tipo3 * np.sin(theta_Tipo3)
posiciones_Tipo3=[xx_Tipo3,yy_Tipo3]# Esta lista se usará para asignar posiciones a los dispositivos que se crearán


tiempo = 0 # tiempo inicial
iteraciones=tiempoLimite/deltaTiempo # las iteraciones  que se producirán recorriendo el tiempo k
dispositivos= [] # una lista para guardar las instancias de dipoitivos de distintos tipos
generadoresAlarmas=[] # una lista para guardar los genradores de eventos de alarmas, uno para cada tipo de dispositivo
nuevaAlarma= [False] * tiposDispositivos
#animacionTrafico= AnimacionTrafico() # Creamos animación y la dibujamos
#animacionTrafico.dibujar()
#animacionTrafico.actualizar()

#Se generan las instancias de cada tipo de dipositivos y sus generadores de alarmas
dispositivos.append(creardispositivos(cantidad_Tipo1,posiciones_Tipo1, lambdaRegular_Tipo1,'Control de iluminacion',tiempo,color_Tipo1,marcador_Tipo1))
generadoresAlarmas.append(GeneradorAlarmas(lambdaAlarma_Tipo1,velPropagacionAlarma_Tipo1,tiempo,modeloEspacial_Tipo1,constanteEspacial1_Tipo1,constanteEspacial2_Tipo1,[0,0]))
dispositivos.append(creardispositivos(cantidad_Tipo2, posiciones_Tipo2,lambdaRegular_Tipo2,'Monitoreo de agua y electricidad',tiempo,color_Tipo2,marcador_Tipo2))
generadoresAlarmas.append(GeneradorAlarmas(lambdaAlarma_Tipo2,velPropagacionAlarma_Tipo2,tiempo,modeloEspacial_Tipo2,constanteEspacial1_Tipo2,constanteEspacial2_Tipo2,[0,0]))
dispositivos.append(creardispositivos(cantidad_Tipo3, posiciones_Tipo3,lambdaRegular_Tipo3,'Deteccion de terremotos',tiempo,color_Tipo3,marcador_Tipo3))
generadoresAlarmas.append(GeneradorAlarmas(lambdaAlarma_Tipo3,velPropagacionAlarma_Tipo3,tiempo,modeloEspacial_Tipo3,constanteEspacial1_Tipo3,constanteEspacial2_Tipo3,[0,0]))

#Graficamos los dispositivos en la celda
#for dispositivosaux in dispositivos:
#    for dispositivo in dispositivosaux: #ciclo para recorrer la lista de dispositivos y dibujar cada uno
#        animacionTrafico.dibujarDispositivo(dispositivo.posicion,dispositivo.color,dispositivo.marcador)
#animacionTrafico.actualizar()

##########  Algoritmo CMMPP  #################

for k in range(0,int(iteraciones + 1)): # Ciclo que avanza el tiempo

    for dispositivosaux,generadorAlarma,tipoDisp in iter.zip_longest(dispositivos,generadoresAlarmas,range(0,dispositivos.__len__())): # Ciclo que recorre los distintos tipos de dispositivos y sus geenradores de alarmas

        if(tiempo==0):
            nuevaAlarma[tipoDisp]= generadorAlarma.generarAlarma(tiempo,radiocelula) # se calcula el primer tiempo de alarma

        for dispositivo in dispositivosaux: # Ciclo que recorre cada uno de los dispositivos del mismo tipo

            dispositivo.registrarAlarma(generadorAlarma.idAlarma,generadorAlarma.siguienteArribo,(generadorAlarma.siguienteArribo+(distanciaList(dispositivo.posicion,generadorAlarma.posicion)/generadorAlarma.velocidad))[0],generadorAlarma.posicion,nuevaAlarma[tipoDisp])

            [listaPnk, nuevaListaAlarmas]= calcularPnk(tiempo,dispositivo.listaAlarmas,generadorAlarma.velocidad,generadorAlarma.modeloEspacial,generadorAlarma.constanteEspacial1,generadorAlarma.constanteEspacial2,dispositivo.m_Pu,dispositivo.m_Pc,deltaTiempo) # parte A del diagrama  /assets/CMMPP_diagrama.jpg

            # listaAlarmas=[idAlarma,tiempoAparicion,tiempoLLegada,posicionAlarma,self.posicion] esta es la forma de listaAlarmas
            for pnk,listaAlarmas in iter.zip_longest(listaPnk,dispositivo.listaAlarmas):
                dispositivo.actualizarestado(pnk) # parte B del diagrama
                dispositivo.generararribo(tiempo,listaAlarmas[0],listaAlarmas[2],numerosDecimalesDeltaTiempo) # parte C del diagrama
                dispositivo.actualizarestadoanormal() # por si hay más de un evento que cree estados de alarma, se cambia siempre a estado normal,

            dispositivo.actualizarListaAlarmas(nuevaListaAlarmas)


        nuevaAlarma[tipoDisp]= generadorAlarma.generarAlarma(tiempo,radiocelula)  # se genera una nueva alarma en una posición aleatoria si la actual ya sucedió


    tiempo = round(tiempo + deltaTiempo, numerosDecimalesDeltaTiempo) # Función para redondear decimales


def takeSecond(elem):
    return elem[1]
arriboOrdenado = dispositivo.registroCompletoArribos.sort(key=takeSecond)


for arribo in dispositivo.registroCompletoArribos:
    estadoAux= "normal" if arribo[4]==0 else "alarma"


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