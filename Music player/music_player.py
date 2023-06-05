#importing libraries
import tkinter as tk
import fnmatch
import os
from pygame import mixer

#initializing the window, path, label, box etc...
window = tk.Tk()
window.title("Music Player")
window.geometry("1000x600")
window.config(bg="blue")
path = "\music"
pat = "*.mp3"
box = tk.Listbox(window, fg="black", bg="blue", width=100, font = ('tahoma', 16))
box.pack(padx=10,pady=10)
l = tk.Label(window,text='',bg='blue', fg='green', font=('tahoma', 20))
l.pack(pady=10)
mixer.init()
prev_image = tk.PhotoImage(file="prev.png")
next_image = tk.PhotoImage(file="next.png")
stop_image = tk.PhotoImage(file="stop.png")
play_image = tk.PhotoImage(file="play.png")
pause_image = tk.PhotoImage(file="pause.png")

#code for all the buttons
def choice():
    l.config(text=box.get("anchor"))
    mixer.music.load(path+"//"+box.get("anchor"))
    mixer.music.play()
def stop():
    mixer.music.stop()
    box.select_clear('active')
    l.config(text="")
def next():
    next_music = box.curselection()
    next_music = next_music[0]+1
    next_music_name = box.get(next_music)
    l.config(text=next_music_name)
    mixer.music.load(path+"//"+next_music_name)
    mixer.music.play()
    box.select_clear(0,'end')
    box.activate(next_music)
    box.select_set(next_music)
def prev():
    prev_music = box.curselection()
    prev_music = prev_music[0]-1
    prev_music_name = box.get(prev_music)
    l.config(text=prev_music_name)
    mixer.music.load(path+"//"+prev_music_name)
    mixer.music.play()
    box.select_clear(0,'end')
    box.activate(prev_music)
    box.select_set(prev_music)
def pause():
    if pause["text"] == "Pause":
        mixer.music.pause()
        pause["text"] = "Play"
    else:
        mixer.music.unpause()
        pause["text"] = "Pause"

#frame and showing the buttons
fr = tk.Frame(window, bg="blue")
fr.pack(padx=10,pady=10, anchor="center")
prev = tk.Button(window,text="Prev", image=prev_image,bg="blue",borderwidth=0, command=prev)
prev.pack(pady=10, in_=fr, side="left")
stop = tk.Button(window,text="Stop",image=stop_image,bg="blue",borderwidth=0, command=stop)
stop.pack(pady=10,in_=fr, side="left") 
play = tk.Button(window,text="Play",image=play_image,bg="blue",borderwidth=0, command=choice)
play.pack(pady=10,in_=fr, side="left") 
pause = tk.Button(window,text="Pause",image=pause_image,bg="blue",borderwidth=0, command=pause)
pause.pack(pady=10,in_=fr, side="left") 
next = tk.Button(window,text="Next",image=next_image,bg="blue",borderwidth=0, command=next)
next.pack(pady=10,in_=fr, side="left") 

for r,d,f in os.walk(path):
    for name in fnmatch.filter(f,pat):
        box.insert('end',name)

window.mainloop()