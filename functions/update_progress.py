# Function to update progress bar
def update_progress(d, progressBar):
    """Update the progress bar during the video download."""
    if d['status'] == 'downloading':
        progress = d.get('downloaded_bytes', 0) / d.get('total_bytes', 1)
        progressBar.set(progress)