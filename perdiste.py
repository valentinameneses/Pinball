from tkinter import*

venP = Tk()
venP.title("Perdiste")

c= Canvas(venP,width=650,height=484)
c.pack()

fondoI= PhotoImage(file="perdisteslowbro.gif")
c.create_image(0,0,image=fondoI,anchor = NW)

venP.mainloop()
