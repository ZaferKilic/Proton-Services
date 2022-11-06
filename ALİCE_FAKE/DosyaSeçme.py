import tkinter
import tkinter.filedialog as fd
import os

root = tkinter.Tk()
root.withdraw() 
currdir = os.getcwd()
tempdir = fd.askopenfilename(parent=root, initialdir= "/", title='DOSYA KONUMU SEÇ')
if len(tempdir) > 0:
    print ("You chose %s" % tempdir)