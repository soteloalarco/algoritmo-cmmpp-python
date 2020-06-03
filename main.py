#from tkinter import *
#import tkinter as tk

# root=Tk()
# root.title("Generación de Tráfico IoT")
# #to print screen size
# screen_width=root.winfo_screenwidth()
# screen_height=root.winfo_screenheight()
# print("Screen width:",screen_width)
# print("Screen height:",screen_height)
# #resize tkinter window 400x200 and place at position (150,150)
# root.geometry("400x200+150+150")
#
# #create main menu bar
# menu_bar=Menu(root)
# #create the submenu, tearoff indicates that menu can pop out
# fileMenu=Menu(menu_bar,tearoff=0)
# #add commands to submenu
# fileMenu.add_command(label="stop",command=root.destroy)
# fileMenu.add_command(label="kill",command=root.destroy)
# fileMenu.add_command(label="exit",command=root.destroy)
# #add the file drop menu down sub-menu in the main menu bar
# menu_bar.add_cascade(label="File",menu=fileMenu)
# root.config(menu=menu_bar)
#
# #labels con colores
# label=Label(root,text='Inicialización de Dispositivos')
# #label.config(foreground='yellow')
# label.pack()
#
# #exit window will close GUI window when clicked
# exitButton=Button(root,text='Exit program',command=root.destroy)
# exitButton.pack()
# #to write a message on the screen
# def my_callback():
#     print("you clicked the button....")
# msg_button=Button(root,text='click here',command=my_callback)
# msg_button.pack()
#
# #create empty box
# entry =Entry(root)
# entry.pack()
# #print the contents of entry box in a console
# def printMsg():
#     print(entry.get())
# #create a button,when clicked will print the contents of the entry box
# button=Button(root,text='print content',command=printMsg)
# button.pack()
#
# root.mainloop()

# root = tk.Tk()
# #Frames en la fila superior
# upperframe = tk.Frame(root)
# upperframe.pack(side=TOP)
#
#
# frame11= tk.Frame(upperframe,bg='white',height='100',width='50')
# frame11.pack(side = LEFT)
# label=Label(frame11,text='Caracteŕisticas de la célula')
# label.pack()
#
# frame12= tk.Frame(upperframe,bg='blue',height='100',width='50')
# frame12.pack(side = LEFT)
# frame13= tk.Frame(upperframe,bg='green',height='100',width='50')
# frame13.pack(side = LEFT)
#
# #Frames en la fila inferior
# bottomframe = Frame(root)
# bottomframe.pack( side = BOTTOM )
#
# text = tk.Entry(frame11, width=10)
# text.pack()
# self.hi_there = tk.Button(self.upperFrame)
# self.hi_there["text"] = "Hello World\n(click me)"
# self.hi_there["command"] = self.say_hi
# self.hi_there.grid(row=0, column=1)
#
# self.quit = tk.Button(self.bottomFrame, text="QUIT", fg="red",
#                       command=self.master.destroy)
# self.quit.grid(row=0, column=0)
#
#
# def say_hi(self):
#     print("hi there, everyone!")


import tkinter as tk
from tkinter import ttk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Generación de Tráfico IoT")
        self.master.geometry("1153x455+200+80")
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
            self.const202['state'] = 'disabled'
        elif (self.modeloesp03.get() == 'Raised-Cosine Window'):
            self.constante31.set('W')
            self.constante32.set('dth')
            self.const202['state'] = 'normal'

    def create_widgets(self):
        self.upperFrame=tk.Frame(self.master)
        self.upperFrame.grid(row=0,column=0)
        self.middleFrame = tk.Frame(self.master)
        self.middleFrame.grid(row=1, column=0)
        self.bottomFrame = tk.LabelFrame(self.master,text='Generar Tráfico',heigh=50,width=1000,bg='grey',bd=3)
        self.bottomFrame.grid(row=2, column=0)

        self.frame00=tk.LabelFrame(self.upperFrame, text='Opciones de Célula',bg='grey', bd=3, heigh=self.altocaja1, width=self.anchocaja1)
        self.frame00.grid(row=0, column=0)

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
        self.frame10.grid(row=0, column=0)

        self.frame11 = tk.LabelFrame(self.middleFrame, text='Control de semáforos', bg='grey', bd=3, heigh=self.altocaja1,
                                     width=self.anchocaja1)
        self.frame11.grid(row=0, column=1)

        self.frame12 = tk.LabelFrame(self.middleFrame, text='Otros dispositivos mMTC', bg='grey', bd=3, heigh=self.altocaja1,
                                     width=self.anchocaja1)
        self.frame12.grid(row=0, column=2)

        self.frame13 = tk.LabelFrame(self.middleFrame, text='Dispositivos URLLC', bg='grey', bd=3, heigh=self.altocaja1,
                                     width=self.anchocaja1)
        self.frame13.grid(row=0, column=3)


root = tk.Tk()
app = Application(master=root)
app.mainloop()