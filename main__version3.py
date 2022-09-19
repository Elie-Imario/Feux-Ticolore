"""
Feu Tricolore -- Version 3 Python
"""

import tkinter as tk
from tkinter import *
from tkinter import ttk
from turtle import bgcolor


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
    text = "Feu Tricolore | Version 3",
    font = ("sans serif", 35),
    bg = "#f5f5f5")
label_title.pack()


##########
current_value1 = tk.DoubleVar()
current_value2 = tk.DoubleVar()
current_value3 = tk.DoubleVar()

def convertToSecond(TimeMillis):
    return float('{: .2f}'.format(TimeMillis / 1000))

#led1
def get_first_led_time_value():
    x = float('{: .2f}'.format(current_value1.get()))
    if x == 0.0 :
        return 0
    else:
        y = int(x)
        return loopTime * (y/100)
    
def RedSlideChanged(event):
    get_first_led_time_value()
    slider1Label.configure(text= str(convertToSecond(get_first_led_time_value()))+' s')
    
####

#led2
def get_second_led_time_value():
    x = float('{: .2f}'.format(current_value2.get()))
    if x == 0.0 :
        return 0
    else:
        y = int(x)
        return loopTime * (y/100)
    
def OrangeSlideChanged(event):
    get_second_led_time_value()
    slider2Label.configure(text= str(convertToSecond(get_second_led_time_value()))+' s')

####

#led3
def get_last_led_time_value():
    x = float('{: .2f}'.format(current_value3.get()))
    if x == 0.0 :
        return 0
    else:
        y = int(x)
        return loopTime * (y/100)
    
def GreenSlideChanged(event):
    get_last_led_time_value()    
    slider3Label.configure(text= str(convertToSecond(get_last_led_time_value()))+' s')
    
    
duree = 0    


###
container_Frame = Frame(frame, bg='#f5f5f5')
slides_container = Frame(frame, bg='#f5f5f5')  
slider_frame = Frame(frame, bg='#f5f5f5')

#label
slider1Label = Label(
    slider_frame,
    text= '',
    font = ("sans serif", 13),
    bg = "#f5f5f5"
)

slider2Label = Label(
    slider_frame,
    text= '',
    font = ("sans serif", 13),
    bg = "#f5f5f5"
)
slider3Label = Label(
    slider_frame,
    text= '',
    font = ("sans serif", 13),
    bg = "#f5f5f5"
)


#start
def start():    
    global duree
    final_R = int(get_first_led_time_value())
    final_O = int(get_second_led_time_value())
    final_G = int(get_last_led_time_value())
    
    if canvas.itemcget(led1, 'fill') == '':
        canvas.itemconfigure(led1, fill="Red")
        canvas.itemconfigure(led2, fill="#430D10")
        canvas.itemconfigure(led3, fill="#004400")
        duree = loopTime
    elif canvas.itemcget(led1, 'fill') == 'Red':
        canvas.itemconfigure(led1, fill="#430D10")
        canvas.itemconfigure(led2, fill="Orange")
        canvas.itemconfigure(led3, fill="#004400")
        duree = final_O 
    elif canvas.itemcget(led2, 'fill') == 'Orange':
        canvas.itemconfigure(led1, fill="#430D10")
        canvas.itemconfigure(led2, fill="#946309")
        canvas.itemconfigure(led3, fill="Green")
        duree = final_G
    elif canvas.itemcget(led3, 'fill') == 'Green':
        canvas.itemconfigure(led1, fill="Red")
        canvas.itemconfigure(led2, fill="#946309")
        canvas.itemconfigure(led3, fill="#004400")
        duree = final_R
    
    window.after(duree, start)
    
    
loopTime = 2500

#Creer feux tricolore
width = 270
height = 550

canvas = Canvas(container_Frame, width=width, height=height, bg='dark grey')

canvas.create_rectangle(12, 10, 260, 540, width=0, fill='Black')



led1 = canvas.create_oval(60 , 20, 210, 170, fill='#430D10')
led2 = canvas.create_oval(60 , 200, 210, 350, fill='#946309')
led3 = canvas.create_oval(60 , 380, 210, 530, fill='#004400')



canvas.itemconfigure(led1, fill = '')


canvas.pack()



# slides

s = ttk.Style()
s.theme_use('clam')
slider1 = ttk.Scale(
    slider_frame,
    from_= 0,
    to = 100,
    length= 125,
    orient = 'horizontal',
    variable = current_value1,
    command = RedSlideChanged,
)
slider1.set(100)

slider2 = ttk.Scale(
    slider_frame,
    from_= 0,
    to = 100,
    length= 125,
    orient = 'horizontal',
    variable = current_value2,
    command = OrangeSlideChanged,
)
slider2.set(100)

slider3 = ttk.Scale(
    slider_frame,
    from_= 0,
    to = 100,
    length= 125,
    orient = 'horizontal',
    variable = current_value3,
    command = GreenSlideChanged,
)
slider3.set(100)


slider1.grid(row=0, column=0, sticky='w')
slider2.grid(row=0, column=1, sticky='w')
slider3.grid(row=0, column=2, sticky='w')


slider1Label.grid(row=1, column=0, sticky='w', padx= 25, pady= 5)
slider2Label.grid(row=1, column=1, sticky='w', padx= 25, pady= 5)
slider3Label.grid(row=1, column=2, sticky='w', padx= 25, pady= 5)

container_Frame.pack(expand=YES)
slider_frame.pack(expand=YES, pady=20)
frame.pack(expand=YES)


start()
# afficher fenetre



window.mainloop()




