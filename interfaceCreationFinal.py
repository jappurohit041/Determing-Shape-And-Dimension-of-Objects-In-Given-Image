from SizeAndShapeDetectionFinal import mainfunction
import tkinter.filedialog as filedialog
from PIL import Image, ImageTk, ImageSequence
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import simpledialog
import filetype
import os.path
from os import path
import threading

master = tk.Tk()
def animate(canvas, root,sequence,image,counter):
    canvas.itemconfig(image, image=sequence[counter])
    root.after(20, lambda: animate(canvas, root,sequence,image,(counter+1) % len(sequence)))
    
def new_window():
    abc = tk.Toplevel(master)
    canvas = tk.Canvas(abc, width=400, height=400)
    canvas.pack()
    sequence = [ImageTk.PhotoImage(img)
                        for img in ImageSequence.Iterator(
                                Image.open(
                                r'load.gif'))]
    abc.after(57000,abc.destroy)
    image = canvas.create_image(200,200, image=sequence[0])
    animate(canvas,abc,sequence,image,1)

def answer():
    mb.showerror("Error", "Wrong file path or wrong file extention")

def inputFunction():
    input_path = tk.filedialog.askopenfilename(defaultextension=".jpeg", 
                                      filetypes=[("All Files","*.*"), 
                                        ("Image File","*.png")])
    input_entry.insert(0, input_path)  # Insert the 'path'

def outputFunction():
    output_path = tk.filedialog.askdirectory()
    output_entry.insert(0, output_path)  # Insert the 'path'

def helloCallBack(filePathDict):
    validextension = ['jpg','png','jpeg']
    inputPath = input_entry.get()
    try:
        if len(inputPath.strip()) == 0:
            answer()
            return
        kind = filetype.guess(inputPath)
        kindtype = str(kind.extension)
        if kindtype not in validextension:
            answer()
            return
    except FileNotFoundError:
        answer()
        return

    outputPath = output_entry.get()
    try:
        if path.isdir(outputPath) == False:
            answer()
            return
    except FileNotFoundError:
        answer()
        return
    filePathDict['inputPath'] = inputPath
    filePathDict['outputPath'] = outputPath
    print(filePathDict)
    t1 = threading.Thread(target=mainfunction,args=(filePathDict,))
    t2 = threading.Thread(target=new_window)
    t1.start()
    t2.start()
top_frame = tk.Frame(master)
bottom_frame = tk.Frame(master)
line = tk.Frame(master, height=1, width=400, bg="grey80", relief='groove')
filePathDict = {}

input_path = tk.Label(top_frame, text="Input File Path:")
input_entry = tk.Entry(top_frame, width=40)
browse1 = tk.Button(top_frame, text="Browse", command = inputFunction)

output_path = tk.Label(bottom_frame, text="Output File Path:")
output_entry = tk.Entry(bottom_frame, text="", width=40)
browse2 = tk.Button(bottom_frame, text="Browse", command= outputFunction)

begin_button = ttk.Button(bottom_frame, text='Start', command= lambda: helloCallBack(filePathDict))

top_frame.pack(side=tk.TOP)
line.pack(pady=10)
bottom_frame.pack(side=tk.BOTTOM)

input_path.pack(pady=5)
input_entry.pack(pady=5)
browse1.pack(pady=5)


output_path.pack(pady=5)
output_entry.pack(pady=5)
browse2.pack(pady=5)

begin_button.pack(pady=20)
master.title("SS PROJECT")
master.resizable(0,0)
master.mainloop()
