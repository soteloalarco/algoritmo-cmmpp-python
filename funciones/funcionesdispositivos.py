import numpy as np  # NumPy package for arrays, random number generation, etc
from clases.DeviceMTC import DeviceMTC


def creardispositivos( numeroDispositivos, lambdaRegular_Tipo,tipo,tiempo):
    dispositivos = []
    for disp in range(0, numeroDispositivos):  # Generamos la cantidad indicada de dispositivos de tipo 1
        # TODO: crear una función para asignar la posición en la célula
        dispositivos.append(
            DeviceMTC(lambdaRegular_Tipo, np.random.uniform(0, 100, 1), np.random.uniform(0, 100, 1), 0,tipo,tiempo,disp,[],0))

    return dispositivos
