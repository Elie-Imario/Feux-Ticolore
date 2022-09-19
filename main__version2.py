"""
Feu Tricolore -- Version 2 Python
"""
import tkinter as tk
from tkinter import ttk
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
    text = "Feu Tricolore | Version 2",
    font = ("sans serif", 35),
    bg = "#f5f5f5")
label_title.pack()

# Slider
current_value = tk.DoubleVar()

#get slider value
def get_current_value():
    x = float('{: .2f}'.format(current_value.get()))
    if x == 0.0 :
        return time
    else:
        y = int(x)
        return time - (y*10)
    
#event on sliderValue changed
def onSlideChanged(event):
    get_current_value()
    
#define start() function
def start():    
    if canvas.itemcget(led1, 'fill') == '':
        canvas.itemconfigure(led1, fill="Red")
        canvas.itemconfigure(led2, fill="#430D10")
        canvas.itemconfigure(led3, fill="#004400")
    elif canvas.itemcget(led1, 'fill') == 'Red':
        canvas.itemconfigure(led1, fill="#430D10")
        canvas.itemconfigure(led2, fill="Orange")
        canvas.itemconfigure(led3, fill="#004400")
    elif canvas.itemcget(led2, 'fill') == 'Orange':
        canvas.itemconfigure(led1, fill="#430D10")
        canvas.itemconfigure(led2, fill="#946309")
        canvas.itemconfigure(led3, fill="Green")
    elif canvas.itemcget(led3, 'fill') == 'Green':
        canvas.itemconfigure(led1, fill="Red")
        canvas.itemconfigure(led2, fill="#946309")
        canvas.itemconfigure(led3, fill="#004400")
    window.after(get_current_value(), start)

    
time = 1500

#Creer feux tricolore
container_frame = Frame(frame, bg='#f5f5f5')
width = 270
height = 550

canvas = Canvas(container_frame, width=width, height=height, bg='dark grey')

canvas.create_rectangle(12, 10, 260, 540, width=0, fill='Black')




led1 = canvas.create_oval(60 , 20, 210, 170, fill='#430D10')
led2 = canvas.create_oval(60 , 200, 210, 350, fill='#946309')
led3 = canvas.create_oval(60 , 380, 210, 530, fill='#004400')

#init led start loop
canvas.itemconfigure(led1, fill = '')

start()

canvas.pack()


        
s = ttk.Style()
s.theme_use('clam')
slider_frame = Frame(frame, bg='#f5f5f5')
slider = ttk.Scale(
    slider_frame,
    from_= 0,
    to = 100,
    length=125,
    orient = 'horizontal',
    variable = current_value,
    command=onSlideChanged,
)
left_label = Label(
    slider_frame, 
    text = "lent",
    font = ("sans serif", 15),
    bg = "#f5f5f5")
        
right_label = Label(
    slider_frame, 
    text = "Rapide",
    font = ("sans serif", 15),
    bg = "#f5f5f5")
        
left_label.grid(padx = 10,row = 0, column = 0, sticky = E)
slider.grid(pady = 30, column=2, row=0, sticky= E)
right_label.grid(padx = 10,row = 0, column = 5, sticky = E)
container_frame.pack()
slider_frame.pack(expand=YES)

frame.pack(expand=YES)



# afficher fenetre
window.mainloop()

