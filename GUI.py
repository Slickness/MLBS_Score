__author__ = 'user0'
import sys
import MLB
from threading import Thread
try:
    #python 2
    import Tkinter as tk
    from Tkinter import messagebox
except ImportError:
    #python 3
    import tkinter as tk
    from tkinter import messagebox
url ="http://www.sportsnet.ca/baseball/mlb/scores/"
url2= "http://www.sportsnet.ca/baseball/mlb/scores/?datepicker-date=2015-08-11" #date picker
Games = MLB.main(url)
def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()
        sys.exit()
def callback(Game):
    root.protocol("WM_DELETE_WINDOW", on_closing)
    text.insert("1.0",Game[4] + "\n")
    text.insert("2.0",Game[0] + " " + Game[1] + "\n")
    text.insert("3.0",Game[2] + " " + Game[3] + "\n")
root = tk.Tk()

#width --> width in chars, height --> lines of text

text_width = 20
text = tk.Text(root,width=text_width, height =3, bg ='yellow')
text.pack()
text.config(font=('courier,48,bold'))
while True:

    Games = MLB.main(url)
    for Game in Games:
        #callbackThread = Thread(target=callback(Game))
        text.after(5000,callback(Game))
        #time.sleep(5)
        root.update()



root.mainloop()