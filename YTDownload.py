import tkinter as tk
import ttkbootstrap as ttk
import os
from pytube import YouTube

videoDirectory = os.path.join("Downloads", "Video")
audioDirectory = os.path.join("Downloads", "Audio")

# Functions
def mp4ButtonClick():
    urlString = url.get()
    yt = YouTube(urlString)
    outString.set("Downloading...")
    titleString.set(yt.title)
    yd = yt.streams.get_highest_resolution()
    yd.download(videoDirectory)

def mp3ButtonClick():
    titleString.set("mp3 button pressed")

# Window
window = ttk.Window(themename = "darkly")
window.title("YouTube Video Downloader")
window.geometry("800x500")

# Heading
heading1 = ttk.Label(master = window, text = "Paste a Youtube URL into the text field", font = "Calibri 24 bold")
heading1.pack(pady = 10)
heading2 = ttk.Label(master = window, text = "and select the file type you would like to download", font = "Calibri 24 bold")
heading2.pack()

# Inputs
inputFrame = ttk.Frame(master = window)
url = tk.StringVar()
textBox = ttk.Entry(master = inputFrame, textvariable = url, width = 50)
mp4Button = ttk.Button(master = inputFrame, text = "Download", command = mp4ButtonClick)

textBox.pack(side = "left", padx = 10)
mp4Button.pack(side = "left")
inputFrame.pack(pady = 20)

# Outputs
outString = tk.StringVar()
titleString = tk.StringVar()
outLabel = ttk.Label(master = window, font = "Calibri 24", textvariable = outString)
vidTitle = ttk.Label(master = window, font = "Calibri 12", textvariable = titleString)
outLabel.pack(pady = 20)
vidTitle.pack()

# Run
window.mainloop()