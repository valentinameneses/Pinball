from tkinter import *
import time

#VENTANA PRINCIPAL
ventana=Tk()  #variable ventana    #inicia el script
ventana.title('PokePinball') # titulo
ventana.config(bg="AliceBlue") #color fondo
ventana.geometry("680x440+0+0")

c = Canvas(ventana,width=680,height=440) 
c.pack()


fondo= PhotoImage(file="POKENOB.gif")
c.create_image(0,0,image= fondo, anchor = NW)

JUGARBOT = PhotoImage(file = 'JUGARBOT.gif')
INSTRUBOT =PhotoImage(file='INSTRUCCIONESBOT.gif')
SALIRBOT =PhotoImage(file='SALIRBOT.gif')




def FuncionJugar():
    ventana.destroy()
    import nombretk
    
def Instrucciones():
    ventana.destroy()
    import INSTRUCCIONES
    


botonjugar= Button(ventana, text="Jugar", image = JUGARBOT, command=FuncionJugar,relief=FLAT,bg='red').place(x=40, y=244)
botoninstrucciones=Button(ventana,text="Instrucciones", image= INSTRUBOT, command=Instrucciones,bg='blue',relief=FLAT).place(x=22,y=337)
botonSalir=Button(ventana,text='Salir',image=SALIRBOT, command=ventana.destroy,bg='green',relief=FLAT).place(x=14,y=155)
