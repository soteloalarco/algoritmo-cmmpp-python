import matplotlib.pyplot as plt  # for plotting
from clases.TiposDispositivos import TiposDispositivos

def graficardispositivos(dispositivosTodos,radio):
    fig, ax = plt.subplots(1, 1)
    # Graficando en el círculo
    xx = [dispositivo[2] for dispositivo in dispositivosTodos]
    yy = [dispositivo[3] for dispositivo in dispositivosTodos]
    ax.scatter(xx, yy, edgecolor='b', facecolor='b', alpha=0.5, marker=".")
    ax.scatter(0,0, s=10, edgecolors="k", facecolor='k', marker="1")
    titulo="Ubicación de "+ str(len(dispositivosTodos)) +" UEs. Célula de radio= "+ str(radio) + " m"
    plt.title(titulo)
    plt.ylabel('Eje vertical')
    plt.xlabel('Eje Horizontal')
    plt.axis('equal')


def histogramatodoseventos(ListaEventos, bins,tiempofinal):
    fig, ax2 = plt.subplots(1, 1)

    tiempoEvento= [evento[1] for evento in ListaEventos]

    ax2.hist(tiempoEvento, density=False, range=(0,tiempofinal), bins=bins+1  ) #rwidth=1 range=(0,tiempofinal)
    plt.title("Histograma de eventos en el tiempo, todos los UEs")
    plt.ylabel('Eventos')
    plt.xlabel('Tiempo')
    plt.axhline()

def graficareventosportipodispositivo(ListaEventos, bins,tiempofinal):

    fig1=plt.figure()
    ax11 = fig1.add_subplot(121)
    ax12 = fig1.add_subplot(122)
    fig2 = plt.figure()
    ax21 = fig2.add_subplot(121)
    ax22 = fig2.add_subplot(122)
    fig3 = plt.figure()
    ax31 = fig3.add_subplot(121)
    ax32 = fig3.add_subplot(122)
    fig4 = plt.figure()
    ax41 = fig4.add_subplot(121)
    ax42 = fig4.add_subplot(122)
    fig5 = plt.figure()
    ax51 = fig5.add_subplot(121)
    ax52 = fig5.add_subplot(122)
    fig6 = plt.figure()
    ax61 = fig6.add_subplot(121)
    ax62 = fig6.add_subplot(122)
    fig7 = plt.figure()
    ax71 = fig7.add_subplot(121)
    ax72 = fig7.add_subplot(122)

    dispTipo1 = []
    dispTipo2 = []
    dispTipo3 = []
    dispTipo4 = []
    dispTipo5 = []
    dispTipo6 = []
    dispTipo7 = []
    for dispositivo in ListaEventos:
        if dispositivo[3] == TiposDispositivos.TIPO1:
            dispTipo1.append(dispositivo[1])
        elif dispositivo[3] == TiposDispositivos.TIPO2:
            dispTipo2.append(dispositivo[1])
        elif dispositivo[3] == TiposDispositivos.TIPO3:
            dispTipo3.append(dispositivo[1])
        elif dispositivo[3] == TiposDispositivos.TIPO4:
            dispTipo4.append(dispositivo[1])
        elif dispositivo[3] == TiposDispositivos.TIPO5:
            dispTipo5.append(dispositivo[1])
        elif dispositivo[3] == TiposDispositivos.TIPO6:
            dispTipo6.append(dispositivo[1])
        elif dispositivo[3] == TiposDispositivos.TIPO7:
            dispTipo7.append(dispositivo[1])

    ax11.hist(dispTipo1, label='paquetes',density=False, range=(0, tiempofinal), bins=bins + 1)
    ax11.legend(loc='upper right')
    fig1.canvas.set_window_title(TiposDispositivos.TIPO1)
    titulo = "Histograma de eventos en el tiempo"
    ax11.title.set_text(titulo)
    ax11.set_ylabel('Eventos')
    ax11.set_xlabel('Tiempo')

    ax21.hist(dispTipo2, label='paquetes', density=False, range=(0, tiempofinal), bins=bins + 1)
    ax21.legend(loc='upper right')
    fig2.canvas.set_window_title(TiposDispositivos.TIPO2)
    titulo = "Histograma de eventos en el tiempo"
    ax21.title.set_text(titulo)
    ax21.set_ylabel('Eventos')
    ax21.set_xlabel('Tiempo')

    ax31.hist(dispTipo3, label='paquetes', density=False, range=(0, tiempofinal), bins=bins + 1)
    ax31.legend(loc='upper right')
    fig3.canvas.set_window_title(TiposDispositivos.TIPO3)
    titulo = "Histograma de eventos en el tiempo"
    ax31.title.set_text(titulo)
    ax31.set_ylabel('Eventos')
    ax31.set_xlabel('Tiempo')

    ax41.hist(dispTipo4, label='paquetes', density=False, range=(0, tiempofinal), bins=bins + 1)
    ax41.legend(loc='upper right')
    fig4.canvas.set_window_title(TiposDispositivos.TIPO4)
    titulo = "Histograma de eventos en el tiempo"
    ax41.title.set_text(titulo)
    ax41.set_ylabel('Eventos')
    ax41.set_xlabel('Tiempo')

    ax51.hist(dispTipo5, label='paquetes', density=False, range=(0, tiempofinal), bins=bins + 1)
    ax51.legend(loc='upper right')
    fig5.canvas.set_window_title(TiposDispositivos.TIPO5)
    titulo = "Histograma de eventos en el tiempo"
    ax51.title.set_text(titulo)
    ax51.set_ylabel('Eventos')
    ax51.set_xlabel('Tiempo')

    ax61.hist(dispTipo6, label='paquetes', density=False, range=(0, tiempofinal), bins=bins + 1)
    ax61.legend(loc='upper right')
    fig6.canvas.set_window_title(TiposDispositivos.TIPO6)
    titulo = "Histograma de eventos en el tiempo"
    ax61.title.set_text(titulo)
    ax61.set_ylabel('Eventos')
    ax61.set_xlabel('Tiempo')

    ax71.hist(dispTipo7, label='paquetes', density=False, range=(0, tiempofinal), bins=bins + 1)
    ax71.legend(loc='upper right')
    fig7.canvas.set_window_title(TiposDispositivos.TIPO7)
    titulo = "Histograma de eventos en el tiempo"
    ax71.title.set_text(titulo)
    ax71.set_ylabel('Eventos')
    ax71.set_xlabel('Tiempo')