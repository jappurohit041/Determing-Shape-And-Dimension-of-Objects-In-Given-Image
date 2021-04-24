import tkinter
from PIL import Image, ImageTk, ImageSequence
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import threading
from time import sleep
'''
class Loading:
    def __init__():
        self.abc = tkinter.Tk()
    def animate(canvas, root,sequence,image,counter):
        canvas.itemconfig(image, image=sequence[counter])
        root.after(20, lambda: animate(canvas, root,sequence,image,(counter+1) % len(sequence)))
        
    def callback():
        abc.destroy()
    def loadingFunction():
        
        canvas = tkinter.Canvas(abc, width=400, height=400)
        canvas.pack()
        sequence = [ImageTk.PhotoImage(img)
                            for img in ImageSequence.Iterator(
                                    Image.open(
                                    r'load.gif'))]
        image = canvas.create_image(200,200, image=sequence[0])
        animate(canvas,abc,sequence,image,1)
        button = tkinter.Button(abc, text='Click Here!')
        button.config(command=callback)
        button.pack(padx=100, pady=50)
        abc.mainloop()

    loadingFunction()

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # configure the root window
        self.title('Loading Screen')
        canvas = tk.Canvas(self, width=400, height=400)
        canvas.pack()
        sequence = [ImageTk.PhotoImage(img)
                            for img in ImageSequence.Iterator(
                                    Image.open(
                                    r'load.gif'))]
        image = canvas.create_image(200,200, image=sequence[0])
        self.animate(canvas,self,sequence,image,1)
        self.button = tk.Button(self, text='Click Here!')
        self.button.config(command=self.callback)
        self.button.pack(padx=100, pady=50)
        
    def animate(self,canvas, root,sequence,image,counter):
        canvas.itemconfig(image, image=sequence[counter])
        root.after(20, lambda: self.animate(canvas, root,sequence,image,(counter+1) % len(sequence)))
     
    def callback(self):
        self.destroy()
def funct1():
    for i in range(0,1000):
        print(i)
    print("threading count in loop screen",threading.active_count())
    
def funct2():
    app = App()
    print("Threading in loading scree",threading.active_count())
    if(threading.active_count()<3):
        app.callback()
    app.mainloop()

def threadingLogic():
    print("Before threading init",threading.active_count())
    t2= threading.Thread(target=funct2).start()
        
    print("After 1 threading init",threading.active_count())
    t1= threading.Thread(target=funct1).start()
    
    print("After 2 threading init",threading.active_count())
threadingLogic()
'''
''''
import tkinter as tk
from time import sleep



def task():
    # The window will stay open until this function call ends.
    sleep(10) # Replace this with the code you want to run
    root.destroy()

root = tk.Tk()
root.title("Example")

label = tk.Label(root, text="Waiting for task to finish.")
label.pack()

root.after(100, task)
root.mainloop()

print("Main loop is now over and we can do other stuff.")'''


def task():
    # The window will stay open until this function call ends.
    for i in range(10000):
        print(i)
    
    abc.destroy()



abc = tkinter.Tk()
canvas = tkinter.Canvas(abc, width=400, height=400)
canvas.pack()
sequence = [ImageTk.PhotoImage(img)
                            for img in ImageSequence.Iterator(
                                    Image.open(
                                    r'load.gif'))]
image = canvas.create_image(200,200, image=sequence[0])
animate(canvas,abc,sequence,image,1)
abc.after(100, task)
abc.mainloop()
