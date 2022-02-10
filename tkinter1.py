import tkinter as tk
from unicodedata import name

class HelloWorld(tk.Frame):
    def __init__(self,parent):
        super(HelloWorld, self).__init__(parent)
        
        self.label = tk.Label(self, text ="Hello world")
        self.label.pack(padx = 20, pady = 20)

if __name__ == "__main__":
    root = tk.Tk()
    main = HelloWorld(root)
    main.pack(fill ="both", expand= True)
    
    root.mainloop()