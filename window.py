import tkinter as tk
from tkinter import filedialog as fd
from tkinter import PhotoImage as PI

# tk._test()



def openFiles():
    BWimage = fd.askopenfilename(title= "Provide a black and white PNG (TRANSPARENT IS NOT WHITE!)", filetypes= [("PNG files", "*.png")])
    if BWimage:
        with open(BWimage, "rb") as imagefile:
            content = PI(file = imagefile)
            tk.Label(source, image = content).pack()


source = tk.Tk()

source.title("Testing")
source.minsize(340, 200)
source.geometry("300x300+100+100")

tk.Label(source, text="Experimentation").pack()

tk.Button(source, text="Enter photo", command= openFiles).pack()



source.mainloop()