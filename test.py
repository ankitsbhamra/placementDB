from Tkinter import *
import ImageTk
root=Tk()

frame2 = Frame(root)
frame2.pack(side=RIGHT, fill=BOTH, expand=True, pady=10, ipadx=10, padx=10, ipady=5)
path="Images"
image=ImageTk.PhotoImage(file=path+"\SJCE.jpg")
image2=image.subsample(2,2)
Button1=Button(frame2,image=image2)
Button1.image=image2
Button1.pack(side=TOP)

root.mainloop()