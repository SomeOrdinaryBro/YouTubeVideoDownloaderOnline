# Function to download the video
def download_video(url, progressBar, finishLabel):
    """Download the YouTube video."""
    try:
        # Download the video
        ydl_opts = {
            'quiet': False,
            'progress_hooks': [lambda d: update_progress(d, progressBar)],
        }
        
        with YoutubeDL(ydl_opts) as ydl:
            finishLabel.configure(text="Downloading...", text_color="yellow")
            ydl.download([url])

        finishLabel.configure(text="Download completed!", text_color="green")
    except Exception as e:
        finishLabel.configure(text=f"Error occurred: {e}", text_color="red")