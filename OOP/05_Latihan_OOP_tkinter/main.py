import tkinter

mainWindow = tkinter.Tk()

label1 = tkinter.Label(mainWindow, text="label1")
label2 = tkinter.Label(mainWindow, text="label2")

button1 = tkinter.Button(mainWindow, text="button1")
button2 = tkinter.Button(mainWindow, text="button2")

# Method positioning
label1.pack()
label2.pack()
button1.pack()
button2.pack()

# Method menampilkan GUI
mainWindow.mainloop()
