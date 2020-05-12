import numpy as np  # NumPy package for arrays, random number generation, etc


class DeviceMTC(object):
    # Definición de constructor
    def __init__(self, lambdareg, Xpos, Ypos, estado,tipo):
        self.lambdareg = lambdareg
        self.posicion = [Xpos, Ypos] # la posición espacial dentro de la celula
        self.estado = estado # estado regular o de alarma (0 es regular y 1 alarma)
        self.tipo=tipo # tipo de dispositivo

    matriz_Pu = [[1, 1], [0, 0]]  # matriz que describe el comportamiento no unsincronized
    m_Pu = np.array(matriz_Pu)
    matriz_Pc = [[0, 1], [1, 0]]  # matriz que describe el comportamiento sincronized
    m_Pc = np.array(matriz_Pc)
    matriz_Pnk = []  # matriz de probabilidad de transición entre estados Pn[k]= Theta_n[k]*Pc + (1-Theta_n[k]*Pu)

    def calcular_Pnk(self, theta):
        thetank=theta*self.calcular_delta_n() # thetank= theta[k] * delta_n = Theta_n[k]
        return (1 - thetank) * self.m_Pu + thetank * self.m_Pc #Pn[k]= Theta_n[k]*Pc + (1-Theta_n[k]*Pu)

    def actualizarestado(self, pnk):
        auxUniforme = np.random.uniform(0, 1, 1)
        if self.estado==1 and auxUniforme > self.pnk[1][1]: # Si se está en estado alarma y si la variable uniforme es mayor a la probabilidad de que no cambie de estado, cambia de estado
            self.estado=0
        if self.estado==0 and auxUniforme > self.pnk[0][0]: # Si se está en estado normal y si la variable uniforme es mayor a la probabilidad de que no cambie de estado, cambia de estado
            self.estado=1

    def calcular_delta_n(self): #TODO: checar la distribución para el cálculo de delta_n
        return np.random.normal(0.5,0.16,1) #variable aleatoria normal para delta_n

    #TODO: función para registrar petición en una lista y un archivo de texto