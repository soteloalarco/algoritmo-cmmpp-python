import tkinter as tk
from tkinter import ttk
import pandas as pd
import itertools as iter
from clases.GeneradorAlarma import GeneradorAlarmas
from funciones.funcionesdispositivos import creardispositivos
from funciones.funcionesdispositivos import calcularPnk
from funciones.miscelaneo import distanciaList
from decimal import *
import numpy as np

class Application(tk.Frame):

    # Variables a modificar
    tiempoLimite = 1  # segundos, tiempo de paro del algoritmo
    deltaTiempo = 0.1  # segundos , diferencial de tiempo entre iteración
    numerosDecimalesDeltaTiempo = 1  # Si se modifica deltaTiempo modificar también esta veriable
    tiposDispositivos = 3  # Cantidad total de dispositivos a caracterizar a continuación
    radiocelula=50 # radio de la célula en metros
    modelodispositivos=0 # 0 para PPP y 1 para uniforme
    repeticiones=1 # repeticiones de la rutina CCMMPP

    ### Control de iluminación
    dipositivos_Tipo1 = 0.05  # intensidad de dispositivos/m^2, o cantidad total si el modelo de distribución  (modelodispositivos) es uniforme
    lambdaRegular_Tipo1 = 1 / 40  # la tasa lambda para el estado regular de los dispositivos de tipo 1 (1 paquete cada 60 seg)
    lambdaAlarma_Tipo1 = 1 / 20  # la tasa a la que se producen eventos de alarma para este tipo de dispositivos (1 evento cada 500 seg)
    velPropagacionAlarma_Tipo1 = 500  # m/s Velocidad de propagación de alarma
    modeloEspacial_Tipo1 = 0  # Propagación espacial de alarma, 0 Decaying exponential 1 raised-cosine Window
    constanteEspacial1_Tipo1 = 0.007  # alpha para Decaying exponential, W para raised-cosine Window
    constanteEspacial2_Tipo1 = 0  # ignorar para Decaying exponential, dth para raised-cosine Window
    # animacion
    color_Tipo1 = 'b'
    marcador_Tipo1 = 'd'

    ### Monitoreo de consumo del agua y electricidad
    dipositivos_Tipo2 = 0.1  # intensidad de dispositivos/m^2, o cantidad total si el modelo de distribución  (modelodispositivos) es uniforme
    lambdaRegular_Tipo2 = 1 / 60  # la tasa lambda para el estado regular de los dispositivos de tipo 2 (0.5 paquete cada 60 seg)
    lambdaAlarma_Tipo2 = 1 / 1000  # la tasa a la que se producen eventos de alarma para este tipo de dispositivos (1 evento cada 200 seg)
    velPropagacionAlarma_Tipo2 = 500  # m/s Velocidad de propagación de alarma
    modeloEspacial_Tipo2 = 1  # Propagación espacial de alarma, 0 Decaying exponential 1 raised-cosine Window
    constanteEspacial1_Tipo2 = 200  # alpha para Decaying exponential, W para raised-cosine Window
    constanteEspacial2_Tipo2 = 80  # ignorar para Decaying exponential, dth para raised-cosine Window
    # animacion
    color_Tipo2 = 'r'
    marcador_Tipo2 = '*'

    ### Detección de terremotos
    dipositivos_Tipo3 = 0.08 # intensidad de dispositivos/m^2, o cantidad total si el modelo de distribución  (modelodispositivos) es uniforme
    lambdaRegular_Tipo3 = 1 / 180  # la tasa lambda para el estado regular de los dispositivos de tipo 2 (0.5 paquete cada 60 seg)
    lambdaAlarma_Tipo3 = 1 / 50  # la tasa a la que se producen eventos de alarma para este tipo de dispositivos (1 evento cada 350 seg)
    velPropagacionAlarma_Tipo3 = 3000  # m/s Velocidad de propagación de alarma
    modeloEspacial_Tipo3 = 0  # Propagación espacial de alarma, 0 Decaying exponential 1 raised-cosine Window
    constanteEspacial1_Tipo3 = 0.007  # alpha para Decaying exponential, W para raised-cosine Window
    constanteEspacial2_Tipo3 = 0  # ignorar para Decaying exponential, dth para raised-cosine Window
    # animacion
    color_Tipo3 = 'k'
    marcador_Tipo3 = '^'

    ### Contaminación del aire
    dipositivos_Tipo4 = 0.01  # intensidad de dispositivos/m^2, o cantidad total si el modelo de distribución  (modelodispositivos) es uniforme
    lambdaRegular_Tipo4 = 1 / 190  # la tasa lambda para el estado regular de los dispositivos de tipo 2 (0.5 paquete cada 60 seg)
    lambdaAlarma_Tipo4 = 1 / 100  # la tasa a la que se producen eventos de alarma para este tipo de dispositivos (1 evento cada 350 seg)
    velPropagacionAlarma_Tipo4 = 1000  # m/s Velocidad de propagación de alarma
    modeloEspacial_Tipo4 = 0  # Propagación espacial de alarma, 0 Decaying exponential 1 raised-cosine Window
    constanteEspacial1_Tipo4 = 0.005  # alpha para Decaying exponential, W para raised-cosine Window
    constanteEspacial2_Tipo4 = 0  # ignorar para Decaying exponential, dth para raised-cosine Window
    # animacion
    color_Tipo4 = 'k'
    marcador_Tipo4 = '^'

    ### Control de semáforos
    dipositivos_Tipo5 = 0.03  # intensidad de dispositivos/m^2, o cantidad total si el modelo de distribución  (modelodispositivos) es uniforme
    lambdaRegular_Tipo5 = 1 / 170  # la tasa lambda para el estado regular de los dispositivos de tipo 2 (0.5 paquete cada 60 seg)
    lambdaAlarma_Tipo5 = 1 / 200  # la tasa a la que se producen eventos de alarma para este tipo de dispositivos (1 evento cada 350 seg)
    velPropagacionAlarma_Tipo5 = 2000  # m/s Velocidad de propagación de alarma
    modeloEspacial_Tipo5 = 1  # Propagación espacial de alarma, 0 Decaying exponential 1 raised-cosine Window
    constanteEspacial1_Tipo5 = 300  # alpha para Decaying exponential, W para raised-cosine Window
    constanteEspacial2_Tipo5 = 200  # ignorar para Decaying exponential, dth para raised-cosine Window
    # animacion
    color_Tipo5 = 'k'
    marcador_Tipo5 = '^'

    def resetTodo(self): #Cargamos al GUI los valores de la clase Application, los que erán poteriormente leidos para realizar la rutina
        #TODO leer de un archido
        #-----Inicio de Rutina

        self.tiemposimulacion.delete(0,tk.END)
        self.tiemposimulacion.insert(0,str(self.tiempoLimite))
        self.diftiempo.delete(0,tk.END)
        self.diftiempo.insert(0,str(self.deltaTiempo))
        if(self.modelodispositivos==0):
            self.modelodisp00.set('PPP')
        else:
            self.modelodisp00.set('Uniforme')
        self.radio00.delete(0,tk.END)
        self.radio00.insert(0,str(self.radiocelula))
        self.repeticiones00.delete(0,tk.END)
        self.repeticiones00.insert(0,str(self.repeticiones))

        self.cambiomodelodispresettodo()

        #-----Control de iluminación
        # Cantidad de dispositivos
        self.numero01.delete(0,tk.END)
        self.numero01.insert(0,str(self.dipositivos_Tipo1))
        # Tasa de paquete
        self.tasapaquete01.delete(0,tk.END)
        self.tasapaquete01.insert(0,str(self.lambdaRegular_Tipo1))
        # Tasa de alarma
        self.tasaalarma01.delete(0,tk.END)
        self.tasaalarma01.insert(0,str(self.lambdaAlarma_Tipo1))
        # Velocidad alarma
        self.veloalarma01.delete(0,tk.END)
        self.veloalarma01.insert(0,str(self.velPropagacionAlarma_Tipo1))
        # Propagación espacial
        if(self.modeloEspacial_Tipo1==0):
            self.modeloesp01.set("Decaying Exponential")
            self.constante11.set('Alpha')
            self.constante12.set('----')
            self.const101['state'] = 'normal'
            self.const201['state'] = 'disabled'
        else:
            self.modeloesp01.set("Raised-Cosine Window")
            self.constante11.set('W')
            self.constante12.set('dth')
            self.const101['state'] = 'normal'
            self.const201['state'] = 'normal'
        # Constantes de propagación espacial alpha,W,dth
        self.const101.delete(0,tk.END)
        self.const101.insert(0,str(self.constanteEspacial1_Tipo1))
        self.const201.delete(0, tk.END)
        self.const201.insert(0, str(self.constanteEspacial2_Tipo1))

        # -----Consumo de agua y electricidad
        # Cantidad de dispositivos
        self.numero02.delete(0, tk.END)
        self.numero02.insert(0, str(self.dipositivos_Tipo2))
        # Tasa de paquete
        self.tasapaquete02.delete(0, tk.END)
        self.tasapaquete02.insert(0, str(self.lambdaRegular_Tipo2))
        # Tasa de alarma
        self.tasaalarma02.delete(0, tk.END)
        self.tasaalarma02.insert(0, str(self.lambdaAlarma_Tipo2))
        # Velocidad alarma
        self.veloalarma02.delete(0, tk.END)
        self.veloalarma02.insert(0, str(self.velPropagacionAlarma_Tipo2))
        # Propagación espacial
        if (self.modeloEspacial_Tipo2 == 0):
            self.modeloesp02.set("Decaying Exponential")
            self.constante21.set('Alpha')
            self.constante22.set('----')
            self.const102['state'] = 'normal'
            self.const202['state'] = 'disabled'
        else:
            self.modeloesp02.set("Raised-Cosine Window")
            self.constante21.set('W')
            self.constante22.set('dth')
            self.const102['state'] = 'normal'
            self.const202['state'] = 'normal'
        # Constantes de propagación espacial alpha,W,dth
        self.const102.delete(0, tk.END)
        self.const102.insert(0, str(self.constanteEspacial1_Tipo2))
        self.const202.delete(0, tk.END)
        self.const202.insert(0, str(self.constanteEspacial2_Tipo2))

        # -----Detección de terremotos
        # Cantidad de dispositivos
        self.numero03.delete(0, tk.END)
        self.numero03.insert(0, str(self.dipositivos_Tipo3))
        # Tasa de paquete
        self.tasapaquete03.delete(0, tk.END)
        self.tasapaquete03.insert(0, str(self.lambdaRegular_Tipo3))
        # Tasa de alarma
        self.tasaalarma03.delete(0, tk.END)
        self.tasaalarma03.insert(0, str(self.lambdaAlarma_Tipo3))
        # Velocidad alarma
        self.veloalarma03.delete(0, tk.END)
        self.veloalarma03.insert(0, str(self.velPropagacionAlarma_Tipo3))
        # Propagación espacial
        if (self.modeloEspacial_Tipo3 == 0):
            self.modeloesp03.set("Decaying Exponential")
            self.constante31.set('Alpha')
            self.constante32.set('----')
            self.const103['state'] = 'normal'
            self.const203['state'] = 'disabled'
        else:
            self.modeloesp03.set("Raised-Cosine Window")
            self.constante31.set('W')
            self.constante32.set('dth')
            self.const103['state'] = 'normal'
            self.const203['state'] = 'normal'
        # Constantes de propagación espacial alpha,W,dth
        self.const103.delete(0, tk.END)
        self.const103.insert(0, str(self.constanteEspacial1_Tipo3))
        self.const203.delete(0, tk.END)
        self.const203.insert(0, str(self.constanteEspacial2_Tipo3))

        # -----Contaminacion del aire
        # Cantidad de dispositivos
        self.numero10.delete(0, tk.END)
        self.numero10.insert(0, str(self.dipositivos_Tipo4))
        # Tasa de paquete
        self.tasapaquete10.delete(0, tk.END)
        self.tasapaquete10.insert(0, str(self.lambdaRegular_Tipo4))
        # Tasa de alarma
        self.tasaalarma10.delete(0, tk.END)
        self.tasaalarma10.insert(0, str(self.lambdaAlarma_Tipo4))
        # Velocidad alarma
        self.veloalarma10.delete(0, tk.END)
        self.veloalarma10.insert(0, str(self.velPropagacionAlarma_Tipo4))
        # Propagación espacial
        if (self.modeloEspacial_Tipo4 == 0):
            self.modeloesp10.set("Decaying Exponential")
            self.constante41.set('Alpha')
            self.constante42.set('----')
            self.const110['state'] = 'normal'
            self.const210['state'] = 'disabled'
        else:
            self.modeloesp10.set("Raised-Cosine Window")
            self.constante41.set('W')
            self.constante42.set('dth')
            self.const110['state'] = 'normal'
            self.const210['state'] = 'normal'
        # Constantes de propagación espacial alpha,W,dth
        self.const110.delete(0, tk.END)
        self.const110.insert(0, str(self.constanteEspacial1_Tipo4))
        self.const210.delete(0, tk.END)
        self.const210.insert(0, str(self.constanteEspacial2_Tipo4))

        # -----Control de semáforos
        # Cantidad de dispositivos
        self.numero11.delete(0, tk.END)
        self.numero11.insert(0, str(self.dipositivos_Tipo5))
        # Tasa de paquete
        self.tasapaquete11.delete(0, tk.END)
        self.tasapaquete11.insert(0, str(self.lambdaRegular_Tipo5))
        # Tasa de alarma
        self.tasaalarma11.delete(0, tk.END)
        self.tasaalarma11.insert(0, str(self.lambdaAlarma_Tipo5))
        # Velocidad alarma
        self.veloalarma11.delete(0, tk.END)
        self.veloalarma11.insert(0, str(self.velPropagacionAlarma_Tipo5))
        # Propagación espacial
        if (self.modeloEspacial_Tipo5 == 0):
            self.modeloesp11.set("Decaying Exponential")
            self.constante51.set('Alpha')
            self.constante52.set('----')
            self.const111['state'] = 'normal'
            self.const211['state'] = 'disabled'
        else:
            self.modeloesp11.set("Raised-Cosine Window")
            self.constante51.set('W')
            self.constante52.set('dth')
            self.const111['state'] = 'normal'
            self.const211['state'] = 'normal'
        # Constantes de propagación espacial alpha,W,dth
        self.const111.delete(0, tk.END)
        self.const111.insert(0, str(self.constanteEspacial1_Tipo5))
        self.const211.delete(0, tk.END)
        self.const211.insert(0, str(self.constanteEspacial2_Tipo5))

    def reset1(self): # Función para resetear valores del frame Control de Iluminación
        # -----Control de iluminación
        # Cantidad de dispositivos
        self.numero01.delete(0, tk.END)
        self.numero01.insert(0, str(self.dipositivos_Tipo1))
        # Tasa de paquete
        self.tasapaquete01.delete(0, tk.END)
        self.tasapaquete01.insert(0, str(self.lambdaRegular_Tipo1))
        # Tasa de alarma
        self.tasaalarma01.delete(0, tk.END)
        self.tasaalarma01.insert(0, str(self.lambdaAlarma_Tipo1))
        # Velocidad alarma
        self.veloalarma01.delete(0, tk.END)
        self.veloalarma01.insert(0, str(self.velPropagacionAlarma_Tipo1))
        # Propagación espacial
        if (self.modeloEspacial_Tipo1 == 0):
            self.modeloesp01.set("Decaying Exponential")
            self.constante11.set('Alpha')
            self.constante12.set('----')
            self.const101['state'] = 'normal'
            self.const201['state'] = 'disabled'
        else:
            self.modeloesp01.set("Raised-Cosine Window")
            self.constante11.set('W')
            self.constante12.set('dth')
            self.const101['state'] = 'normal'
            self.const201['state'] = 'normal'
        # Constantes de propagación espacial alpha,W,dth
        self.const101.delete(0, tk.END)
        self.const101.insert(0, str(self.constanteEspacial1_Tipo1))
        self.const201.delete(0, tk.END)
        self.const201.insert(0, str(self.constanteEspacial2_Tipo1))

    def reset2(self):
        # -----Consumo de agua y electricidad
        # Cantidad de dispositivos
        self.numero02.delete(0, tk.END)
        self.numero02.insert(0, str(self.dipositivos_Tipo2))
        # Tasa de paquete
        self.tasapaquete02.delete(0, tk.END)
        self.tasapaquete02.insert(0, str(self.lambdaRegular_Tipo2))
        # Tasa de alarma
        self.tasaalarma02.delete(0, tk.END)
        self.tasaalarma02.insert(0, str(self.lambdaAlarma_Tipo2))
        # Velocidad alarma
        self.veloalarma02.delete(0, tk.END)
        self.veloalarma02.insert(0, str(self.velPropagacionAlarma_Tipo2))
        # Propagación espacial
        if (self.modeloEspacial_Tipo2 == 0):
            self.modeloesp02.set("Decaying Exponential")
            self.constante21.set('Alpha')
            self.constante22.set('----')
            self.const102['state'] = 'normal'
            self.const202['state'] = 'disabled'
        else:
            self.modeloesp02.set("Raised-Cosine Window")
            self.constante21.set('W')
            self.constante22.set('dth')
            self.const102['state'] = 'normal'
            self.const202['state'] = 'normal'
        # Constantes de propagación espacial alpha,W,dth
        self.const102.delete(0, tk.END)
        self.const102.insert(0, str(self.constanteEspacial1_Tipo2))
        self.const202.delete(0, tk.END)
        self.const202.insert(0, str(self.constanteEspacial2_Tipo2))

    def reset3(self):
        # -----Detección de terremotos
        # Cantidad de dispositivos
        self.numero03.delete(0, tk.END)
        self.numero03.insert(0, str(self.dipositivos_Tipo3))
        # Tasa de paquete
        self.tasapaquete03.delete(0, tk.END)
        self.tasapaquete03.insert(0, str(self.lambdaRegular_Tipo3))
        # Tasa de alarma
        self.tasaalarma03.delete(0, tk.END)
        self.tasaalarma03.insert(0, str(self.lambdaAlarma_Tipo3))
        # Velocidad alarma
        self.veloalarma03.delete(0, tk.END)
        self.veloalarma03.insert(0, str(self.velPropagacionAlarma_Tipo3))
        # Propagación espacial
        if (self.modeloEspacial_Tipo3 == 0):
            self.modeloesp03.set("Decaying Exponential")
            self.constante31.set('Alpha')
            self.constante32.set('----')
            self.const103['state'] = 'normal'
            self.const203['state'] = 'disabled'
        else:
            self.modeloesp03.set("Raised-Cosine Window")
            self.constante31.set('W')
            self.constante32.set('dth')
            self.const103['state'] = 'normal'
            self.const203['state'] = 'normal'
        # Constantes de propagación espacial alpha,W,dth
        self.const103.delete(0, tk.END)
        self.const103.insert(0, str(self.constanteEspacial1_Tipo3))
        self.const203.delete(0, tk.END)
        self.const203.insert(0, str(self.constanteEspacial2_Tipo3))

    def reset4(self):
        # -----Contaminacion del aire
        # Cantidad de dispositivos
        self.numero10.delete(0, tk.END)
        self.numero10.insert(0, str(self.dipositivos_Tipo4))
        # Tasa de paquete
        self.tasapaquete10.delete(0, tk.END)
        self.tasapaquete10.insert(0, str(self.lambdaRegular_Tipo4))
        # Tasa de alarma
        self.tasaalarma10.delete(0, tk.END)
        self.tasaalarma10.insert(0, str(self.lambdaAlarma_Tipo4))
        # Velocidad alarma
        self.veloalarma10.delete(0, tk.END)
        self.veloalarma10.insert(0, str(self.velPropagacionAlarma_Tipo4))
        # Propagación espacial
        if (self.modeloEspacial_Tipo4 == 0):
            self.modeloesp10.set("Decaying Exponential")
            self.constante41.set('Alpha')
            self.constante42.set('----')
            self.const110['state'] = 'normal'
            self.const210['state'] = 'disabled'
        else:
            self.modeloesp10.set("Raised-Cosine Window")
            self.constante41.set('W')
            self.constante42.set('dth')
            self.const110['state'] = 'normal'
            self.const210['state'] = 'normal'
        # Constantes de propagación espacial alpha,W,dth
        self.const110.delete(0, tk.END)
        self.const110.insert(0, str(self.constanteEspacial1_Tipo4))
        self.const210.delete(0, tk.END)
        self.const210.insert(0, str(self.constanteEspacial2_Tipo4))

    def reset5(self):
        # -----Control de semáforos
        # Cantidad de dispositivos
        self.numero11.delete(0, tk.END)
        self.numero11.insert(0, str(self.dipositivos_Tipo5))
        # Tasa de paquete
        self.tasapaquete11.delete(0, tk.END)
        self.tasapaquete11.insert(0, str(self.lambdaRegular_Tipo5))
        # Tasa de alarma
        self.tasaalarma11.delete(0, tk.END)
        self.tasaalarma11.insert(0, str(self.lambdaAlarma_Tipo5))
        # Velocidad alarma
        self.veloalarma11.delete(0, tk.END)
        self.veloalarma11.insert(0, str(self.velPropagacionAlarma_Tipo5))
        # Propagación espacial
        if (self.modeloEspacial_Tipo5 == 0):
            self.modeloesp11.set("Decaying Exponential")
            self.constante51.set('Alpha')
            self.constante52.set('----')
            self.const111['state'] = 'normal'
            self.const211['state'] = 'disabled'
        else:
            self.modeloesp11.set("Raised-Cosine Window")
            self.constante51.set('W')
            self.constante52.set('dth')
            self.const111['state'] = 'normal'
            self.const211['state'] = 'normal'
        # Constantes de propagación espacial alpha,W,dth
        self.const111.delete(0, tk.END)
        self.const111.insert(0, str(self.constanteEspacial1_Tipo5))
        self.const211.delete(0, tk.END)
        self.const211.insert(0, str(self.constanteEspacial2_Tipo5))

    def leerentradas(self):
        # Variables a modificar
        self.tiempoLimite = float(self.tiemposimulacion.get())  # segundos, tiempo de paro del algoritmo
        self.deltaTiempo = float(self.diftiempo.get())  # segundos , diferencial de tiempo entre iteración
        decimales=Decimal(self.diftiempo.get())
        self.numerosDecimalesDeltaTiempo = -1*(int(decimales.as_tuple().exponent))  # Si se modifica deltaTiempo modificar también esta veriable
        self.radiocelula=float(self.radio00.get())
        if (self.modelodisp00.get() == 'PPP'):
            self.modelodispositivos=0
        else:
            self.modelodispositivos = 1
        self.repeticiones=int(self.repeticiones00.get())

        self.tiposDispositivos = 3  # Cantidad total de dispositivos a caracterizar a continuación

        ### Control de iluminación
        self.dipositivos_Tipo1 = float(self.numero01.get())  # número de dispositivos de tipo 1,
        self.lambdaRegular_Tipo1 = float(self.tasapaquete01.get())  # la tasa lambda para el estado regular de los dispositivos de tipo 1 (1 paquete cada 60 seg)
        self.lambdaAlarma_Tipo1 = float(self.tasaalarma01.get())  # la tasa a la que se producen eventos de alarma para este tipo de dispositivos (1 evento cada 500 seg)
        self.velPropagacionAlarma_Tipo1 = float(self.veloalarma01.get())  # m/s Velocidad de propagación de alarma
        if (self.modeloesp01.get() == 'Decaying Exponential'):
            self.modeloEspacial_Tipo1 = 0  # Propagación espacial de alarma, 0 Decaying exponential 1 raised-cosine Window
        else:
            self.modeloEspacial_Tipo1 = 1
        self.constanteEspacial1_Tipo1 = float(self.const101.get())  # alpha para Decaying exponential, W para raised-cosine Window
        if (self.modeloesp01.get() == 'Raised-Cosine Window'):
            self.constanteEspacial2_Tipo1 = float(self.const201.get())  # ignorar para Decaying exponential, dth para raised-cosine Window
        # animacion
        self.color_Tipo1 = 'b'
        self.marcador_Tipo1 = 'd'

        ### Monitoreo de consumo del agua y electricidad
        self.dipositivos_Tipo2 = float(self.numero02.get())  # número de dispositivos de tipo 2
        self.lambdaRegular_Tipo2 = float(self.tasapaquete02.get())  # la tasa lambda para el estado regular de los dispositivos de tipo 2 (0.5 paquete cada 60 seg)
        self.lambdaAlarma_Tipo2 = float(self.tasaalarma02.get())  # la tasa a la que se producen eventos de alarma para este tipo de dispositivos (1 evento cada 200 seg)
        self.velPropagacionAlarma_Tipo2 = float(self.veloalarma02.get())  # m/s Velocidad de propagación de alarma
        if (self.modeloesp02.get() == 'Decaying Exponential'):
            self.modeloEspacial_Tipo2 = 0  # Propagación espacial de alarma, 0 Decaying exponential 1 raised-cosine Window
        else:
            self.modeloEspacial_Tipo2 = 1
        self.constanteEspacial1_Tipo2 = float(self.const102.get())  # alpha para Decaying exponential, W para raised-cosine Window
        if (self.modeloesp02.get() == 'Raised-Cosine Window'):
            self.constanteEspacial2_Tipo2 = float(self.const202.get())  # ignorar para Decaying exponential, dth para raised-cosine Window
        # animacion
        self.color_Tipo2 = 'r'
        self.marcador_Tipo2 = '*'

        ### Detección de terremotos
        self.dipositivos_Tipo3 = float(self.numero03.get())  # número de dispositivos de tipo 3
        self.lambdaRegular_Tipo3 = float(self.tasapaquete03.get())  # la tasa lambda para el estado regular de los dispositivos de tipo 2 (0.5 paquete cada 60 seg)
        self.lambdaAlarma_Tipo3 = float(self.tasaalarma03.get())   # la tasa a la que se producen eventos de alarma para este tipo de dispositivos (1 evento cada 350 seg)
        self.velPropagacionAlarma_Tipo3 = float(self.veloalarma03.get())  # m/s Velocidad de propagación de alarma
        if (self.modeloesp03.get() == 'Decaying Exponential'):
            self.modeloEspacial_Tipo3 = 0  # Propagación espacial de alarma, 0 Decaying exponential 1 raised-cosine Window
        else:
            self.modeloEspacial_Tipo3 = 1
        self.constanteEspacial1_Tipo3 = float(self.const103.get())  # alpha para Decaying exponential, W para raised-cosine Window
        if (self.modeloesp03.get() == 'Raised-Cosine Window'):
            self.constanteEspacial2_Tipo3 = float(self.const203.get())  # ignorar para Decaying exponential, dth para raised-cosine Window
        # animacion
        self.color_Tipo3 = 'k'
        self.marcador_Tipo3 = '^'

        ### Contaminación del aire
        self.dipositivos_Tipo4 = float(self.numero10.get())  # número de dispositivos de tipo 3
        self.lambdaRegular_Tipo4 = float(self.tasapaquete10.get())  # la tasa lambda para el estado regular de los dispositivos de tipo 2 (0.5 paquete cada 60 seg)
        self.lambdaAlarma_Tipo4 = float(self.tasaalarma10.get())  # la tasa a la que se producen eventos de alarma para este tipo de dispositivos (1 evento cada 350 seg)
        self.velPropagacionAlarma_Tipo4 = float(self.veloalarma10.get()) # m/s Velocidad de propagación de alarma
        if (self.modeloesp10.get() == 'Decaying Exponential'):
            self.modeloEspacial_Tipo4 = 0  # Propagación espacial de alarma, 0 Decaying exponential 1 raised-cosine Window
        else:
            self.modeloEspacial_Tipo4 = 1
        self.constanteEspacial1_Tipo4 = float(self.const110.get())   # alpha para Decaying exponential, W para raised-cosine Window
        if (self.modeloesp10.get() == 'Raised-Cosine Window'):
            self.constanteEspacial2_Tipo4 = float(self.const210.get())  # ignorar para Decaying exponential, dth para raised-cosine Window
        # animacion
        self.color_Tipo4 = 'k'
        self.marcador_Tipo4 = '^'

        ### Control de semáforos
        self.dipositivos_Tipo5 = float(self.numero11.get())  # número de dispositivos de tipo 3
        self.lambdaRegular_Tipo5 = float(self.tasapaquete11.get())  # la tasa lambda para el estado regular de los dispositivos de tipo 2 (0.5 paquete cada 60 seg)
        self.lambdaAlarma_Tipo5 = float(self.tasaalarma11.get())  # la tasa a la que se producen eventos de alarma para este tipo de dispositivos (1 evento cada 350 seg)
        self.velPropagacionAlarma_Tipo5 = float(self.veloalarma11.get())  # m/s Velocidad de propagación de alarma
        if (self.modeloesp11.get() == 'Decaying Exponential'):
            self.modeloEspacial_Tipo5 = 0  # Propagación espacial de alarma, 0 Decaying exponential 1 raised-cosine Window
        else:
            self.modeloEspacial_Tipo5 = 1
        self.constanteEspacial1_Tipo5 = float(self.const111.get())   # alpha para Decaying exponential, W para raised-cosine Window
        if (self.modeloesp11.get() == 'Raised-Cosine Window'):
            self.constanteEspacial2_Tipo5 = float(self.const211.get())  # ignorar para Decaying exponential, dth para raised-cosine Window
        # animacion
        self.color_Tipo5 = 'k'
        self.marcador_Tipo5 = '^'


    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Generación de Tráfico IoT")
        self.master.geometry("1033x430+100+80")
        self.anchocaja1=320
        self.altocaja1=200
        self.create_widgets()

    #--------------funciones para el GUI----------------
    def cambiomodelo1(self, event):
        if(self.modeloesp01.get()=='Decaying Exponential'):
            self.constante11.set('Alpha')
            self.constante12.set('----')
            self.const101['state'] = 'normal'
            self.const101.delete(0, tk.END)
            self.const201.delete(0, tk.END)
            self.const201['state']='disabled'

        elif(self.modeloesp01.get()=='Raised-Cosine Window'):
            self.constante11.set('W')
            self.constante12.set('dth')
            self.const101['state'] = 'normal'
            self.const201['state'] = 'normal'
            self.const101.delete(0, tk.END)
            self.const201.delete(0, tk.END)

    def cambiomodelo2(self, event):
        if (self.modeloesp02.get() == 'Decaying Exponential'):
            self.constante21.set('Alpha')
            self.constante22.set('----')
            self.const102['state'] = 'normal'
            self.const102.delete(0, tk.END)
            self.const202.delete(0, tk.END)
            self.const202['state'] = 'disabled'

        elif (self.modeloesp02.get() == 'Raised-Cosine Window'):
            self.constante21.set('W')
            self.constante22.set('dth')
            self.const102['state'] = 'normal'
            self.const202['state'] = 'normal'
            self.const102.delete(0, tk.END)
            self.const202.delete(0, tk.END)

    def cambiomodelo3(self, event):
        if (self.modeloesp03.get() == 'Decaying Exponential'):
            self.constante31.set('Alpha')
            self.constante32.set('----')
            self.const103['state'] = 'normal'
            self.const103.delete(0, tk.END)
            self.const203.delete(0, tk.END)
            self.const203['state'] = 'disabled'

        elif (self.modeloesp03.get() == 'Raised-Cosine Window'):
            self.constante31.set('W')
            self.constante32.set('dth')
            self.const103['state'] = 'normal'
            self.const203['state'] = 'normal'
            self.const103.delete(0, tk.END)
            self.const203.delete(0, tk.END)

    def cambiomodelo4(self, event):
        if (self.modeloesp10.get() == 'Decaying Exponential'):
            self.constante41.set('Alpha')
            self.constante42.set('----')
            self.const110['state'] = 'normal'
            self.const110.delete(0, tk.END)
            self.const210.delete(0, tk.END)
            self.const210['state'] = 'disabled'
        elif (self.modeloesp10.get() == 'Raised-Cosine Window'):
            self.constante41.set('W')
            self.constante42.set('dth')
            self.const110['state'] = 'normal'
            self.const210['state'] = 'normal'
            self.const110.delete(0, tk.END)
            self.const210.delete(0, tk.END)


    def cambiomodelo5(self, event):
        if (self.modeloesp11.get() == 'Decaying Exponential'):
            self.constante51.set('Alpha')
            self.constante52.set('----')
            self.const111['state'] = 'normal'
            self.const111.delete(0, tk.END)
            self.const211.delete(0, tk.END)
            self.const211['state'] = 'disabled'

        elif (self.modeloesp11.get() == 'Raised-Cosine Window'):
            self.constante51.set('W')
            self.constante52.set('dth')
            self.const111['state'] = 'normal'
            self.const211['state'] = 'normal'
            self.const111.delete(0, tk.END)
            self.const211.delete(0, tk.END)



    def cambiomodelo6(self, event):
        if (self.modeloesp12.get() == 'Decaying Exponential'):
            self.constante61.set('Alpha')
            self.constante62.set('----')
            self.const212['state'] = 'disabled'
        elif (self.modeloesp12.get() == 'Raised-Cosine Window'):
            self.constante61.set('W')
            self.constante62.set('dth')
            self.const212['state'] = 'normal'

    def cambiomodelo7(self, event):
        if (self.modeloesp13.get() == 'Decaying Exponential'):
            self.constante71.set('Alpha')
            self.constante72.set('----')
            self.const213['state'] = 'disabled'
        elif (self.modeloesp13.get() == 'Raised-Cosine Window'):
            self.constante71.set('W')
            self.constante72.set('dth')
            self.const213['state'] = 'normal'

    def cambiomodelodisp(self,event):
        if(self.modelodisp00.get()=='PPP'):
            self.constante13.set('Intensidad')
            self.constante23.set('Intensidad')
            self.constante33.set('Intensidad')
            self.constante43.set('Intensidad')
            self.constante53.set('Intensidad')
            self.constante63.set('Intensidad')
            self.constante73.set('Intensidad')
            self.constante14.set('disp\'s/m^2')
            self.constante24.set('disp\'s/m^2')
            self.constante34.set('disp\'s/m^2')
            self.constante44.set('disp\'s/m^2')
            self.constante54.set('disp\'s/m^2')
            self.constante64.set('disp\'s/m^2')
            self.constante74.set('disp\'s/m^2')
            self.numero01['state'] = 'normal'
            self.numero01.delete(0, tk.END)
            self.numero02['state'] = 'normal'
            self.numero02.delete(0, tk.END)
            self.numero03['state'] = 'normal'
            self.numero03.delete(0, tk.END)
            self.numero10['state'] = 'normal'
            self.numero10.delete(0, tk.END)
            self.numero11['state'] = 'normal'
            self.numero11.delete(0, tk.END)
            self.numero12['state'] = 'normal'
            self.numero12.delete(0, tk.END)
            self.numero13['state'] = 'normal'
            self.numero13.delete(0, tk.END)

        else:
            self.constante13.set('Cantidad')
            self.constante23.set('Cantidad')
            self.constante33.set('Cantidad')
            self.constante43.set('Cantidad')
            self.constante53.set('Cantidad')
            self.constante63.set('Cantidad')
            self.constante73.set('Cantidad')
            self.constante14.set('dispositivos')
            self.constante24.set('dispositivos')
            self.constante34.set('dispositivos')
            self.constante44.set('dispositivos')
            self.constante54.set('dispositivos')
            self.constante64.set('dispositivos')
            self.constante74.set('dispositivos')
            self.numero01['state'] = 'normal'
            self.numero01.delete(0, tk.END)
            self.numero02['state'] = 'normal'
            self.numero02.delete(0, tk.END)
            self.numero03['state'] = 'normal'
            self.numero03.delete(0, tk.END)
            self.numero10['state'] = 'normal'
            self.numero10.delete(0, tk.END)
            self.numero11['state'] = 'normal'
            self.numero11.delete(0, tk.END)
            self.numero12['state'] = 'normal'
            self.numero12.delete(0, tk.END)
            self.numero13['state'] = 'normal'
            self.numero13.delete(0, tk.END)


    def cambiomodelodispresettodo(self):
        if (self.modelodispositivos==0):
            self.constante13.set('Intensidad')
            self.constante23.set('Intensidad')
            self.constante33.set('Intensidad')
            self.constante43.set('Intensidad')
            self.constante53.set('Intensidad')
            self.constante63.set('Intensidad')
            self.constante73.set('Intensidad')
            self.constante14.set('disp\'s/m^2')
            self.constante24.set('disp\'s/m^2')
            self.constante34.set('disp\'s/m^2')
            self.constante44.set('disp\'s/m^2')
            self.constante54.set('disp\'s/m^2')
            self.constante64.set('disp\'s/m^2')
            self.constante74.set('disp\'s/m^2')
            self.numero01['state'] = 'normal'
            self.numero01.delete(0, tk.END)
            self.numero02['state'] = 'normal'
            self.numero02.delete(0, tk.END)
            self.numero03['state'] = 'normal'
            self.numero03.delete(0, tk.END)
            self.numero10['state'] = 'normal'
            self.numero10.delete(0, tk.END)
            self.numero11['state'] = 'normal'
            self.numero11.delete(0, tk.END)
            self.numero12['state'] = 'normal'
            self.numero12.delete(0, tk.END)
            self.numero13['state'] = 'normal'
            self.numero13.delete(0, tk.END)
        else:
            self.constante13.set('Cantidad')
            self.constante23.set('Cantidad')
            self.constante33.set('Cantidad')
            self.constante43.set('Cantidad')
            self.constante53.set('Cantidad')
            self.constante63.set('Cantidad')
            self.constante73.set('Cantidad')
            self.constante14.set('dispositivos')
            self.constante24.set('dispositivos')
            self.constante34.set('dispositivos')
            self.constante44.set('dispositivos')
            self.constante54.set('dispositivos')
            self.constante64.set('dispositivos')
            self.constante74.set('dispositivos')
            self.numero01['state'] = 'normal'
            self.numero01.delete(0, tk.END)
            self.numero02['state'] = 'normal'
            self.numero02.delete(0, tk.END)
            self.numero03['state'] = 'normal'
            self.numero03.delete(0, tk.END)
            self.numero10['state'] = 'normal'
            self.numero10.delete(0, tk.END)
            self.numero11['state'] = 'normal'
            self.numero11.delete(0, tk.END)
            self.numero12['state'] = 'normal'
            self.numero12.delete(0, tk.END)
            self.numero13['state'] = 'normal'
            self.numero13.delete(0, tk.END)



    def create_widgets(self):
        self.upperFrame=tk.Frame(self.master)
        self.upperFrame.grid(row=0,column=0)
        self.middleFrame = tk.Frame(self.master)
        self.middleFrame.grid(row=1, column=0)
        self.bottomFrame = tk.LabelFrame(self.master,text='Generar Tráfico',heigh=50,width=1000,bg='grey',bd=3)
        self.bottomFrame.grid(row=2, column=0)


        self.constante11 = tk.StringVar()
        self.constante12 = tk.StringVar()
        self.constante13 = tk.StringVar()
        self.constante14 = tk.StringVar()
        self.constante21 = tk.StringVar()
        self.constante22 = tk.StringVar()
        self.constante23 = tk.StringVar()
        self.constante24 = tk.StringVar()
        self.constante31 = tk.StringVar()
        self.constante32 = tk.StringVar()
        self.constante33 = tk.StringVar()
        self.constante34 = tk.StringVar()
        self.constante41 = tk.StringVar()
        self.constante42 = tk.StringVar()
        self.constante43 = tk.StringVar()
        self.constante44 = tk.StringVar()
        self.constante51 = tk.StringVar()
        self.constante52 = tk.StringVar()
        self.constante53 = tk.StringVar()
        self.constante54 = tk.StringVar()
        self.constante61 = tk.StringVar()
        self.constante62 = tk.StringVar()
        self.constante63 = tk.StringVar()
        self.constante64 = tk.StringVar()
        self.constante71 = tk.StringVar()
        self.constante72 = tk.StringVar()
        self.constante73 = tk.StringVar()
        self.constante74 = tk.StringVar()


        #----------Opciones Celula---------
        self.frame00 = tk.LabelFrame(self.upperFrame, text='Opciones de Célula', bg='grey', bd=3, heigh=self.altocaja1,
                                     width=self.anchocaja1)
        self.frame00.grid(row=0, column=0, sticky='n' + 's')
        # Radio de la célula
        tk.Label(self.frame00, text='Radio célula:').grid(row=0, column=0, sticky='w' + 'e')
        self.radio00 = tk.Entry(self.frame00, width=8)
        self.radio00.grid(row=0, column=1)
        tk.Label(self.frame00, text='metros').grid(row=0, column=2, sticky='w' + 'e')
        # Modelo de distribución de usuarios
        tk.Label(self.frame00, text='Distribución de usuarios:').grid(row=1, column=0, columnspan=2,sticky='w' + 'e')
        self.modelodisp00 = ttk.Combobox(self.frame00, state="readonly", width=10)
        self.modelodisp00["values"] = ['PPP', 'Uniforme']
        self.modelodisp00.set('Seleccionar')
        self.modelodisp00.bind('<<ComboboxSelected>>', self.cambiomodelodisp)
        self.modelodisp00.grid(row=1, column=2, columnspan=2)
        # Repeticiones
        tk.Label(self.frame00, text='Repetir:').grid(row=2, column=0, sticky='w' + 'e')
        self.repeticiones00 = tk.Entry(self.frame00, width=8)
        self.repeticiones00.grid(row=2, column=1)
        tk.Label(self.frame00, text='veces').grid(row=2, column=2, sticky='w' + 'e')


        #-----------Recuadro de Control de iluminación------------
        self.frame01 = tk.LabelFrame(self.upperFrame, text='Control de iluminación', bg='grey', bd=3, heigh=self.altocaja1, width=self.anchocaja1)
        self.frame01.grid(row=0, column=1,sticky='n' + 's')
        #cantidad de dispositivos
        tk.Label(self.frame01,textvariable=self.constante13).grid(row=0,column=0,sticky='w'+'e')
        self.numero01 = tk.Entry(self.frame01,width=6)
        self.numero01['state'] = 'disabled'
        self.numero01.grid(row=0,column=1)
        tk.Label(self.frame01, textvariable=self.constante14).grid(row=0, column=2, sticky='w' + 'e')
        #tasa de generación de paquetes
        tk.Label(self.frame01, text='Tasa de paquete:').grid(row=1, column=0,sticky='w'+'e')
        self.tasapaquete01 = tk.Entry(self.frame01,width=6)
        self.tasapaquete01.grid(row=1, column=1)
        tk.Label(self.frame01, text='paquetes/seg').grid(row=1, column=2, sticky='w' + 'e')
        #tasa de generación de eventos de alarma
        tk.Label(self.frame01, text='Tasa de alarma:').grid(row=2, column=0,sticky='w'+'e')
        self.tasaalarma01 = tk.Entry(self.frame01,width=6)
        self.tasaalarma01.grid(row=2, column=1)
        tk.Label(self.frame01, text='alarmas/seg').grid(row=2, column=2, sticky='w' + 'e')
        #velocidad de protagación de alarmas
        tk.Label(self.frame01, text='Velocidad alarma:').grid(row=3, column=0, sticky='w' + 'e')
        self.veloalarma01 = tk.Entry(self.frame01,width=6)
        self.veloalarma01.grid(row=3, column=1)
        tk.Label(self.frame01, text='metros/seg').grid(row=3, column=2, sticky='w' + 'e')
        #Modelo de propagación espacial
        tk.Label(self.frame01, text='Propagación espacial:').grid(row=4, column=0, sticky='w' + 'e')
        self.modeloesp01 = ttk.Combobox(self.frame01, state="readonly",width=18)
        self.modeloesp01["values"] = ["Decaying Exponential","Raised-Cosine Window"]
        self.modeloesp01.set("Seleccionar modelo")
        self.modeloesp01.bind('<<ComboboxSelected>>', self.cambiomodelo1)
        self.modeloesp01.grid(row=4,column=1,columnspan=2)
        #Constante modelo 1
        self.const101label = tk.Label(self.frame01, textvariable=self.constante11)
        self.const101label.grid(row=5, column=0, sticky='w' + 'e')
        self.const101= tk.Entry(self.frame01,width=6)
        self.const101['state'] = 'disabled'
        self.const101.grid(row=5, column=1)
        # Constante modelo 2
        self.const201label = tk.Label(self.frame01, textvariable=self.constante12)
        self.const201label.grid(row=6, column=0, sticky='w' + 'e')
        self.const201 = tk.Entry(self.frame01, width=6)
        self.const201['state'] = 'disabled'
        self.const201.grid(row=6, column=1)
        # Boton para cargar datos
        self.botoncarga01 =tk.Button(self.frame01,text='Reset',command=self.reset1)
        self.botoncarga01.grid(row=7,column=0,columnspan=3)

        #---------Consumo de Agua y electricidad-------------
        self.frame02 = tk.LabelFrame(self.upperFrame, text='Consumo de agua y electricidad', bg='grey', bd=3, heigh=self.altocaja1,
                                     width=self.anchocaja1)
        self.frame02.grid(row=0, column=2, sticky='n' + 's')

        # cantidad de dispositivos
        tk.Label(self.frame02, textvariable=self.constante23).grid(row=0, column=0, sticky='w' + 'e')
        self.numero02 = tk.Entry(self.frame02, width=6)
        self.numero02['state'] = 'disabled'
        self.numero02.grid(row=0, column=1)
        tk.Label(self.frame02, textvariable=self.constante24).grid(row=0, column=2, sticky='w' + 'e')
        # tasa de generación de paquetes
        tk.Label(self.frame02, text='Tasa de paquete:').grid(row=1, column=0, sticky='w' + 'e')
        self.tasapaquete02 = tk.Entry(self.frame02, width=6)
        self.tasapaquete02.grid(row=1, column=1)
        tk.Label(self.frame02, text='paquetes/seg').grid(row=1, column=2, sticky='w' + 'e')
        # tasa de generación de eventos de alarma
        tk.Label(self.frame02, text='Tasa de alarma:').grid(row=2, column=0, sticky='w' + 'e')
        self.tasaalarma02 = tk.Entry(self.frame02, width=6)
        self.tasaalarma02.grid(row=2, column=1)
        tk.Label(self.frame02, text='alarmas/seg').grid(row=2, column=2, sticky='w' + 'e')
        # velocidad de protagación de alarmas
        tk.Label(self.frame02, text='Velocidad alarma:').grid(row=3, column=0, sticky='w' + 'e')
        self.veloalarma02 = tk.Entry(self.frame02, width=6)
        self.veloalarma02.grid(row=3, column=1)
        tk.Label(self.frame02, text='metros/seg').grid(row=3, column=2, sticky='w' + 'e')
        # Modelo de propagación espacial
        tk.Label(self.frame02, text='Propagación espacial:').grid(row=4, column=0, sticky='w' + 'e')
        self.modeloesp02 = ttk.Combobox(self.frame02, state="readonly", width=18)
        self.modeloesp02["values"] = ["Decaying Exponential", "Raised-Cosine Window"]
        self.modeloesp02.set("Seleccionar modelo")
        self.modeloesp02.bind('<<ComboboxSelected>>', self.cambiomodelo2)
        self.modeloesp02.grid(row=4, column=1, columnspan=2)
        # Constante modelo 1
        self.const102label = tk.Label(self.frame02, textvariable=self.constante21)
        self.const102label.grid(row=5, column=0, sticky='w' + 'e')
        self.const102 = tk.Entry(self.frame02, width=6)
        self.const102['state'] = 'disabled'
        self.const102.grid(row=5, column=1)
        # Constante modelo 2
        self.const202label = tk.Label(self.frame02, textvariable=self.constante22)
        self.const202label.grid(row=6, column=0, sticky='w' + 'e')
        self.const202 = tk.Entry(self.frame02, width=6)
        self.const202['state'] = 'disabled'
        self.const202.grid(row=6, column=1)
        # Boton para cargar datos
        self.botoncarga02 = tk.Button(self.frame02, text='Reset',command=self.reset2)
        self.botoncarga02.grid(row=7, column=0, columnspan=3)

        #------- Deteccción de terremotos-------------
        self.frame03 = tk.LabelFrame(self.upperFrame, text='Detección de terremotos', bg='grey', bd=3, heigh=self.altocaja1,
                                     width=self.anchocaja1)
        self.frame03.grid(row=0, column=3,sticky='n' + 's')

        # cantidad de dispositivos
        tk.Label(self.frame03, textvariable=self.constante33).grid(row=0, column=0, sticky='w' + 'e')
        self.numero03 = tk.Entry(self.frame03, width=6)
        self.numero03['state'] = 'disabled'
        self.numero03.grid(row=0, column=1)
        tk.Label(self.frame03, textvariable=self.constante34).grid(row=0, column=2, sticky='w' + 'e')
        # tasa de generación de paquetes
        tk.Label(self.frame03, text='Tasa de paquete:').grid(row=1, column=0, sticky='w' + 'e')
        self.tasapaquete03 = tk.Entry(self.frame03, width=6)
        self.tasapaquete03.grid(row=1, column=1)
        tk.Label(self.frame03, text='paquetes/seg').grid(row=1, column=2, sticky='w' + 'e')
        # tasa de generación de eventos de alarma
        tk.Label(self.frame03, text='Tasa de alarma:').grid(row=2, column=0, sticky='w' + 'e')
        self.tasaalarma03 = tk.Entry(self.frame03, width=6)
        self.tasaalarma03.grid(row=2, column=1)
        tk.Label(self.frame03, text='alarmas/seg').grid(row=2, column=2, sticky='w' + 'e')
        # velocidad de protagación de alarmas
        tk.Label(self.frame03, text='Velocidad alarma:').grid(row=3, column=0, sticky='w' + 'e')
        self.veloalarma03 = tk.Entry(self.frame03, width=6)
        self.veloalarma03.grid(row=3, column=1)
        tk.Label(self.frame03, text='metros/seg').grid(row=3, column=2, sticky='w' + 'e')
        # Modelo de propagación espacial
        tk.Label(self.frame03, text='Propagación espacial:').grid(row=4, column=0, sticky='w' + 'e')
        self.modeloesp03 = ttk.Combobox(self.frame03, state="readonly", width=18)
        self.modeloesp03["values"] = ["Decaying Exponential", "Raised-Cosine Window"]
        self.modeloesp03.set("Seleccionar modelo")
        self.modeloesp03.bind('<<ComboboxSelected>>', self.cambiomodelo3)
        self.modeloesp03.grid(row=4, column=1, columnspan=2)
        # Constante modelo 1
        self.const103label = tk.Label(self.frame03, textvariable=self.constante31)
        self.const103label.grid(row=5, column=0, sticky='w' + 'e')
        self.const103 = tk.Entry(self.frame03, width=6)
        self.const103['state'] = 'disabled'
        self.const103.grid(row=5, column=1)
        # Constante modelo 2
        self.const203label = tk.Label(self.frame03, textvariable=self.constante32)
        self.const203label.grid(row=6, column=0, sticky='w' + 'e')
        self.const203 = tk.Entry(self.frame03, width=6)
        self.const203['state'] = 'disabled'
        self.const203.grid(row=6, column=1)
        # Boton para cargar datos
        self.botoncarga03 = tk.Button(self.frame03, text='Reset',command=self.reset3)
        self.botoncarga03.grid(row=7, column=0, columnspan=3)

        #------------ Contaminación del aire -------------
        self.frame10 = tk.LabelFrame(self.middleFrame, text='Contaminación del aire', bg='grey', bd=3, heigh=self.altocaja1, width=self.anchocaja1)
        self.frame10.grid(row=0, column=0,sticky='n' + 's')

        # cantidad de dispositivos
        tk.Label(self.frame10, textvariable=self.constante43).grid(row=0, column=0, sticky='w' + 'e')
        self.numero10 = tk.Entry(self.frame10, width=6)
        self.numero10['state'] = 'disabled'
        self.numero10.grid(row=0, column=1)
        tk.Label(self.frame10, textvariable=self.constante44).grid(row=0, column=2, sticky='w' + 'e')
        # tasa de generación de paquetes
        tk.Label(self.frame10, text='Tasa de paquete:').grid(row=1, column=0, sticky='w' + 'e')
        self.tasapaquete10 = tk.Entry(self.frame10, width=6)
        self.tasapaquete10.grid(row=1, column=1)
        tk.Label(self.frame10, text='paquetes/seg').grid(row=1, column=2, sticky='w' + 'e')
        # tasa de generación de eventos de alarma
        tk.Label(self.frame10, text='Tasa de alarma:').grid(row=2, column=0, sticky='w' + 'e')
        self.tasaalarma10 = tk.Entry(self.frame10, width=6)
        self.tasaalarma10.grid(row=2, column=1)
        tk.Label(self.frame10, text='alarmas/seg').grid(row=2, column=2, sticky='w' + 'e')
        # velocidad de protagación de alarmas
        tk.Label(self.frame10, text='Velocidad alarma:').grid(row=3, column=0, sticky='w' + 'e')
        self.veloalarma10 = tk.Entry(self.frame10, width=6)
        self.veloalarma10.grid(row=3, column=1)
        tk.Label(self.frame10, text='metros/seg').grid(row=3, column=2, sticky='w' + 'e')
        # Modelo de propagación espacial
        tk.Label(self.frame10, text='Propagación espacial:').grid(row=4, column=0, sticky='w' + 'e')
        self.modeloesp10 = ttk.Combobox(self.frame10, state="readonly", width=18)
        self.modeloesp10["values"] = ["Decaying Exponential", "Raised-Cosine Window"]
        self.modeloesp10.set("Seleccionar modelo")
        self.modeloesp10.bind('<<ComboboxSelected>>', self.cambiomodelo4)
        self.modeloesp10.grid(row=4, column=1, columnspan=2)
        # Constante modelo 1
        self.const110label = tk.Label(self.frame10, textvariable=self.constante41)
        self.const110label.grid(row=5, column=0, sticky='w' + 'e')
        self.const110 = tk.Entry(self.frame10, width=6)
        self.const110['state']='disabled'
        self.const110.grid(row=5, column=1)
        # Constante modelo 2
        self.const210label = tk.Label(self.frame10, textvariable=self.constante42)
        self.const210label.grid(row=6, column=0, sticky='w' + 'e')
        self.const210 = tk.Entry(self.frame10, width=6)
        self.const210['state']='disabled'
        self.const210.grid(row=6, column=1)
        # Boton para cargar datos
        self.botoncarga10 = tk.Button(self.frame10, text='Reset',command=self.reset4)
        self.botoncarga10.grid(row=7, column=0, columnspan=3)

        #------------- Control de Semáforos ----------
        self.frame11 = tk.LabelFrame(self.middleFrame, text='Control de semáforos', bg='grey', bd=3, heigh=self.altocaja1,
                                     width=self.anchocaja1)
        self.frame11.grid(row=0, column=1,sticky='n' + 's')

        # cantidad de dispositivos
        tk.Label(self.frame11, textvariable=self.constante53).grid(row=0, column=0, sticky='w' + 'e')
        self.numero11 = tk.Entry(self.frame11, width=6)
        self.numero11['state'] = 'disabled'
        self.numero11.grid(row=0, column=1)
        tk.Label(self.frame11, textvariable=self.constante54).grid(row=0, column=2, sticky='w' + 'e')
        # tasa de generación de paquetes
        tk.Label(self.frame11, text='Tasa de paquete:').grid(row=1, column=0, sticky='w' + 'e')
        self.tasapaquete11 = tk.Entry(self.frame11, width=6)
        self.tasapaquete11.grid(row=1, column=1)
        tk.Label(self.frame11, text='paquetes/seg').grid(row=1, column=2, sticky='w' + 'e')
        # tasa de generación de eventos de alarma
        tk.Label(self.frame11, text='Tasa de alarma:').grid(row=2, column=0, sticky='w' + 'e')
        self.tasaalarma11 = tk.Entry(self.frame11, width=6)
        self.tasaalarma11.grid(row=2, column=1)
        tk.Label(self.frame11, text='alarmas/seg').grid(row=2, column=2, sticky='w' + 'e')
        # velocidad de protagación de alarmas
        tk.Label(self.frame11, text='Velocidad alarma:').grid(row=3, column=0, sticky='w' + 'e')
        self.veloalarma11 = tk.Entry(self.frame11, width=6)
        self.veloalarma11.grid(row=3, column=1)
        tk.Label(self.frame11, text='metros/seg').grid(row=3, column=2, sticky='w' + 'e')
        # Modelo de propagación espacial
        tk.Label(self.frame11, text='Propagación espacial:').grid(row=4, column=0, sticky='w' + 'e')
        self.modeloesp11 = ttk.Combobox(self.frame11, state="readonly", width=18)
        self.modeloesp11["values"] = ["Decaying Exponential", "Raised-Cosine Window"]
        self.modeloesp11.set("Seleccionar modelo")
        self.modeloesp11.bind('<<ComboboxSelected>>', self.cambiomodelo5)
        self.modeloesp11.grid(row=4, column=1, columnspan=2)
        # Constante modelo 1
        self.const111label = tk.Label(self.frame11, textvariable=self.constante51)
        self.const111label.grid(row=5, column=0, sticky='w' + 'e')
        self.const111 = tk.Entry(self.frame11, width=6)
        self.const111['state']='disabled'
        self.const111.grid(row=5, column=1)
        # Constante modelo 2
        self.const211label = tk.Label(self.frame11, textvariable=self.constante52)
        self.const211label.grid(row=6, column=0, sticky='w' + 'e')
        self.const211 = tk.Entry(self.frame11, width=6)
        self.const211['state'] = 'disabled'
        self.const211.grid(row=6, column=1)
        # Boton para cargar datos
        self.botoncarga11 = tk.Button(self.frame11, text='Reset',command=self.reset5)
        self.botoncarga11.grid(row=7, column=0, columnspan=3)

        #---------Otros dispositivos mMTC
        self.frame12 = tk.LabelFrame(self.middleFrame, text='Otros dispositivos mMTC', bg='grey', bd=3, heigh=self.altocaja1,
                                     width=self.anchocaja1)
        self.frame12.grid(row=0, column=2,sticky='n' + 's')

        # cantidad de dispositivos
        tk.Label(self.frame12, textvariable=self.constante63).grid(row=0, column=0, sticky='w' + 'e')
        self.numero12 = tk.Entry(self.frame12, width=6)
        self.numero12['state'] = 'disabled'
        self.numero12.grid(row=0, column=1)
        tk.Label(self.frame12, textvariable=self.constante64).grid(row=0, column=2, sticky='w' + 'e')
        # tasa de generación de paquetes
        tk.Label(self.frame12, text='Tasa de paquete:').grid(row=1, column=0, sticky='w' + 'e')
        self.tasapaquete12 = tk.Entry(self.frame12, width=6)
        self.tasapaquete12.grid(row=1, column=1)
        tk.Label(self.frame12, text='paquetes/seg').grid(row=1, column=2, sticky='w' + 'e')
        # tasa de generación de eventos de alarma
        tk.Label(self.frame12, text='Tasa de alarma:').grid(row=2, column=0, sticky='w' + 'e')
        self.tasaalarma12 = tk.Entry(self.frame12, width=6)
        self.tasaalarma12.grid(row=2, column=1)
        tk.Label(self.frame12, text='alarmas/seg').grid(row=2, column=2, sticky='w' + 'e')
        # velocidad de protagación de alarmas
        tk.Label(self.frame12, text='Velocidad alarma:').grid(row=3, column=0, sticky='w' + 'e')
        self.veloalarma12 = tk.Entry(self.frame12, width=6)
        self.veloalarma12.grid(row=3, column=1)
        tk.Label(self.frame12, text='metros/seg').grid(row=3, column=2, sticky='w' + 'e')
        # Modelo de propagación espacial
        tk.Label(self.frame12, text='Propagación espacial:').grid(row=4, column=0, sticky='w' + 'e')
        self.modeloesp12 = ttk.Combobox(self.frame12, state="readonly", width=18)
        self.modeloesp12["values"] = ["Decaying Exponential", "Raised-Cosine Window"]
        self.modeloesp12.set("Decaying Exponential")
        self.modeloesp12.bind('<<ComboboxSelected>>', self.cambiomodelo6)
        self.modeloesp12.grid(row=4, column=1, columnspan=2)
        # Constante modelo 1
        self.const112label = tk.Label(self.frame12, textvariable=self.constante61)
        self.const112label.grid(row=5, column=0, sticky='w' + 'e')
        self.const112 = tk.Entry(self.frame12, width=6)
        self.const112.grid(row=5, column=1)
        # Constante modelo 2
        self.const212label = tk.Label(self.frame12, textvariable=self.constante62)
        self.const212label.grid(row=6, column=0, sticky='w' + 'e')
        self.const212 = tk.Entry(self.frame12, width=6)
        self.const212.grid(row=6, column=1)
        # Boton para cargar datos
        self.botoncarga12 = tk.Button(self.frame12, text='Reset')
        self.botoncarga12.grid(row=7, column=0, columnspan=3)

        #----------Dispositivos URLLC-------------
        self.frame13 = tk.LabelFrame(self.middleFrame, text='Dispositivos URLLC', bg='grey', bd=3, heigh=self.altocaja1,
                                     width=self.anchocaja1)
        self.frame13.grid(row=0, column=3,sticky='n' + 's')

        # cantidad de dispositivos
        tk.Label(self.frame13, textvariable=self.constante73).grid(row=0, column=0, sticky='w' + 'e')
        self.numero13 = tk.Entry(self.frame13, width=6)
        self.numero13['state'] = 'disabled'
        self.numero13.grid(row=0, column=1)
        tk.Label(self.frame13, textvariable=self.constante74).grid(row=0, column=2, sticky='w' + 'e')
        # tasa de generación de paquetes
        tk.Label(self.frame13, text='Tasa de paquete:').grid(row=1, column=0, sticky='w' + 'e')
        self.tasapaquete13 = tk.Entry(self.frame13, width=6)
        self.tasapaquete13.grid(row=1, column=1)
        tk.Label(self.frame13, text='paquetes/seg').grid(row=1, column=2, sticky='w' + 'e')
        # tasa de generación de eventos de alarma
        tk.Label(self.frame13, text='Tasa de alarma:').grid(row=2, column=0, sticky='w' + 'e')
        self.tasaalarma13 = tk.Entry(self.frame13, width=6)
        self.tasaalarma13.grid(row=2, column=1)
        tk.Label(self.frame13, text='alarmas/seg').grid(row=2, column=2, sticky='w' + 'e')
        # velocidad de protagación de alarmas
        tk.Label(self.frame13, text='Velocidad alarma:').grid(row=3, column=0, sticky='w' + 'e')
        self.veloalarma13 = tk.Entry(self.frame13, width=6)
        self.veloalarma13.grid(row=3, column=1)
        tk.Label(self.frame13, text='metros/seg').grid(row=3, column=2, sticky='w' + 'e')
        # Modelo de propagación espacial
        tk.Label(self.frame13, text='Propagación espacial:').grid(row=4, column=0, sticky='w' + 'e')
        self.modeloesp13 = ttk.Combobox(self.frame13, state="readonly", width=18)
        self.modeloesp13["values"] = ["Decaying Exponential", "Raised-Cosine Window"]
        self.modeloesp13.set("Decaying Exponential")
        self.modeloesp13.bind('<<ComboboxSelected>>', self.cambiomodelo7)
        self.modeloesp13.grid(row=4, column=1, columnspan=2)
        # Constante modelo 1
        self.const113label = tk.Label(self.frame13, textvariable=self.constante71)
        self.const113label.grid(row=5, column=0, sticky='w' + 'e')
        self.const113 = tk.Entry(self.frame13, width=6)
        self.const113.grid(row=5, column=1)
        # Constante modelo 2
        self.const213label = tk.Label(self.frame13, textvariable=self.constante72)
        self.const213label.grid(row=6, column=0, sticky='w' + 'e')
        self.const213 = tk.Entry(self.frame13, width=6)
        self.const213.grid(row=6, column=1)
        # Boton para cargar datos
        self.botoncarga13 = tk.Button(self.frame13, text='Reset')
        self.botoncarga13.grid(row=7, column=0, columnspan=3)

        # ----------Iniciar Script-------------
        # tiempo de simulación
        tk.Label(self.bottomFrame, text='Generar por (seg):').grid(row=0, column=0, sticky='w' + 'e')
        self.tiemposimulacion = tk.Entry(self.bottomFrame, width=6)
        self.tiemposimulacion.grid(row=0, column=1)

        # diferencial de tiempo
        tk.Label(self.bottomFrame, text='Diferencial de tiempo (ms):').grid(row=0, column=3, sticky='w' + 'e')
        self.diftiempo = tk.Entry(self.bottomFrame, width=6)
        self.diftiempo.grid(row=0, column=4)

        # Boton para cargar datos
        self.cargardatos = tk.Button(self.bottomFrame, text='Cargar Datos', command=self.resetTodo)
        self.cargardatos.grid(row=0, column=5)

        # Boton para iniciar script
        self.botoniniciar = tk.Button(self.bottomFrame, text='Iniciar Rutina', command=self.rutinaCMMPP)
        self.botoniniciar.grid(row=0, column=6)

    def rutinaCMMPP(self):
        self.leerentradas()
        ######################################################
        #TODO Checar por qué se generan cada vez archivos más grandes .cvs
        
        # # Inicialización de parámetros y variables
        # self.tiempo = 0  # tiempo inicial
        # self.iteraciones = int(self.tiempoLimite / self.deltaTiempo)  # las iteraciones  que se producirán recorriendo el tiempo k
        # self.dispositivos = []  # una lista para guardar las instancias de dipoitivos de distintos tipos
        # self.generadoresAlarmas = []  # una lista para guardar los genradores de eventos de alarmas, uno para cada tipo de dispositivo
        # self.nuevaAlarma = [False] * self.tiposDispositivos
        #
        #
        # # Se generan las instancias de cada tipo de dipositivos y sus generadores de alarmas
        # self.dispositivos.append(
        #     creardispositivos(self.dipositivos_Tipo1, self.lambdaRegular_Tipo1, 'Control de iluminacion', self.tiempo, self.color_Tipo1,
        #                       self.marcador_Tipo1))
        # self.generadoresAlarmas.append(
        #     GeneradorAlarmas(self.lambdaAlarma_Tipo1, self.velPropagacionAlarma_Tipo1, self.tiempo, self.modeloEspacial_Tipo1,
        #                      self.constanteEspacial1_Tipo1, self.constanteEspacial2_Tipo1, [0, 0]))
        # self.dispositivos.append(
        #     creardispositivos(self.dipositivos_Tipo2, self.lambdaRegular_Tipo2, 'Monitoreo de agua y electricidad', self.tiempo,
        #                       self.color_Tipo2, self.marcador_Tipo2))
        # self.generadoresAlarmas.append(
        #     GeneradorAlarmas(self.lambdaAlarma_Tipo2, self.velPropagacionAlarma_Tipo2, self.tiempo, self.modeloEspacial_Tipo2,
        #                      self.constanteEspacial1_Tipo2, self.constanteEspacial2_Tipo2, [0, 0]))
        # self.dispositivos.append(
        #     creardispositivos(self.dipositivos_Tipo3, self.lambdaRegular_Tipo3, 'Deteccion de terremotos', self.tiempo, self.color_Tipo3,
        #                       self.marcador_Tipo3))
        # self.generadoresAlarmas.append(
        #     GeneradorAlarmas(self.lambdaAlarma_Tipo3, self.velPropagacionAlarma_Tipo3, self.tiempo, self.modeloEspacial_Tipo3,
        #                      self.constanteEspacial1_Tipo3, self.constanteEspacial2_Tipo3, [0, 0]))
        #
        # for self.k in range(0, int(self.iteraciones + 1)):  # Ciclo que avanza el tiempo
        #
        #     for self.dispositivosaux, self.generadorAlarma, self.tipoDisp in iter.zip_longest(self.dispositivos, self.generadoresAlarmas,
        #                                                                        range(0,
        #                                                                              self.dispositivos.__len__())):  # Ciclo que recorre los distintos tipos de dispositivos y sus geenradores de alarmas
        #
        #         if (self.tiempo == 0):
        #             self.nuevaAlarma[self.tipoDisp] = self.generadorAlarma.generarAlarma(
        #                 self.tiempo)  # se calcula el primer tiempo de alarma
        #
        #         for self.dispositivo in self.dispositivosaux:  # Ciclo que recorre cada uno de los dispositivos del mismo tipo
        #
        #             self.dispositivo.registrarAlarma(self.generadorAlarma.idAlarma, self.generadorAlarma.siguienteArribo, (
        #                         self.generadorAlarma.siguienteArribo + (distanciaList(self.dispositivo.posicion,
        #                                                                          self.generadorAlarma.posicion) / self.generadorAlarma.velocidad))[
        #                 0], self.generadorAlarma.posicion, self.nuevaAlarma[self.tipoDisp])
        #
        #             [self.listaPnk, self.nuevaListaAlarmas] = calcularPnk(self.tiempo, self.dispositivo.listaAlarmas,
        #                                                         self.generadorAlarma.velocidad,
        #                                                         self.generadorAlarma.modeloEspacial,
        #                                                         self.generadorAlarma.constanteEspacial1,
        #                                                         self.generadorAlarma.constanteEspacial2, self.dispositivo.m_Pu,
        #                                                         self.dispositivo.m_Pc,
        #                                                         self.deltaTiempo)  # parte A del diagrama  /assets/CMMPP_diagrama.jpg
        #
        #             # listaAlarmas=[idAlarma,tiempoAparicion,tiempoLLegada,posicionAlarma,self.posicion] esta es la forma de listaAlarmas
        #             for self.pnk, self.listaAlarmas in iter.zip_longest(self.listaPnk, self.dispositivo.listaAlarmas):
        #                 self.dispositivo.actualizarestado(self.pnk)  # parte B del diagrama
        #                 self.dispositivo.generararribo(self.tiempo, self.listaAlarmas[0], self.listaAlarmas[2],
        #                                           self.numerosDecimalesDeltaTiempo)  # parte C del diagrama
        #                 self.dispositivo.actualizarestadoanormal()  # por si hay más de un evento que cree estados de alarma, se cambia siempre a estado normal,
        #
        #             self.dispositivo.actualizarListaAlarmas(self.nuevaListaAlarmas)
        #
        #         self.nuevaAlarma[self.tipoDisp] = self.generadorAlarma.generarAlarma(
        #             self.tiempo)  # se genera una nueva alarma en una posición aleatoria si la actual ya sucedió
        #
        #     self.tiempo = round(self.tiempo + self.deltaTiempo, self.numerosDecimalesDeltaTiempo)  # Función para redondear decimales
        areaCelula = np.pi * self.radiocelula ** 2  # area de la célula
        # Iniciamos la creación de dispositivos según la distribución seleccionada
        # Dispositivos tipo 1
        if (self.modelodispositivos == 0):
            cantidad_Tipo1 = np.random.poisson(self.dipositivos_Tipo1 * areaCelula)  # Poisson número de dispoitivos de tipo1
        else:
            cantidad_Tipo1 = self.dipositivos_Tipo1  # si no se trata de un PPP se generarán los dispositivos especifiados
        theta_Tipo1 = 2 * np.pi * np.random.uniform(0, 1, cantidad_Tipo1)
        rho_Tipo1 = self.radiocelula * np.sqrt(np.random.uniform(0, 1, cantidad_Tipo1))
        # Convertimos las coordenadas polares a cartesianas
        xx_Tipo1 = rho_Tipo1 * np.cos(theta_Tipo1)
        yy_Tipo1 = rho_Tipo1 * np.sin(theta_Tipo1)
        posiciones_Tipo1 = [xx_Tipo1,
                            yy_Tipo1]  # Esta lista se usará para asignar posiciones a los dispositivos que se crearán
        # Dispositivos tipo 2
        if (self.modelodispositivos == 0):
            cantidad_Tipo2 = np.random.poisson(self.dipositivos_Tipo2 * areaCelula)  # Poisson número de dispoitivos de tipo1
        else:
            cantidad_Tipo2 = self.dipositivos_Tipo2  # si no se trata de un PPP se generarán los dispositivos especifiados
        theta_Tipo2 = 2 * np.pi * np.random.uniform(0, 1, cantidad_Tipo2)
        rho_Tipo2 = self.radiocelula * np.sqrt(np.random.uniform(0, 1, cantidad_Tipo2))
        # Convertimos las coordenadas polares a cartesianas
        xx_Tipo2 = rho_Tipo2 * np.cos(theta_Tipo2)
        yy_Tipo2 = rho_Tipo2 * np.sin(theta_Tipo2)
        posiciones_Tipo2 = [xx_Tipo2,
                            yy_Tipo2]  # Esta lista se usará para asignar posiciones a los dispositivos que se crearán
        # Dispositivos tipo 3
        if (self.modelodispositivos == 0):
            cantidad_Tipo3 = np.random.poisson(self.dipositivos_Tipo3 * areaCelula)  # Poisson número de dispoitivos de tipo1
        else:
            cantidad_Tipo3 = self.dipositivos_Tipo3  # si no se trata de un PPP se generarán los dispositivos especifiados
        theta_Tipo3 = 2 * np.pi * np.random.uniform(0, 1, cantidad_Tipo3)
        rho_Tipo3 = self.radiocelula * np.sqrt(np.random.uniform(0, 1, cantidad_Tipo3))
        # Convertimos las coordenadas polares a cartesianas
        xx_Tipo3 = rho_Tipo3 * np.cos(theta_Tipo3)
        yy_Tipo3 = rho_Tipo3 * np.sin(theta_Tipo3)
        posiciones_Tipo3 = [xx_Tipo3,
                            yy_Tipo3]  # Esta lista se usará para asignar posiciones a los dispositivos que se crearán

        tiempo = 0  # tiempo inicial
        iteraciones = self.tiempoLimite / self.deltaTiempo  # las iteraciones  que se producirán recorriendo el tiempo k
        self.dispositivos = []  # una lista para guardar las instancias de dipoitivos de distintos tipos
        generadoresAlarmas = []  # una lista para guardar los genradores de eventos de alarmas, uno para cada tipo de dispositivo
        nuevaAlarma = [False] * self.tiposDispositivos
        # animacionTrafico= AnimacionTrafico() # Creamos animación y la dibujamos
        # animacionTrafico.dibujar()
        # animacionTrafico.actualizar()

        # Se generan las instancias de cada tipo de dipositivos y sus generadores de alarmas
        self.dispositivos.append(
            creardispositivos(cantidad_Tipo1, posiciones_Tipo1, self.lambdaRegular_Tipo1, 'Control de iluminacion', tiempo,
                              self.color_Tipo1, self.marcador_Tipo1))
        generadoresAlarmas.append(
            GeneradorAlarmas(self.lambdaAlarma_Tipo1, self.velPropagacionAlarma_Tipo1, tiempo, self.modeloEspacial_Tipo1,
                             self.constanteEspacial1_Tipo1, self.constanteEspacial2_Tipo1, [0, 0]))
        self.dispositivos.append(
            creardispositivos(cantidad_Tipo2, posiciones_Tipo2, self.lambdaRegular_Tipo2, 'Monitoreo de agua y electricidad',
                              tiempo, self.color_Tipo2, self.marcador_Tipo2))
        generadoresAlarmas.append(
            GeneradorAlarmas(self.lambdaAlarma_Tipo2, self.velPropagacionAlarma_Tipo2, tiempo, self.modeloEspacial_Tipo2,
                             self.constanteEspacial1_Tipo2, self.constanteEspacial2_Tipo2, [0, 0]))
        self.dispositivos.append(
            creardispositivos(cantidad_Tipo3, posiciones_Tipo3, self.lambdaRegular_Tipo3, 'Deteccion de terremotos', tiempo,
                              self.color_Tipo3, self.marcador_Tipo3))
        generadoresAlarmas.append(
            GeneradorAlarmas(self.lambdaAlarma_Tipo3, self.velPropagacionAlarma_Tipo3, tiempo, self.modeloEspacial_Tipo3,
                             self.constanteEspacial1_Tipo3, self.constanteEspacial2_Tipo3, [0, 0]))

        ##########  Algoritmo CMMPP  #################

        for k in range(0, int(iteraciones + 1)):  # Ciclo que avanza el tiempo

            for dispositivosaux, generadorAlarma, tipoDisp in iter.zip_longest(self.dispositivos, generadoresAlarmas,
                                                                               range(0,
                                                                                     self.dispositivos.__len__())):  # Ciclo que recorre los distintos tipos de dispositivos y sus geenradores de alarmas

                if (tiempo == 0):
                    nuevaAlarma[tipoDisp] = generadorAlarma.generarAlarma(tiempo,
                                                                          self.radiocelula)  # se calcula el primer tiempo de alarma

                for dispositivo in dispositivosaux:  # Ciclo que recorre cada uno de los dispositivos del mismo tipo

                    dispositivo.registrarAlarma(generadorAlarma.idAlarma, generadorAlarma.siguienteArribo, (
                                generadorAlarma.siguienteArribo + (distanciaList(dispositivo.posicion,
                                                                                 generadorAlarma.posicion) / generadorAlarma.velocidad))[
                        0], generadorAlarma.posicion, nuevaAlarma[tipoDisp])

                    [listaPnk, nuevaListaAlarmas] = calcularPnk(tiempo, dispositivo.listaAlarmas,
                                                                generadorAlarma.velocidad,
                                                                generadorAlarma.modeloEspacial,
                                                                generadorAlarma.constanteEspacial1,
                                                                generadorAlarma.constanteEspacial2, dispositivo.m_Pu,
                                                                dispositivo.m_Pc,
                                                                self.deltaTiempo)  # parte A del diagrama  /assets/CMMPP_diagrama.jpg

                    # listaAlarmas=[idAlarma,tiempoAparicion,tiempoLLegada,posicionAlarma,self.posicion] esta es la forma de listaAlarmas
                    for pnk, listaAlarmas in iter.zip_longest(listaPnk, dispositivo.listaAlarmas):
                        dispositivo.actualizarestado(pnk)  # parte B del diagrama
                        dispositivo.generararribo(tiempo, listaAlarmas[0], listaAlarmas[2],
                                                  self.numerosDecimalesDeltaTiempo)  # parte C del diagrama
                        dispositivo.actualizarestadoanormal()  # por si hay más de un evento que cree estados de alarma, se cambia siempre a estado normal,

                    dispositivo.actualizarListaAlarmas(nuevaListaAlarmas)

                nuevaAlarma[tipoDisp] = generadorAlarma.generarAlarma(tiempo,
                                                                      self.radiocelula)  # se genera una nueva alarma en una posición aleatoria si la actual ya sucedió

            tiempo = round(tiempo + self.deltaTiempo, self.numerosDecimalesDeltaTiempo)  # Función para redondear decimales

        def takeSecond(elem):
            return elem[1]
        arriboOrdenado = dispositivo.registroCompletoArribos.sort(key=takeSecond) # Ordenamos los arribos por tiempo

        # Registro de todos los eventos
        self.ListaEventos = dispositivo.registroCompletoArribos
        # Creación de un Dataframe apartir de una lista
        df_eventos = pd.DataFrame(self.ListaEventos)
        # Guardado de datos en archivo con extensión .csv
        df_eventos.to_csv("ArchivoEventos.csv")

        print('Fin de Rutina')



root = tk.Tk()
app = Application(master=root)
app.mainloop()