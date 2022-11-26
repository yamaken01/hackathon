import os
import sys
import tkinter as tk

if os.path.isdir("tes") == False:
    os.mkdir("tes")

root = tk.Tk()

# window title
root.title(u"window")

# windows size
root.geometry('400x300')

def inputTxt(txt):
    f = open('./tes/tes.txt','w')
    f.write(txt)
    f.close

def deleteEntry(event):
    entry.delete(0, tk.END)

def getText(event):
    entryValue = 0
    entryValue = entry.get()
    inputTxt(entryValue)

def main():
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
    button1.pack()

    root.mainloop()


if __name__ == '__main__':
    main()

