import os

if os.path.isdir("tes") == False:
    os.mkdir("tes")

mode = input("plese r or w key\n")
if mode == "r":
    try:
        f = open('./tes/tes.txt','r')
    except:
        print("file is not defind")
if mode == "w":
        f = open('./tes/tes.txt','w')
        txt = input("plese write any word!\n")
        f.write(txt)
        f.close
a = input()


