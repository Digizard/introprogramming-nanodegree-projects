import re
import webbrowser


class Playlist():

    """Collection of videos."""

    def __init__(self, playlist_name, item_type, videos=[]):
        """Initialize instance of class Playlist.

        Args:
            playlist_name: Title of playlist.
            item_type: What to refer to each item as.
            videos: A list of videos.

        """
        self.name = playlist_name
        self.type = item_type
        self.videos = videos
        self.current = 0

    def __iter__(self):
        """Makes Playlist objects iterable."""
        return self

    def next(self):
        """Gets next item when Playlist is being iterated.

        Returns:
            Video: The next video in the list.

        Raises:
            StopIteration: If there are no more videos in the list.

        """
        if self.current >= len(self.videos):
            raise StopIteration
        else:
            current_video = self.videos[self.current]
            self.current += 1
            return current_video


class Video():

    """Video-related information"""

    def __init__(self, video_title, youtube_url):
        """Initialize instance of class Video.

        Args:
            video_title: The title of the video.
            youtube_url: The URL for the video on YouTube.

        """
        self.title = video_title
        self.youtube_url = youtube_url
        self.setup_youtube_id()
        self.thumbnail_url = 'http://img.youtube.com/vi/' + \
            self.youtube_id + '/mqdefault.jpg'

    def show(self):
        """Opens the YouTube URL of the video in the browser."""
        webbrowser.open(self.youtube_url)

    def setup_youtube_id(self):
        """Extract the YouTube ID from the URL."""
        # Thanks to original fresh_tomatoes.py code from Udacity!
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', self.youtube_url) or \
            re.search(r'(?<=be/)[^&#]+', self.youtube_url)
        self.youtube_id = (youtube_id_match.group(0) if youtube_id_match
                           else None)


class Episode(Video):

    """Episode-related information."""

    def __init__(self, episode_number, episode_title, youtube_url):
        """Initialize instance of class Episode.

        Args:
            episode_number: The number associated with the episode.
            episode_title: The title of the episode.
            youtube_url: The URL for the episode on YouTube.

        """
        Video.__init__(self, episode_title, youtube_url)
        self.episode_number = episode_number
