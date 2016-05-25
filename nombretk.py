from tkinter import *
import time

#VENTANA PRINCIPAL
ventanaN=Tk()  
ventanaN.title('Nombre') 
ventanaN.config(bg="AliceBlue") #color fondo
ventanaN.geometry("680x440+0+0")
variable_string=StringVar()

c = Canvas(ventanaN,width=680,height=440) 
c.pack()


fondo= PhotoImage(file="NOMBRESQ.gif")
c.create_image(0,0,image= fondo, anchor = NW)


#cajaT.grid(row=1,column=1)

NOMBREBOT= PhotoImage(file='NOMBRESQBOT.gif')


def iniciarJuego():
    nombre=cajaT.get()
    ventanaN.destroy()
    import PINBALL
    PINBALL.iniciar(nombre)
    

botonNombre= Button(ventanaN, text="Nombre",command=iniciarJuego,image=NOMBREBOT,relief=FLAT,bg='green').place(x=50, y=50)
cajaT=Entry(ventanaN,textvariable=variable_string)
cajaT.place(x=175,y=92)
#canvas.create_window((400,10),window=cajaT)
ventanaN.mainloop()
