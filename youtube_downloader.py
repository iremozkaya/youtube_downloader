import yt_dlp
import tkinter as tk
from tkinter import messagebox

def download():
    global status_label
    url = box.get()
    if not url:
        status_label.config(text="please enter an URL")
        return
       
    ydl_opts = {
        'format': 'best',
        'outtmpl': r'C:\Users\LENOVO\OneDrive\Belgeler\PYTHON KODLARIM\yt_downloader\indirdiklerim"\%(title)s.(ext)s'
    }

    try:
        status_label.config(text="Downloading, please wait.") 
        window.update()

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        status_label.config(text="Succesfully downloaded",fg="green")
    except:
        status_label.config(text="error.",fg="red")

window=tk.Tk()
window.title("Youtube Downloader")
window.geometry("500x300")

label=tk.Label(window,text="Enter URL: ",font=(11))
label.pack(pady=50)

status_label=tk.Label(window, text="")
status_label.pack(pady=20)

box=tk.Entry(window)
box.pack(pady=10)

button=tk.Button(window,text="Download video", command=download)
button.pack(pady=5)

window.mainloop()
