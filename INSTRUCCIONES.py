from tkinter import*

venI = Tk()
venI.title("¿Como Jugar?")

c= Canvas(venI,width=630,height=354)
c.pack()

fondoI= PhotoImage(file="MAGIPOKEF.gif")
c.create_image(0,0,image=fondoI,anchor = NW)

VOLVERBOT = PhotoImage(file = 'magikarpBGIF.gif')

def matar(venI):
    venI.destroy()

def volverMenu():
    matar(venI)
    import MENU


botonVolver= Button(venI, text="Volver", image = VOLVERBOT, command=volverMenu, relief=FLAT,bg='#F6620C').place(x=275,y=313)

venI.mainloop()
