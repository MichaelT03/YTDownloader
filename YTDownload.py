import tkinter as tk
import ttkbootstrap as ttk
from pytube import YouTube

# Functions
def downloadButtonClick():
    outString.set("Downloading please wait")
    urlString = url.get()
    print(urlString)

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
textBox = ttk.Entry(master = inputFrame, textvariable = url)
downloadButton = ttk.Button(master = inputFrame, text = "Download", command = downloadButtonClick)

textBox.pack(side = "left", padx = 10)
downloadButton.pack(side = "left")
inputFrame.pack(pady = 5)

# Outputs
outString = tk.StringVar()
outLabel = ttk.Label(master = window, font = "Calibri 24", textvariable = outString)
outLabel.pack(pady = 20)

# Run
window.mainloop()