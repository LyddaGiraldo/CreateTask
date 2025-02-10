import tkinter as tk
from tkinter import filedialog as fd
from PIL import Image, ImageTk

# tk._test()

class MainWindow():

    def __init__(self, source):
        self.source = source
        self.source.title("Testing")
        self.source.minsize(340, 200)
        self.source.geometry("300x300+100+100")
        
        self.BWImage = Image.new("1",[100,100])

        self.imageToTextLabel = tk.Label(self.source, text="Experimentation").pack()
        self.importImage = tk.Button(self.source, text="Enter photo", command= self.openFiles).pack()
        self.BWImageDisplay = tk.Label(source, text="test", image= ImageTk.PhotoImage(self.BWImage)).pack()
        
    def openFiles(self):
    
        image = fd.askopenfilename(title= "Provide a black and white PNG (TRANSPARENT IS NOT WHITE!)", filetypes= [("PNG files", "*.png")])
        
        image = Image.open(image)
        self.BWimage = ImageTk.PhotoImage(image)
        self.BWImageDisplay.config(image=self.BWimage)
        print("imagefound")
        
        


source = tk.Tk()

mainFrame = MainWindow(source)



source.mainloop()