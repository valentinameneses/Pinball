from tkinter import *
import time
import random


#VENTANA JUEGO
ventana=Tk()  #variable ventana    #inicia el script
ventana.title('Poke_Pinball') # titulo
ventana.config(bg="Grey") #color fondo
ventana.geometry("1000x780+0+0")

c = Canvas(ventana,width=650,height=780) #650 -780
c.pack()


fondo= PhotoImage(file="CHARIGIF.gif")
c.create_image(0,0,image= fondo, anchor = NW)


## FIGURAS ##

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

### OBSTACULOS #####
c.create_oval(100,200,200,300,outline="black",fill="red",width=2) # ObstI
c.create_oval(275,60,375,160,outline="black",fill="red",width=2) #ObstM
c.create_oval(435,200,535,300,outline="black",fill="red",width=2) #ObstD


##### PALETAS #####

palI=c.create_polygon(230,690,330,700,330,700,340,720,fill="red",width=2,outline="black")
palD= c.create_polygon(490,685,400,700,400,700,390,720,fill="red",width=2,outline="black")



#####  MOVER PALETAS ###########


def MoverPalD(event):
    global c,palD
    tecla=repr(event.char)

    if(tecla == "'m'"):

        
        c.delete(palD)
        palD=c.create_polygon(490,685,400,700,400,700,390,680,fill="red",width=2,outline="black")
        c.update()
        c.delete(palD)
        time.sleep(0.10)
        palD= c.create_polygon(490,685,400,700,400,700,390,720,fill="red",width=2,outline="black")

def MoverPalI(event):
    global c,palI
    tecla=repr(event.char)

    if(tecla == "'x'"):

        c.delete(palI)
        palI= c.create_polygon(230,690,330,700,330,700,340,680,fill="red",width=2,outline="black") #palIArriba
        c.update()
        c.delete(palI)
        time.sleep(0.10)
        palI=c.create_polygon(230,690,330,700,330,700,340,720,fill="red",width=2,outline="black")

###### MOVER BOLA #####
puntaje = 0
def moveball():
    global puntaje
    x1, y1, x2, y2 = c.coords(ball["obj"])
    x = (x1 + x2) // 2
    y = (y1 + y2) // 2

    valenbola = c.find_overlapping(x1, y1, x2, y2)
    print (valenbola)

    
    if x < 10 or x > 650:
        ball["dx"] *= -1
        
    if y < 10 or y > 740:
        ball["dy"] *= -1


    if valenbola == (1, 12, 18):     #SALIDA BOLA
        ball["dx"] = -5
        ball["dy"] = -3

        
    if valenbola == (1, 14, 18):   #BOLMEDIO
        ball["dx"] = 6
        ball ["dy"] = 3
        puntaje = puntaje + 30

        
    if valenbola == (1, 6, 18):   ## TUBITO
         ball["dx"] = random.randint(-10,-5)
         ball ["dy"] = random.randint(-1,5)
         
    if valenbola == (1, 2, 18):
         ball["dx"] = 3
         ball ["dy"] = -1
         
    if valenbola == (1, 9, 18):   #PARTEABAJO PAL I
        
        ball["dx"] = -6 
        ball["dy"] = random.randint(-6,-5)
        ball["dy"] = random.randint(-5,-3) 


    if valenbola == (1, 17, 18) or valenbola == (1, 18, 20) or valenbola == (1, 18, 22) or valenbola == (1, 18, 24) or valenbola == (1, 18, 26)  or valenbola == (1, 18, 28) or valenbola == (1, 18, 30):
        #PAL 
        ball["dx"] == random.randint(-6,-4) 
        ball["dy"] = random.randint(-9,-5)


    if valenbola == (1, 5, 18):
        
        ball["dx"] = -4
        ball["dy"] = -3


    if valenbola == ((1, 7, 18)):
        
        ball["dx"] = -4
        ball["dy"] = -3
      
    if valenbola == (1, 2, 5, 18):
        ball["dx"] = 4
        ball["dy"] = -4

    if valenbola == (1, 10, 18):
        ball["dx"] = 1
        ball ["dy"] = -7  
        
   
    if valenbola == (1, 15, 18):     ###BOL DERECHA
        ball["dx"] = 1
        ball ["dy"] = -3
        puntaje = puntaje + 60

    if valenbola == (1, 13, 18):    ###BOLIZQUIERDA
        ball["dx"] = 2
        ball ["dy"] = 4
        puntaje = puntaje + 50

    if valenbola == (1, 16, 18):
        ball["dx"] = 4
        ball ["dy"] = -5



      


    #if x >=10 or x <=100:   (1, 16, 18) (1, 17, 18)
    #    ball["dx"] *= -1
    #if y < 10 or y > 200:
    #   ball["dy"] *= -1
        
           
    c.move(ball["obj"],ball["dx"],ball["dy"])
    ventana.after(10,moveball)
    ball["dy"] = ball["dy"] + 0.08 # Gravedad
    cosa_puntaje.config(text = ""+str(puntaje))
    

ball= {"dx":0, "dy":-10, "obj":c.create_oval(647,645,618,615,outline="black",fill="red",width=2)}



### EMPIEZA JUEGO ##########

def empezar(event):
    tecla=repr(event.char)
    if (tecla =="'b'"):
        moveball()
    
'''def cuadricula(c, line_distance):
    for x in range(line_distance,650,line_distance):
        c.create_line(x, 0, x, 780, fill="red")        
    for y in range(line_distance,780,line_distance):
        c.create_line(0, y, 650, y, fill="red")

        
cuadricula(c,100)'''

c.bind("b",empezar)
c.bind("m",MoverPalD)
c.bind("x",MoverPalI)
c.focus_set()

cosa_puntaje = Label( c, text = "" , fg = "white", bg = "red" )
cosa_puntaje.pack()
c.create_window( 335, 17, window = cosa_puntaje )
def iniciar(nombre):
    botonNombre= Label(text="Jugador: \n"+nombre,font=("century gothic", 20)).place(x=10, y=200)
    ventana.mainloop()  #crea la ventana  # lo finaliza #llama a iniciar programa



