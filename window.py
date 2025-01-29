import tkinter as tk
from tkinter import filedialog as fd
# tk._test()


def openFiles():
    BWimage = fd.askopenfilename(title= "Provide a black and white PNG (TRANSPARENT IS NOT WHITE!)", filetypes= "*.png")

source = tk.Tk()

source.title("Testing")
source.minsize(340, 200)
source.geometry("300x300+100+100")

tk.Label(source, text="Experimentation").pack()

tk.Button(source, text="Enter photo", command= openFiles).pack()

source.mainloop()