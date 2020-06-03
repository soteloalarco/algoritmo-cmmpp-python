import tkinter as tk
from tkinter import ttk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Generación de Tráfico IoT")
        self.master.geometry("1207x455+100+80")
        self.anchocaja1=250
        self.altocaja1=200
        self.create_widgets()

    def modified(self,event):
        if(self.modeloesp01.get()=='Decaying Exponential'):
            self.constante11.set('Alpha')
            self.constante12.set('----')
            self.const201['state']='disabled'
        elif(self.modeloesp01.get()=='Raised-Cosine Window'):
            self.constante11.set('W')
            self.constante12.set('dth')
            self.const201['state'] = 'normal'
        if (self.modeloesp02.get() == 'Decaying Exponential'):
            self.constante21.set('Alpha')
            self.constante22.set('----')
            self.const202['state'] = 'disabled'
        elif (self.modeloesp02.get() == 'Raised-Cosine Window'):
            self.constante21.set('W')
            self.constante22.set('dth')
            self.const202['state'] = 'normal'
        if (self.modeloesp03.get() == 'Decaying Exponential'):
            self.constante31.set('Alpha')
            self.constante32.set('----')
            self.const203['state'] = 'disabled'
        elif (self.modeloesp03.get() == 'Raised-Cosine Window'):
            self.constante31.set('W')
            self.constante32.set('dth')
            self.const203['state'] = 'normal'
        if (self.modeloesp10.get() == 'Decaying Exponential'):
            self.constante41.set('Alpha')
            self.constante42.set('----')
            self.const210['state'] = 'disabled'
        elif (self.modeloesp10.get() == 'Raised-Cosine Window'):
            self.constante41.set('W')
            self.constante42.set('dth')
            self.const210['state'] = 'normal'
        if (self.modeloesp11.get() == 'Decaying Exponential'):
            self.constante51.set('Alpha')
            self.constante52.set('----')
            self.const211['state'] = 'disabled'
        elif (self.modeloesp11.get() == 'Raised-Cosine Window'):
            self.constante51.set('W')
            self.constante52.set('dth')
            self.const211['state'] = 'normal'
        if (self.modeloesp12.get() == 'Decaying Exponential'):
            self.constante61.set('Alpha')
            self.constante62.set('----')
            self.const212['state'] = 'disabled'
        elif (self.modeloesp12.get() == 'Raised-Cosine Window'):
            self.constante61.set('W')
            self.constante62.set('dth')
            self.const212['state'] = 'normal'
        if (self.modeloesp13.get() == 'Decaying Exponential'):
            self.constante71.set('Alpha')
            self.constante72.set('----')
            self.const213['state'] = 'disabled'
        elif (self.modeloesp13.get() == 'Raised-Cosine Window'):
            self.constante71.set('W')
            self.constante72.set('dth')
            self.const213['state'] = 'normal'

    def create_widgets(self):
        self.upperFrame=tk.Frame(self.master)
        self.upperFrame.grid(row=0,column=0)
        self.middleFrame = tk.Frame(self.master)
        self.middleFrame.grid(row=1, column=0)
        self.bottomFrame = tk.LabelFrame(self.master,text='Generar Tráfico',heigh=50,width=1000,bg='grey',bd=3)
        self.bottomFrame.grid(row=2, column=0)

        self.frame00=tk.LabelFrame(self.upperFrame, text='Opciones de Célula',bg='grey', bd=3, heigh=self.altocaja1, width=self.anchocaja1)
        self.frame00.grid(row=0, column=0,sticky='n' + 's')

        self.constante11 = tk.StringVar()
        self.constante12 = tk.StringVar()
        self.constante21 = tk.StringVar()
        self.constante22 = tk.StringVar()
        self.constante31 = tk.StringVar()
        self.constante32 = tk.StringVar()
        self.constante41 = tk.StringVar()
        self.constante42 = tk.StringVar()
        self.constante51 = tk.StringVar()
        self.constante52 = tk.StringVar()
        self.constante61 = tk.StringVar()
        self.constante62 = tk.StringVar()
        self.constante71 = tk.StringVar()
        self.constante72 = tk.StringVar()

        #----------Opciones Celula---------
        tk.Label(self.frame00, text='Forma y demás de la célula').grid(row=0, column=0, sticky='w' + 'e')

        #-----------Recuadro de Control de iluminación------------
        self.frame01 = tk.LabelFrame(self.upperFrame, text='Control de iluminación', bg='grey', bd=3, heigh=self.altocaja1, width=self.anchocaja1)
        self.frame01.grid(row=0, column=1,sticky='n' + 's')
        #cantidad de dispositivos
        tk.Label(self.frame01,text='Cantidad:').grid(row=0,column=0,sticky='w'+'e')
        self.numero01 = tk.Entry(self.frame01,width=6)
        self.numero01.grid(row=0,column=1)
        tk.Label(self.frame01, text='dispositivos').grid(row=0, column=2, sticky='w' + 'e')
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
        self.modeloesp01.set("Decaying Exponential")
        self.modeloesp01.bind('<<ComboboxSelected>>', self.modified)
        self.modeloesp01.grid(row=4,column=1,columnspan=2)
        #Constante modelo 1
        self.const101label = tk.Label(self.frame01, textvariable=self.constante11)
        self.const101label.grid(row=5, column=0, sticky='w' + 'e')
        self.const101= tk.Entry(self.frame01,width=6)
        self.const101.grid(row=5, column=1)
        # Constante modelo 2
        self.const201label = tk.Label(self.frame01, textvariable=self.constante12)
        self.const201label.grid(row=6, column=0, sticky='w' + 'e')
        self.const201 = tk.Entry(self.frame01, width=6)
        self.const201.grid(row=6, column=1)
        # Boton para cargar datos
        self.botoncarga01 =tk.Button(self.frame01,text='Reset')
        self.botoncarga01.grid(row=7,column=0,columnspan=3)

        #---------Consumo de Agua y electricidad-------------
        self.frame02 = tk.LabelFrame(self.upperFrame, text='Consumo de agua y electricidad', bg='grey', bd=3, heigh=self.altocaja1,
                                     width=self.anchocaja1)
        self.frame02.grid(row=0, column=2, sticky='n' + 's')

        # cantidad de dispositivos
        tk.Label(self.frame02, text='Cantidad:').grid(row=0, column=0, sticky='w' + 'e')
        self.numero02 = tk.Entry(self.frame02, width=6)
        self.numero02.grid(row=0, column=1)
        tk.Label(self.frame02, text='dispositivos').grid(row=0, column=2, sticky='w' + 'e')
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
        self.modeloesp02.set("Decaying Exponential")
        self.modeloesp02.bind('<<ComboboxSelected>>', self.modified)
        self.modeloesp02.grid(row=4, column=1, columnspan=2)
        # Constante modelo 1
        self.const102label = tk.Label(self.frame02, textvariable=self.constante21)
        self.const102label.grid(row=5, column=0, sticky='w' + 'e')
        self.const102 = tk.Entry(self.frame02, width=6)
        self.const102.grid(row=5, column=1)
        # Constante modelo 2
        self.const202label = tk.Label(self.frame02, textvariable=self.constante22)
        self.const202label.grid(row=6, column=0, sticky='w' + 'e')
        self.const202 = tk.Entry(self.frame02, width=6)
        self.const202.grid(row=6, column=1)
        # Boton para cargar datos
        self.botoncarga02 = tk.Button(self.frame02, text='Reset')
        self.botoncarga02.grid(row=7, column=0, columnspan=3)

        #------- Deteccción de terremotos-------------
        self.frame03 = tk.LabelFrame(self.upperFrame, text='Detección de terremotos', bg='grey', bd=3, heigh=self.altocaja1,
                                     width=self.anchocaja1)
        self.frame03.grid(row=0, column=3,sticky='n' + 's')

        # cantidad de dispositivos
        tk.Label(self.frame03, text='Cantidad:').grid(row=0, column=0, sticky='w' + 'e')
        self.numero03 = tk.Entry(self.frame03, width=6)
        self.numero03.grid(row=0, column=1)
        tk.Label(self.frame03, text='dispositivos').grid(row=0, column=2, sticky='w' + 'e')
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
        self.modeloesp03.set("Decaying Exponential")
        self.modeloesp03.bind('<<ComboboxSelected>>', self.modified)
        self.modeloesp03.grid(row=4, column=1, columnspan=2)
        # Constante modelo 1
        self.const103label = tk.Label(self.frame03, textvariable=self.constante31)
        self.const103label.grid(row=5, column=0, sticky='w' + 'e')
        self.const103 = tk.Entry(self.frame03, width=6)
        self.const103.grid(row=5, column=1)
        # Constante modelo 2
        self.const203label = tk.Label(self.frame03, textvariable=self.constante32)
        self.const203label.grid(row=6, column=0, sticky='w' + 'e')
        self.const203 = tk.Entry(self.frame03, width=6)
        self.const203.grid(row=6, column=1)
        # Boton para cargar datos
        self.botoncarga03 = tk.Button(self.frame03, text='Reset')
        self.botoncarga03.grid(row=7, column=0, columnspan=3)

        #------------ Contaminación del aire -------------
        self.frame10 = tk.LabelFrame(self.middleFrame, text='Contaminación del aire', bg='grey', bd=3, heigh=self.altocaja1, width=self.anchocaja1)
        self.frame10.grid(row=0, column=0,sticky='n' + 's')

        # cantidad de dispositivos
        tk.Label(self.frame10, text='Cantidad:').grid(row=0, column=0, sticky='w' + 'e')
        self.numero10 = tk.Entry(self.frame10, width=6)
        self.numero10.grid(row=0, column=1)
        tk.Label(self.frame10, text='dispositivos').grid(row=0, column=2, sticky='w' + 'e')
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
        self.modeloesp10.set("Decaying Exponential")
        self.modeloesp10.bind('<<ComboboxSelected>>', self.modified)
        self.modeloesp10.grid(row=4, column=1, columnspan=2)
        # Constante modelo 1
        self.const110label = tk.Label(self.frame10, textvariable=self.constante41)
        self.const110label.grid(row=5, column=0, sticky='w' + 'e')
        self.const110 = tk.Entry(self.frame10, width=6)
        self.const110.grid(row=5, column=1)
        # Constante modelo 2
        self.const210label = tk.Label(self.frame10, textvariable=self.constante42)
        self.const210label.grid(row=6, column=0, sticky='w' + 'e')
        self.const210 = tk.Entry(self.frame10, width=6)
        self.const210.grid(row=6, column=1)
        # Boton para cargar datos
        self.botoncarga10 = tk.Button(self.frame10, text='Reset')
        self.botoncarga10.grid(row=7, column=0, columnspan=3)

        #------------- Control de Semáforos ----------
        self.frame11 = tk.LabelFrame(self.middleFrame, text='Control de semáforos', bg='grey', bd=3, heigh=self.altocaja1,
                                     width=self.anchocaja1)
        self.frame11.grid(row=0, column=1,sticky='n' + 's')

        # cantidad de dispositivos
        tk.Label(self.frame11, text='Cantidad:').grid(row=0, column=0, sticky='w' + 'e')
        self.numero11 = tk.Entry(self.frame11, width=6)
        self.numero11.grid(row=0, column=1)
        tk.Label(self.frame11, text='dispositivos').grid(row=0, column=2, sticky='w' + 'e')
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
        self.modeloesp11.set("Decaying Exponential")
        self.modeloesp11.bind('<<ComboboxSelected>>', self.modified)
        self.modeloesp11.grid(row=4, column=1, columnspan=2)
        # Constante modelo 1
        self.const111label = tk.Label(self.frame11, textvariable=self.constante51)
        self.const111label.grid(row=5, column=0, sticky='w' + 'e')
        self.const111 = tk.Entry(self.frame11, width=6)
        self.const111.grid(row=5, column=1)
        # Constante modelo 2
        self.const211label = tk.Label(self.frame11, textvariable=self.constante52)
        self.const211label.grid(row=6, column=0, sticky='w' + 'e')
        self.const211 = tk.Entry(self.frame11, width=6)
        self.const211.grid(row=6, column=1)
        # Boton para cargar datos
        self.botoncarga11 = tk.Button(self.frame11, text='Reset')
        self.botoncarga11.grid(row=7, column=0, columnspan=3)

        #---------Otros dispositivos mMTC
        self.frame12 = tk.LabelFrame(self.middleFrame, text='Otros dispositivos mMTC', bg='grey', bd=3, heigh=self.altocaja1,
                                     width=self.anchocaja1)
        self.frame12.grid(row=0, column=2,sticky='n' + 's')

        # cantidad de dispositivos
        tk.Label(self.frame12, text='Cantidad:').grid(row=0, column=0, sticky='w' + 'e')
        self.numero12 = tk.Entry(self.frame12, width=6)
        self.numero12.grid(row=0, column=1)
        tk.Label(self.frame12, text='dispositivos').grid(row=0, column=2, sticky='w' + 'e')
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
        self.modeloesp12.bind('<<ComboboxSelected>>', self.modified)
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
        tk.Label(self.frame13, text='Cantidad:').grid(row=0, column=0, sticky='w' + 'e')
        self.numero13 = tk.Entry(self.frame13, width=6)
        self.numero13.grid(row=0, column=1)
        tk.Label(self.frame13, text='dispositivos').grid(row=0, column=2, sticky='w' + 'e')
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
        self.modeloesp13.bind('<<ComboboxSelected>>', self.modified)
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
        self.cargardatos = tk.Button(self.bottomFrame, text='Cargar Datos')
        self.cargardatos.grid(row=0, column=5)

        # Boton para iniciar script
        self.botoniniciar = tk.Button(self.bottomFrame, text='Iniciar Rutina')
        self.botoniniciar.grid(row=0, column=6)

root = tk.Tk()
app = Application(master=root)
app.mainloop()