from email.mime import image
from email.policy import default
import imghdr
import tkinter as tk
from tkinter import filedialog as fd
from tkinter import PhotoImage as PI
from PIL import Image, ImageTk
import numpy as np

# tk._test()

np.set_printoptions(threshold=np.inf)

class MainWindow():

    def __init__(self, source):
        

        with open("loreipsum.txt", "r") as file:
            defaultText = file.read()
            
        #print(defaultText)

        self.source = source
        self.source.title("Testing")
        self.source.minsize(340, 200)
        self.source.geometry("600x300+100+100")
        
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

        self.insertText = tk.Text(self.source, height = 5, width = 20)
        self.insertText.insert(tk.END,defaultText)
        self.insertText.pack(side="right")

        self.insertTextButton = tk.Button(self.source, text="Submit text", command=self.readText)
        self.insertTextButton.pack(side="right")

        self.inputtedTextList = []

    def readText(self):
        inputtedText = self.insertText.get("1.0", "end-1c")
        self.inputtedTextList = [ltr for ltr in inputtedText if ltr != '/n']

        imageArray= np.asarray(self.PIL_BW_image)
        
        """
        print(self.inputtedTextList)
        print(self.BWConvertedimage.size)
        print(imageData)
        print(self.PIL_BW_image.getbands()) 
        print("image shape = ")
        print(imageArray.shape)       
        print(imageArray)
        """
        
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

        """
        imageData = [imageData[i] for i in range(len(imageData)) if (i%16==0)]
        print("saves only every 16 i think")
        print(imageData, len(imageData))

        imageData = [imageData[i] for i in range(len(imageData)) if (i==0) or imageData[i] != imageData[i-1]]
        print("without dupes")
        print(imageData)
                
        
        for row in imageArray:
            for col in row:
                if i>=len(inputtedText):
                    i=0
                if col:
                    formattedText += "."
                    i += 1
                else:
                    formattedText += " "
            
            formattedText += '\n'
        #print(formattedText)
        """
        
        
    def openFiles(self):                                                                     
    
        self.PIL_BW_image = fd.askopenfilename(title= "Provide a black and white PNG (TRANSPARENT IS NOT WHITE!)", filetypes= [("PNG files", "*.png")])

        self.PIL_BW_image = Image.open(self.PIL_BW_image)
        self.PIL_BW_image = self.PIL_BW_image.convert(mode="1")

        self.BWimage = ImageTk.PhotoImage(self.PIL_BW_image.resize((250,250)))
        self.BWImageDisplay.configure(image=self.BWimage)
        print("imagefound")

        """
       for x in np.nditer(imageArray):
            print(x)
       print(list(self.PIL_BW_image.getdata()), len(list(self.PIL_BW_image.getdata())))
       """ 

source = tk.Tk()

mainFrame = MainWindow(source)

source.mainloop()