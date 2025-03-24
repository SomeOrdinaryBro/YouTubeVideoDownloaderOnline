# Function to start the download in a separate thread
def start_download():
    """Start downloading the video in a separate thread."""
    url = url_var.get()
    if not url:
        finishLabel.configure(text="Please enter a valid URL.", text_color="red")
        return
    
    # Start downloading in a separate thread to avoid blocking the GUI
    download_thread = threading.Thread(target=download_video, args=(url, progressBar, finishLabel))
    download_thread.start()