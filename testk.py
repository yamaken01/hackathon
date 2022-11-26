import sys
import tkinter as tk

root = tk.Tk()

# window title
root.title(u"window")

# windows size
root.geometry('400x300')

def deleteEntry(event):
    entry.delete(0, tk.END)

def getText(event):
    entryValue = 0
    entryValue = entry.get()
    label = tk.Label(text=str(entryValue))
    label.pack()

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
