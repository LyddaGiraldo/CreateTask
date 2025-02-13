import tkinter as tk
from tkinter import filedialog as fd
from tkinter import PhotoImage as PI
from PIL import Image, ImageTk

# tk._test()

class MainWindow():

    def __init__(self, source):
        self.source = source
        self.source.title("Testing")
        self.source.minsize(340, 200)
        self.source.geometry("500x300+100+100")
        
        defaultImage = Image.open("defaultgrey.png")
        defaultImage = defaultImage.resize((250,250))
        defaultImage = ImageTk.PhotoImage(defaultImage)


        self.imageToTextLabel = tk.Label(self.source, text="Experimentation")
        self.imageToTextLabel.pack()
        
        self.BWImageDisplay = tk.Label(source, text="test", image= defaultImage)
        self.BWImageDisplay.defaultImage=defaultImage
        self.BWImageDisplay.pack(side= "left")

        self.importImage = tk.Button(self.source, text="Enter photo", command= self.openFiles)
        self.importImage.pack(side= "left")
        
    def openFiles(self):
    
        image = fd.askopenfilename(title= "Provide a black and white PNG (TRANSPARENT IS NOT WHITE!)", filetypes= [("PNG files", "*.png")])

        image = Image.open(image)
    

        image = image.resize((250,250))
        self.BWimage = ImageTk.PhotoImage(image)
        self.BWImageDisplay.configure(image=self.BWimage)
        print("imagefound")
        
        


source = tk.Tk()

mainFrame = MainWindow(source)



source.mainloop()