#GUI - Graphical User Interface

# Libraries
# 1. tkinter
# 2. PyQT
# 3. Turtle

import tkinter as ttk
app = ttk.Tk()
app.title('My App')
app.geometry('600x400')

ttk.Label(app, text = 'A simple Text Label').place(x=50,y=50)
ttk.Label(app, text= 'Panda loves bamboo').place(x=50,y=80)
app.mainloop()