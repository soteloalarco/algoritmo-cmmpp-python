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
        self.master.geometry("1000x550+200+80")
        self.anchocaja1=250
        self.altocaja1=250
        self.create_widgets()

    def create_widgets(self):
        self.upperFrame=tk.Frame(self.master)
        self.upperFrame.grid(row=0,column=0)
        self.middleFrame = tk.Frame(self.master)
        self.middleFrame.grid(row=1, column=0)
        self.bottomFrame = tk.LabelFrame(self.master,text='Generar Tráfico',heigh=50,width=1000,bg='grey',bd=3)
        self.bottomFrame.grid(row=2, column=0)

        self.frame00=tk.LabelFrame(self.upperFrame, text='Opciones de Célula',bg='grey', bd=3, heigh=self.altocaja1, width=self.anchocaja1)
        self.frame00.grid(row=0, column=0)

        #Recuadro de Control de iluminación
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
        tk.Label(self.frame01, text='paquete/seg').grid(row=1, column=2, sticky='w' + 'e')
        #tasa de generación de eventos de alarma
        tk.Label(self.frame01, text='Tasa de alarma:').grid(row=2, column=0,sticky='w'+'e')
        self.tasaalarma01 = tk.Entry(self.frame01,width=6)
        self.tasaalarma01.grid(row=2, column=1)
        tk.Label(self.frame01, text='alarma/seg').grid(row=2, column=2, sticky='w' + 'e')
        #velocidad de protagación de alarmas
        tk.Label(self.frame01, text='Velocidad alarma:').grid(row=3, column=0, sticky='w' + 'e')
        self.veloalarma01 = tk.Entry(self.frame01,width=6)
        self.veloalarma01.grid(row=3, column=1)
        tk.Label(self.frame01, text='metros/seg').grid(row=3, column=2, sticky='w' + 'e')
        #Modelo de propagación espacial
        tk.Label(self.frame01, text='Propagación espacial:').grid(row=4, column=0, sticky='w' + 'e')
        self.modeloesp01 = ttk.Combobox(self.frame01, state="readonly")
        self.modeloesp01.grid(row=4,column=1,columnspan=2)

        self.frame02 = tk.LabelFrame(self.upperFrame, text='Consumo de agua y electricidad', bg='grey', bd=3, heigh=self.altocaja1,
                                     width=self.anchocaja1)
        self.frame02.grid(row=0, column=2)

        self.frame03 = tk.LabelFrame(self.upperFrame, text='Detección de terremotos', bg='grey', bd=3, heigh=self.altocaja1,
                                     width=self.anchocaja1)
        self.frame03.grid(row=0, column=3)

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