import matplotlib.pyplot as plt  # for plotting

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
