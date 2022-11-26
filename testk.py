import os
import sys
import tkinter as tk

if os.path.isdir("tes") == False:
    os.mkdir("tes")

root = tk.Tk()

# window title
root.title(u"window")

#canvas = tk.Canvas(bg="black", width=400, height=300)
#canvas.pack()
pic = tk.PhotoImage(file="./tes/IMG_6257.png", width=400, height=300)
#canvas.create_image(0, 0, image=pic, anchor=tk.NW)

# windows size
root.geometry('400x300')

def deleteEntry(event):
    entry.delete(0, tk.END)

def getText(event):
    saveFile = open('./tes/tes.txt','a')
    saveFile.write(entry.get())
    saveFile.close

def putPicture(event):
    canvas = tk.Canvas(bg="black", width=400, height=300)
    canvas.pack()
    #pic = tk.PhotoImage(file="./tes/human.png", width=40, height=30)
    canvas.create_image(0, 0, image=pic, anchor=tk.NW)

# frontend
# label
static1 = tk.Label(text="test", foreground='#ff0000', background='#90caf9')
# これで本当にいいのか？
static1.pack()

# entry
entry = tk.Entry(width=50)
entry.insert(tk.END, '挿入する文字列')
entry.pack()

# button
button1 = tk.Button(text = 'なぐる', width=50)
button1.bind('<1>', getText)
button1.bind('<3>', putPicture)
button1.pack()

root.mainloop()



