import numpy as np  # NumPy package for arrays, random number generation, etc


class GeneradorAlarmas(object):

    # Definición de constructor
    def __init__(self, lambdaEvento,velocidad,tiempoInicial, modeloEspacial,constanteEspacial1,constanteEspacial2,posicion):
        self.lambdaEvento=lambdaEvento # tasa de generacion de eventos de alarma
        self.velocidad=velocidad #velocidad de propagación de los eventos de alarma
        self.siguienteArribo=tiempoInicial #debe ser inicializado al tiempo inicial de la simulación
        self.modeloEspacial=modeloEspacial # 0 para modelo decaying exponential,  1 para raised-cosine window
        self.constanteEspacial1=constanteEspacial1 # alpha para modelo decaying exponential, W para raised-cosine window
        self.constanteEspacial2=constanteEspacial2 # dth para raised-cosine window, nada para dacaying exponential
        self.posicion = posicion  # la posición espacial dentro de la celula


#TODO Hay un problema y todos los eventos se crean mass o menos al mismo tiempo sin importar lass distintas lambdas
    def calcularSiguienteAlarma(self): #Calcular en qué momento sucederá la siguiente alarma
        tiempoEspera = np.random.exponential(1 / (self.lambdaEvento), 1)  # el siguiente arribo se producirá segun una varible exponencial
        self.siguienteArribo=self.siguienteArribo + tiempoEspera
        #TODO crear funcion para generar posicion en la célula
        self.posicion=[np.random.uniform(0, 100, 1)-50, np.random.uniform(0, 100, 1)-50] # se calcula la posicion

    def generarAlarma(self,tiempoActual):

        if(self.siguienteArribo <= tiempoActual): # Si ya sucedió la última alarma calcular una nueva
            self.calcularSiguienteAlarma()


