import tkinter as tk
# tk._test()

source = tk.Tk()

source.title("Testing")
source.minsize(340, 200)
source.geometry("300x300+100+100")

tk.Label(source, text="Experimentation").pack()

source.mainloop()