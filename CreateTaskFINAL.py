import tkinter as tk
from tkinter import filedialog as fd
from tkinter import PhotoImage as PI
from PIL import Image, ImageTk
import numpy as np

np.set_printoptions(threshold=np.inf)

class MainWindow():

    def __init__(self, source):
        

        with open("loreipsum.txt", "r") as file:
            defaultText = file.read()
            
        self.source = source
        self.source.title("Image to Text Converter")
        self.source.minsize(340, 200)
        self.source.geometry("750x400+100+100")

        self.imageFrame = tk.Frame(source, padx=30)
        self.imageFrame.pack(side="left")
        
        self.textFrame = tk.Frame(source, padx=30)
        self.textFrame.pack(side="right")
        
        defaultImage = Image.open("defaultgrey.png")
        PIL_BW_image = defaultImage.convert(mode="1")
        defaultImage = defaultImage.resize((250,250))
        defaultImage = ImageTk.PhotoImage(defaultImage)

        self.imageInstructions= tk.Label(self.imageFrame, text="Please enter a black and white png file.\nColored images will be turned monochrome.\nLarger files may result in slowed runtimes.")
        self.imageInstructions.pack()

        self.BWImageDisplay = tk.Label(self.imageFrame, image= defaultImage)
        self.BWImageDisplay.defaultImage=defaultImage
        self.BWImageDisplay.pack()

        self.importImage = tk.Button(self.imageFrame, text="Enter photo", command= self.openFiles, relief="raised")
        self.importImage.pack()

        self.textInstructions= tk.Label(self.textFrame, text="Please enter the string you want overlayed on the image.\nThen use the button to submit.")
        self.textInstructions.pack()

        self.insertText = tk.Text(self.textFrame, height = 20, width = 50)
        self.insertText.insert(tk.END,defaultText)
        self.insertText.pack()

        self.insertTextButton = tk.Button(self.textFrame, text="Submit text", command= lambda: self.readText(PIL_BW_image), relief="raised")
        self.insertTextButton.pack()    

    def readText(self, pilbwImage):

        inputtedText = self.insertText.get("1.0", "end-1c")
        imageArray= np.asarray(pilbwImage)
        
        formattedText = ''
        i=0
        
        for row in imageArray:
            for col in row:
                if i>=len(inputtedText):
                    i=0
                if col:
                    formattedText += inputtedText[i]
                    i += 1
                else:
                    formattedText += " "
            
            formattedText += '\n'
        print(formattedText)
        
        with open("imageFormattedAsPhoto.txt", "w") as iFAPFile:
            iFAPFile.write(formattedText)
        
    def openFiles(self):                                                                     
    
        self.PIL_BW_image = fd.askopenfilename(title= "Provide a black and white PNG (TRANSPARENT IS NOT WHITE!)", filetypes= [("PNG files", "*.png")])

        self.PIL_BW_image = Image.open(self.PIL_BW_image)
        self.PIL_BW_image = self.PIL_BW_image.convert(mode="1")

        self.BWimage = ImageTk.PhotoImage(self.PIL_BW_image.resize((250,250)))
        self.BWImageDisplay.configure(image=self.BWimage)

source = tk.Tk()

mainFrame = MainWindow(source)

source.mainloop()