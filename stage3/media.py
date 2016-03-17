"""Defines classes for storing and organizing video information."""
import re
import webbrowser


class Playlist():

    """Collection of videos.

    Attributes:
        title: Title of playlist.
        type: Label for each individual video.
        videos: List of videos.
        current: Current iterator position within video list.

    """

    def __init__(self, playlist_title, item_type, videos=[]):
        """Initialize instance of class Playlist.

        Args:
            playlist_title: Title of playlist.
            item_type: Label for each individual video.
            videos: List of videos.

        """
        self.title = playlist_title
        self.type = item_type
        self.videos = videos
        self.current = 0

    def __iter__(self):
        """Makes Playlist objects iterable."""
        return self

    def next(self):
        """Gets next item when Playlist is being iterated.

        Returns:
            Video: Next video in the list.

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

    """Video-related information

    Attributes:
        title: Title of video.
        youtube_url: URL for video on YouTube.
        youtube_id: ID of video on YouTube.
        thumbnail_url: URL to YouTube video image.

    """

    def __init__(self, video_title, youtube_url):
        """Initialize instance of class Video.

        Args:
            video_title: Title of video.
            youtube_url: URL for video on YouTube.

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
        """Extract the YouTube ID from the URL and store it."""
        # Thanks to original fresh_tomatoes.py code from Udacity!
        youtube_id_match = re.search(r'(?<=v=)[^&#]+', self.youtube_url) or \
            re.search(r'(?<=be/)[^&#]+', self.youtube_url)
        self.youtube_id = (youtube_id_match.group(0) if youtube_id_match
                           else None)


class Episode(Video):

    """Episode-related information.

    Attributes:
        title: Title of episode.
        youtube_url: URL for the video on YouTube.
        youtube_id: ID of video on YouTube.
        thumbnail_url: URL to YouTube video image.
        number: Number associated with episode.

    """

    def __init__(self, episode_number, episode_title, youtube_url):
        """Initialize instance of class Episode.

        Args:
            episode_number: Number associated with episode.
            episode_title: Title of episode.
            youtube_url: URL for the video on YouTube.

        """
        Video.__init__(self, episode_title, youtube_url)
        self.number = episode_number
