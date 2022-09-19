"""
Feu Tricolore -- Version 1 Python
"""

from tkinter import *


# creer une permiere Fenetre

window = Tk()

frame = Frame(window, bg='#f5f5f5')


# personnaliser fenetre

window.title("Interface | Feu Tricolore")
window.geometry("600x700")
#min size window.minsize(480,360)
window.iconbitmap("ico.ico")
window.config(background='#f5f5f5')

#define variable

# Add text
label_title = Label(
    window, 
    text = "Feu Tricolore | Version 1",
    font = ("sans serif", 35),
    bg = "#f5f5f5")
label_title.pack()

#Creer feux tricolore
left_Frame = Frame(frame, bg='#f5f5f5')
width = 270
height = 600

canvas = Canvas(left_Frame, width=width, height=height, bg='dark grey')

canvas.create_rectangle(14, 14, 260, 590, width=0, fill='Black')



led1 = canvas.create_oval(55 , 35, 225, 205, fill='#430D10')
led2 = canvas.create_oval(55 , 215, 225, 385, fill='#946309')
led3 = canvas.create_oval(55 , 395, 225, 565, fill='#004400')


canvas.itemconfigure(led1, fill = 'Red')


canvas.pack()

# buttons
right_Frame = Frame(frame, bg='#f5f5f5' )  

compteur = 0

def suivant():
    global compteur
    compteur += 1
    if compteur == 1:
        canvas.itemconfigure(led1, fill="#430D10")
        canvas.itemconfigure(led2, fill="Orange")
        canvas.itemconfigure(led3, fill="#004400")
    if compteur == 2:
        canvas.itemconfigure(led1, fill="#430D10")
        canvas.itemconfigure(led2, fill="#946309")
        canvas.itemconfigure(led3, fill="Green")
    if compteur == 3:
        compteur = 0 #remettre compteur à 0
        canvas.itemconfigure(led1, fill="Red")
        canvas.itemconfigure(led2, fill="#946309")
        canvas.itemconfigure(led3, fill="#004400")
        
def reset():
    global compteur
    compteur = 0
    canvas.itemconfigure(led1, fill="Red")
    canvas.itemconfigure(led2, fill="#946309")
    canvas.itemconfigure(led3, fill="#004400")

next_btn = Button(right_Frame, text = "Suivant", width = 10, font = ("sans serif", 15), bg = "#093F76", fg = "#fff", command=suivant) 
reset_btn = Button(right_Frame, text = "Reinitialiser", width = 10, font = ("sans serif", 15), bg = "#093F76", fg = "#fff", command=reset) 
quit_btn = Button(right_Frame, text = "Quitter", width = 10, font = ("sans serif", 15), bg = "#093F76", fg = "#fff", command=window.quit) 

next_btn.pack(pady=10)
reset_btn.pack(pady=10)
quit_btn.pack(pady=10)

left_Frame.grid(row = 0, column = 0, sticky = E)
right_Frame.grid(row = 0, column = 1, sticky = W, padx=50)

frame.pack(expand=YES)
# afficher fenetre



window.mainloop()

