from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
import os
from pygame import mixer

mixer.init()

def Version():
    messagebox.showinfo('About','Music player\n version : 1.0\n author : Satrap18')

def Help():
    messagebox.showinfo('Help','Open Folder(*.mp3)')

def Clear():
    list_music.delete(0,END) 
    
def Folder():
    path = filedialog.askdirectory()
    os.chdir(r'' + path)
    songs=os.listdir()
    for s in songs:
        if s.endswith('.mp3'):
            list_music.insert(END,s)

def Play():
    run = list_music.get(ACTIVE)
    mixer.music.load(run)
    mixer.music.play()
    
window = Tk()
window.title('music_player')
window.geometry('400x350')
window.resizable(False,False)

icon = PhotoImage(file='1.jpg')
window.iconphoto(True,icon)


photo1 = PhotoImage(file='icons8-music-96.png')
photo2 = PhotoImage(file='icons8-eighth-rest-48.png')

photo3 = PhotoImage(file='icons8-play-48.png')
photo4 = PhotoImage(file='icons8-pause-48.png')
photo5 = PhotoImage(file='icons8-resume-button-48.png')
photo6 = PhotoImage(file='icons8-stop-48.png')

lbl = Label(window,image=photo1)
lbl.pack()

lbl2 = Label(window,image=photo2)
lbl2.place(x=215,y=35)

list_music=Listbox(window,selectmode=SINGLE,bg='#F0F0F0',font=('arial',12),width=40)
list_music.pack()

btn = Button(window,image=photo3,bd=0,command=Play)
btn.place(x=40,y=295)

btn2 = Button(window,image=photo4,bd=0,command=mixer.music.pause)
btn2.place(x=120,y=295)

btn3 = Button(window,image=photo5,bd=0,command=mixer.music.unpause)
btn3.place(x=200,y=295)

btn4 = Button(window,image=photo6,bd=0,command=mixer.music.stop)
btn4.place(x=280,y=295)

menubar = Menu(window)

filemenu = Menu(menubar,tearoff=0)
filemenu1 = Menu(menubar,tearoff=0)


menubar.add_cascade(label="File",menu=filemenu)
menubar.add_cascade(label="Help",menu=filemenu1)


filemenu.add_command(label="Open Folder",command=Folder)
filemenu.add_command(label='Clear List',command=Clear)
filemenu.add_command(label='Exit',command=exit)
filemenu1.add_command(label="ViewHelp",command=Help)
filemenu1.add_command(label="About Music player",command=Version)


window.config(menu=menubar)

window.mainloop()