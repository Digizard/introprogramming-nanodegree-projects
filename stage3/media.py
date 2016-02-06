import re
import webbrowser

class Video():
    """Video-related information."""

    def __init__(self, video_title, youtube_url):
        # initialize instance of class Video
        self.title = video_title
        self.youtube_url = youtube_url
        self.setup_youtube_id()
        self.thumbnail_url = "http://img.youtube.com/vi/" + self.youtube_id + "/mqdefault.jpg"

    def show(self):
        webbrowser.open(self.youtube_url)

    def setup_youtube_id(self):
         # Extract the youtube ID from the url, thanks to original fresh_tomatoes.py code!
        youtube_id_match = re.search(r'(?<=v=)[^&#]+', self.youtube_url) or re.search(r'(?<=be/)[^&#]+', self.youtube_url)
        self.youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)