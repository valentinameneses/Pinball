

from tkinter import *
import time

#VENTANA PRINCIPAL
ventana=Tk()  #variable ventana    #inicia el script
ventana.title('Poke_Pinball') # titulo
ventana.config(bg="Grey") #color fondo
ventana.geometry("1000x780+0+0")

c = Canvas(ventana,width=650,height=780) #650 -780
c.pack()


fondo= PhotoImage(file="CHARIGIF.gif")
c.create_image(0,0,image= fondo, anchor = NW)

#MENU

#PIDE NOMBRE


##figuras

c.create_line(650,780,650,0,width=3) # marco d
c.create_line(0,3,650,3,width=3) # marco arriba
c.create_line(3,3,3,780,width=3) # marco izq
c.create_line(3,733,650,733,width=3) # limite abajo
c.create_line(610,650,610,220,width=3) #tubo
c.create_line(610,650,480,690,width=2) #inicioPaletaDe
c.create_line(610,650,700,650,width=3) #Base Bolita
c.create_line(100,650,230,690,width=2) #InicoPaletaI
c.create_line(100,650,100,510,width=3)  #BaseArribaPaletaI
c.create_line(0,140,200,0,width=3) #MarcoI
c.create_line(500,0,650,170,width=3) #MarcoD

###OBSTACULOS#####
c.create_oval(100,200,200,300,outline="black",fill="red",width=2) # ObstI
c.create_oval(275,60,375,160,outline="black",fill="red",width=2) #ObstM
c.create_oval(435,200,535,300,outline="black",fill="red",width=2) #ObstD
####  BOLITA  ###### 
#c.create_oval(647,645,618,615,outline="black",fill="red",width=2) # Intento de bola
###### PALETAS FAIL ####### 35 dif 685-720 en Y  90 dif en X PALIABAJO 
##
##palDAbajo=c.create_polygon(230,690,330,700,330,700,340,720,fill="red",width=2,outline="black") #Pal I
##palDArriba= c.create_polygon(230,690,330,700,330,700,340,680,fill="red",width=2,outline="black") 
##palIAbajo= c.create_polygon(490,685,400,700,400,700,390,720,fill="red",width=2,outline="black") #Pal D
##palIArriba= c.create_polygon(490,685,400,700,400,700,390,680,fill="red",width=2,outline="black")
##
##        

#####MOVER PALETAS###############

def movPalI(event):
    global c,palDerecha
    tecla=repr(event.char)
    if (tecla=="'x'"):
        c.delete(palDerecha)
        palDerecha= c.create_polygon(230,690,330,700,330,700,340,680,fill="red",width=2,outline="black")
        c.update()
        c.delete(palDerecha)
        time.sleep(0.15)
        palDerecha= c.create_polygon(230,690,330,700,330,700,340,720,fill="red",width=2,outline="black")


###  PALETA DERECHA  #####
def paletita1():
    global c,palDerecha
    palDerecha= c.create_polygon(230,690,330,700,330,700,340,720,fill="red",width=2,outline="black")#canvas de pal D abajo

def paletita11():
    global c, palDerecha
    palDerecha= c.create_polygon(230,690,330,700,330,700,340,680,fill="red",width=2,outline="black")#canvas pal D arriba

def paletita111():
    global c,palDerecha
    c.delete(palDerecha)
    paletita1()
#### PALETA IZQUIERDA  #####
    
def paletita2():
    global c,palIzquierda  #canvas palI abajo
    palIzquierda= c.create_polygon(490,685,400,700,400,700,390,720,fill="red",width=2,outline="black")

def paletita22():
    global c,palIzquierda
    palIzquierda = c.create_polygon(490,685,400,700,400,700,390,680,fill="red",width=2,outline="black")

def paletita222():
    global c,palDerecha
    c.delete(palDerecha)
    paletita2()


##### TECLAS ####
##
##
def teclitas(event):   #funcion interna de tk
    global c,palIzquierda,palDerecha
    
    tecla = repr(event.char) # lea la tecla
    if tecla == "'x'":
       c.delete (paletita1)
       c.after(0,paletita11)
    c.after(300,paletita111)
        
    if tecla == "'m'":
        c.delete (paletita2)
        c.after(0,paletita22)
        c.after(300,paletita222)
        
####MOVIMIENTO BOLA ##############
def moveball():
    x1, y1, x2, y2 = c.coords(ball["obj"])
    x = (x1 + x2) // 2
    y = (y1 + y2) // 2
    dx = 4
    if x < 10 or x > 650:
        ball["dx"] *= -1
    if y < 10 or y > 780:
        ball["dy"] *= -1
    c.move(ball["obj"],ball["dx"],ball["dy"])
    ventana.after(10,moveball)
    
#ball = {"dx":9 , "dy": 7, "obj":Figure.create_oval(190, 190, 210, 210, fill = "yellow")}
ball= {"dx":0, "dy":-3, "obj":c.create_oval(647,645,618,615,outline="black",fill="red",width=2)}
    

#def perdiste(ventana):
  #  ventana.destroy()
   # import perdiste
    
def cuadricula(c, line_distance):
    for x in range(line_distance,650,line_distance):
        c.create_line(x, 0, x, 780, fill="red")        
    for y in range(line_distance,780,line_distance):
        c.create_line(0, y, 650, y, fill="red")
cuadricula(c,100)


c.bind_all("<Key>", teclitas)
c.focus_set()
paletita1()
paletita2()


ventana.mainloop()  #crea la ventana  # lo finaliza #llama a iniciar programa

