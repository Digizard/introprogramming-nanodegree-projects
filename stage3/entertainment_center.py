import fresh_tomatoes
import media

red_trailer = media.Video("Red Trailer", "https://www.youtube.com/watch?v=pYW2GmHB5xs")

white_trailer = media.Video("White Trailer", "https://www.youtube.com/watch?v=Vt9vl8iAN5Q")

black_trailer = media.Video("Black Trailer", "https://www.youtube.com/watch?v=ImKCt7BD4U4")

yellow_trailer = media.Video("Yellow Trailer", "https://www.youtube.com/watch?v=QCw_aAS7vWI")


videos = [red_trailer, white_trailer, black_trailer, yellow_trailer]
fresh_tomatoes.open_videos_page(videos)