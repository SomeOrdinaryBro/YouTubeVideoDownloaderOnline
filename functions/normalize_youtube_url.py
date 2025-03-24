# Function to normalize YouTube URL
def normalize_youtube_url(url):
    """Ensure the YouTube URL is in a normalized format."""
    if not url.startswith('https://'):
        url = 'https://' + url
    if 'youtu.be' in url:
        url = url.replace('youtu.be', 'www.youtube.com/watch')
    return url