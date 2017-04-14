from Tkinter import *

class MakeButton:
    def __init__(self,frame,name):
        self.name=name
        self.frame=frame
        #self.func=func

    def makeB(self):
        button = Button(self.frame, text=self.name)
        button.pack(side=TOP, padx=10, pady=10)
        #button.bind("<Button-1>", lambda event:self.func )
        return button

class MakeLabel:
    def __init__(self, frame, name):
        self.name = name
        self.frame=frame

    def makeL(self):
        label = Label(self.frame, text=self.name)
        label.pack(side=LEFT, padx=10, pady=10)
        #label.bind("<Button-1>", lambda event: self.func)
        return label