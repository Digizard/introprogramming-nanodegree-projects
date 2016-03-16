import re
import webbrowser


class Playlist():

    """Collection of videos."""

    def __init__(self, playlist_name, item_type, videos=[]):
        self.name = playlist_name
        self.type = item_type
        self.videos = videos
        self.current = 0

    def __iter__(self):
        return self

    def next(self):
        if self.current >= len(self.videos):
            raise StopIteration
        else:
            current_video = self.videos[self.current]
            self.current += 1
            return current_video


class Video():

    """Video-related information."""

    def __init__(self, video_title, youtube_url):
        # initialize instance of class Video
        self.title = video_title
        self.youtube_url = youtube_url
        self.setup_youtube_id()
        self.thumbnail_url = "http://img.youtube.com/vi/" + \
            self.youtube_id + "/mqdefault.jpg"

    def show(self):
        webbrowser.open(self.youtube_url)

    def setup_youtube_id(self):
         # Extract the youtube ID from the url, thanks to original
         # fresh_tomatoes.py code!
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', self.youtube_url) or \
            re.search(r'(?<=be/)[^&#]+', self.youtube_url)
        self.youtube_id = (youtube_id_match.group(0) if youtube_id_match
                           else None)


class Episode(Video):

    """Episode-related information."""

    def __init__(self, episode_number, episode_title, youtube_url):
        # initialize instance of class Episode
        Video.__init__(self, episode_title, youtube_url)
        self.episode_number = episode_number
