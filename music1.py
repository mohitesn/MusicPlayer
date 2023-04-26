from tkinter import *
from PIL import ImageTk,Image
import os
from pygame import mixer

co1="#ffb6c1"
co2="#3C1DC6"
co3="#333333"
co4="#CFC7F8"

window=Tk()
window.title("")
window.geometry('352x255')
window.configure(background=co1)
window.resizable(width=FALSE, height=FALSE)

def play_music():
    running=listbox.get(ACTIVE)
    running_song['text']=running
    mixer.music.load(running)
    mixer.music.play()
    
def pause_music():
    mixer.music.pause()    
    
def continue_music():
    mixer.music.unpause()    
    
def stop_music():
    mixer.music.stop() 
    
def next_music():
    playing=running_song['text']
    index=songs.index(playing)
    new_index=index + 1
    playing=songs[new_index]
    mixer.music.load(playing)
    mixer.music.play() 
    
    listbox.delete(0,END)
    show()
    
    listbox.select_set(new_index)
    running_song['text']=playing 
    
def prev_music():
    playing=running_song['text']
    index=songs.index(playing)
    new_index=index - 1
    playing=songs[new_index]
    mixer.music.load(playing)
    mixer.music.play() 
    
    listbox.delete(0,END)
    show()
    
    listbox.select_set(new_index)
    running_song['text']=playing                 
        
    
    


left_frame=Frame(window,width=150,height=150,bg=co1)
left_frame.grid(row=0,column=0,padx=1,pady=1)

right_frame=Frame(window,width=250,height=150,bg=co3)
right_frame.grid(row=0,column=1,padx=0)

down_frame=Frame(window,width=400,height=100,bg=co1)
down_frame.grid(row=1,column=0,columnspan=3,padx=0,pady=1)

listbox=Listbox(right_frame,selectmode=SINGLE,font=("Arial 9 bold"),width=22,bg=co3,fg=co1)
listbox.grid(row=0,column=0)



w=Scrollbar(right_frame)
w.grid(row=0,column=1)

listbox.config(yscrollcommand=w.set)
w.config(command=listbox.yview)

img1=Image.open('image/5.png')
img1=img1.resize((130,130))
img1=ImageTk.PhotoImage(img1)
appimage=Label(left_frame,height=130,image=img1,padx=10)
appimage.place(x=10,y=35)

img2=Image.open('image/6.png')
img2=img2.resize((30,30))
img2=ImageTk.PhotoImage(img2)
play_button=Button(down_frame,width=40,height=40,image=img2,padx=10,font=("Ivy 10"),command=play_music)
play_button.place(x=56+28,y=35)

img3=Image.open('image/3.png')
img3=img3.resize((30,30))
img3=ImageTk.PhotoImage(img3)
prev_button=Button(down_frame,width=40,height=40,image=img3,padx=10,font=("Ivy 10"),command=prev_music)
prev_button.place(x=10+28,y=35)

img4=Image.open('image/1.png')
img4=img4.resize((30,30))
img4=ImageTk.PhotoImage(img4)
next_button=Button(down_frame,width=40,height=40,image=img4,padx=10,font=("Ivy 10"),command=next_music)
next_button.place(x=102+28,y=35)


img5=Image.open('image/7.png')
img5=img5.resize((30,30))
img5=ImageTk.PhotoImage(img5)
pause_button=Button(down_frame,width=40,height=40,image=img5,padx=10,font=("Ivy 10"),command=pause_music)
pause_button.place(x=148+28,y=35)


img6=Image.open('image/4.png')
img6=img6.resize((30,30))
img6=ImageTk.PhotoImage(img6)
continue_button=Button(down_frame,width=40,height=40,image=img6,padx=10,font=("Ivy 10"),command=continue_music)
continue_button.place(x=198+28,y=35)

img7=Image.open('image/7.png')
img7=img7.resize((30,30))
img7=ImageTk.PhotoImage(img7)
stop_button=Button(down_frame,width=40,height=40,image=img7,padx=10,font=("Ivy 10"),command=stop_music)
stop_button.place(x=240+28,y=35)



line=Label(left_frame,width=200,height=1,padx=10,bg=co3)
line.place(x=0,y=1)

line=Label(left_frame,width=200,height=1,padx=10,bg=co1)
line.place(x=0,y=3)

running_song=Label(down_frame,text="choose song",font=("Ivy 10"),width=44,height=1,padx=10,bg=co1,fg=co3,anchor=NW)
running_song.place(x=0,y=1)

os.chdir(r'D:\music plyer\Music')

songs=os.listdir()
def show():
    
    for i in songs:
        listbox.insert(END,i)
show()    

mixer.init()
music_state=StringVar()
music_state.set("choose one")    



window.mainloop()
