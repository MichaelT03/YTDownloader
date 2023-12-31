import tkinter as tk
import ttkbootstrap as ttk
import re
import os
import threading
from pytube import YouTube
from pytube.exceptions import VideoUnavailable

videoDirectory = os.path.join("Downloads", "Video")
audioDirectory = os.path.join("Downloads", "Audio")

# Functions #
def printMessage(message):
    outString.set(message)
    
    # Wait 2 seconds before beginning download
    window.after(2000)

## Video functions
def validateVideoUrl():
    #reinitialize outputs
    outString.set(" ")
    titleString.set(" ")
    waitString.set(" ")
    completeString.set(" ")
    
    urlString = url.get()

    if not re.match("https?://(www\.)?youtube\.com/watch\?v=", urlString):
        outString.set("Invalid YouTube URL")
    else:
        getVideo(urlString)

def getVideo(urlString):
    printMessage("Downloading video...")

    try:
        yt = YouTube(urlString)
    except VideoUnavailable:
        outString.set("An error has occured while trying to access video")
        titleString.set("The video may be region blocked, age restricted, or private")
    else:
        titleString.set(yt.title)
        waitString.set("Please wait for 'Download Complete' prompt")

        #create a thread for downloading a video so that the GUI doesn't lock up and crash if it takes to long to download
        #this allows videos longer than ~10 minutes to be downloaded
        downloadThread = threading.Thread(target = downloadVideo, args = (yt,))
        downloadThread.start()
    
def downloadVideo(yt):
    try:
        yd = yt.streams.get_highest_resolution()
    except VideoUnavailable:
        outString.set("An error has occured while trying to access video")
        titleString.set("The video may be region blocked, age restricted, or private")
        waitString.set(" ")
    else:
        yd.download(videoDirectory)

        window.after(0, lambda: completeString.set("Download complete"))

## Audio functions
def validateAudioUrl():
    #reinitialize outputs
    outString.set(" ")
    titleString.set(" ")
    waitString.set(" ")
    completeString.set(" ")

    urlString = url.get()

    if not re.match("https?://(www\.)?youtube\.com/watch\?v=", urlString):
        outString.set("Invalid YouTube URL")
    else:
        getAudio(urlString)

def getAudio(urlString):
    printMessage("Downloading audio...")

    try:
        yt = YouTube(urlString)
    except VideoUnavailable:
        outString.set("An error has occured while trying to access video")
        titleString.set("The video may be region blocked, age restricted, or private")
    else:
        titleString.set(yt.title)
        waitString.set("Please wait for 'Download Complete' prompt")

        # agrs has a comma because it is a touple
        downloadThread = threading.Thread(target = downloadAudio, args = (yt,))
        downloadThread.start()

def downloadAudio(yt):
    try:
        yd = yt.streams.get_audio_only()
    except VideoUnavailable:
        outString.set("An error has occured while trying to access video")
        titleString.set("The video may be region blocked, age restricted, or private")
        waitString.set(" ")
    else:
        yd.download(audioDirectory)

        window.after(0, lambda: completeString.set("Download complete"))


# Tkinter #

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
textBox = ttk.Entry(master = inputFrame, textvariable = url, width = 75)
videoButton = ttk.Button(master = inputFrame, text = "Download Video", command = validateVideoUrl, width = 20)
audioButton = ttk.Button(master = inputFrame, text = "Download Only Audio", command = validateAudioUrl)

textBox.pack(side = "left", padx = 5)
videoButton.pack(side = "left", padx = 5)
audioButton.pack(side = "left")
inputFrame.pack(pady = 20)

# Outputs
outString = tk.StringVar()
titleString = tk.StringVar()
waitString = tk.StringVar()
completeString = tk.StringVar()

outLabel = ttk.Label(master = window, font = "Calibri 24", textvariable = outString)
vidTitle = ttk.Label(master = window, font = "Calibri 12", textvariable = titleString)
waitLabel = ttk.Label(master = window, font = "Calibri 24", textvariable = waitString)
completeLabel = ttk.Label(master = window, font = "Calibri 24", textvariable = completeString)

outLabel.pack(pady = 20)
vidTitle.pack()
waitLabel.pack(pady = 20)
completeLabel.pack(pady = 30)

# Run
window.mainloop()