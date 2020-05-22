import numpy as np  # NumPy package for arrays, random number generation, etc


class DeviceMTC(object):
    # Definición de constructor
    def __init__(self, lambdareg, Xpos, Ypos, estado, tipo,tiempoInicial,identificador, registroArribos, tamañopkt):
        self.lambdareg = lambdareg
        self.posicion = [Xpos, Ypos]  # la posición espacial dentro de la celula
        self.estado = estado  # estado regular o de alarma (0 es regular y 1 alarma)
        self.tipo = tipo  # tipo de dispositivo
        self.tiempoArribo = tiempoInicial # siguiente instante en el que se realizará una petición, debe iniciarse con el tiempo inicial
        self.identificador = identificador
        self.registroArribos = registroArribos
        self.tamañopkt = tamañopkt


    matriz_Pu = [[1, 1], [0, 0]]  # matriz que describe el comportamiento no unsincronized
    m_Pu = np.array(matriz_Pu)
    matriz_Pc = [[0, 1], [1, 0]]  # matriz que describe el comportamiento sincronized
    m_Pc = np.array(matriz_Pc)
    #matriz_Pnk = []  # matriz de probabilidad de transición entre estados Pn[k]= Theta_n[k]*Pc + (1-Theta_n[k]*Pu)
    registroCompletoArribos = []  # El conglomerado de arribos del estado normal y del de alarma
    cuentaAlarmas = 0  # Contador que registra las veces que se estuvo en estado de alarma

    def calcular_Pnk(self, theta):
        thetank = theta * self.calcular_delta_n()  # thetank= theta[k] * delta_n = Theta_n[k]
        return (1 - thetank) * self.m_Pu + thetank * self.m_Pc  # Pn[k]= Theta_n[k]*Pc + (1-Theta_n[k]*Pu)

    def actualizarestado(self, pnk):
        auxUniforme = np.random.uniform(0, 1, 1)
        if self.estado == 1 and auxUniforme > pnk[1][1]:  # Si se está en estado alarma y si la variable uniforme es mayor a la probabilidad de que no cambie de estado, cambia de estado
            self.estado = 0
        if self.estado == 0 and auxUniforme > pnk[0][0]:  # Si se está en estado normal y si la variable uniforme es mayor a la probabilidad de que no cambie de estado, cambia de estado
            self.estado = 1

    def generararribo(self, tiempo):
        if self.estado == 1:  # alarma
            self.generarpaquetealarma() # tamaño fijo parte D del diagrama  /assets/CMMPP_diagrama.jpg
            self.generararriboalarma(tiempo)  # Generar exactamente 1 paquete

        elif self.tiempoArribo <= tiempo:
            self.generarpaquetenormal() # variable de pareto parte D del diagrama  /assets/CMMPP_diagrama.jpg
            self.generararribonormal()  # Generar un paquete en caso de que no exista ya uno

    def generararriboalarma(self, tiempo):
        self.registroArribos.append([tiempo,self.tipo,self.identificador,self.estado,self.tamañopkt])  # se registra el arribo en la lista
        self.registroCompletoArribos.append([tiempo,self.tipo,self.identificador,self.estado,self.tamañopkt])
        self.cuentaAlarmas = self.cuentaAlarmas + 1 #¿QUE FUNCION TIENE ESTE CONTADOR?

    def generararribonormal(self):
        tiempoEspera = np.random.exponential(1 / (self.lambdareg),1)  # el siguiente arribo se producirá segun una varible exponencial
        self.tiempoArribo = self.tiempoArribo + tiempoEspera
        self.registroArribos.append([int(self.tiempoArribo), self.tipo,self.identificador,self.estado,self.tamañopkt])  # se registra el arribo en la lista
        self.registroCompletoArribos.append([int(self.tiempoArribo), self.tipo,self.identificador,self.estado, self.tamañopkt])

    def calcular_delta_n(self):  # TODO: checar la distribución para el cálculo de delta_n
        return np.random.normal(0.5, 0.16, 1)  # variable aleatoria normal para delta_n

    def generarpaquetenormal(self):
        while True:
            lower = 20  # the lower bound for your values
            shape = 1  # the distribution shape parameter, also known as `a` or `alpha`
            size = 1  # the size of your sample (number of random values)
            x = np.random.pareto(shape, size) + lower
            upper = x
            if upper<=200:
                break
        self.tamañopkt=x

    def generarpaquetealarma(self):
        self.tamañopkt=20

    # TODO: función para registrar petición en una lista y un archivo de texto, junto con el tamaño del paquete y otra información del dispositivo
