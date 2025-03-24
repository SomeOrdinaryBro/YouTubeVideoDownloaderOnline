# Function to validate YouTube URL
def is_valid_youtube_url(url):
    """Check if the provided URL is a valid YouTube URL."""
    youtube_regex = r'(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/.*'
    return re.match(youtube_regex, url) is not None
