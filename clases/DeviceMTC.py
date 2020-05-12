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

    #TODO: función para registrar petición en una lista y un archivo de texto