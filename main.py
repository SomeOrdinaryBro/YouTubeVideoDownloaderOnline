import tkinter
import customtkinter
from yt_dlp import YoutubeDL
import threading

from functions import start_download
from functions import download_video
from functions import is_valid_youtube_url
from functions import normalize_youtube_url
from functions import on_progress
from functions import update_progress

# GUI Setup
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

# Create the main app window
app = customtkinter.CTk()
app.geometry("600x400")
app.title("YouTube Downloader")
app.resizable(False, False)

# Set the app icon (make sure the path is correct)
app.iconbitmap("ytdl.ico")  # Make sure the path is correct, and ytdl.ico exists in your project directory

# UI Elements
title = customtkinter.CTkLabel(app, text="YouTube Downloader", font=("Helvetica", 24, "bold"), text_color="#00BFFF")
title.pack(pady=(30, 20))

instructionLabel = customtkinter.CTkLabel(app, text="Insert the YouTube video link below:", font=("Helvetica", 14), text_color="#FFFFFF")
instructionLabel.pack(pady=(0, 10))

url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=400, height=40, textvariable=url_var, placeholder_text="Enter YouTube URL", fg_color="#333333", text_color="white", border_color="#00BFFF")
link.pack(pady=(0, 30))

finishLabel = customtkinter.CTkLabel(app, text="", font=("Helvetica", 14))
finishLabel.pack()

pPercentage = customtkinter.CTkLabel(app, text="0%", font=("Helvetica", 12))
pPercentage.pack(pady=(10, 10))

progressBar = customtkinter.CTkProgressBar(app, width=400, progress_color="#00BFFF", mode="determinate")
progressBar.set(0)
progressBar.pack(pady=(0, 20))

download_button = customtkinter.CTkButton(app, text="Download", command=start_download, fg_color="#00BFFF", hover_color="#0080FF", width=150, height=40)
download_button.pack(pady=(20, 30))

# Start the GUI loop
app.mainloop()
