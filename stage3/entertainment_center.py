import fresh_tomatoes
import media

red_trailer = media.Video("Red Trailer", "https://www.youtube.com/watch?v=pYW2GmHB5xs")

white_trailer = media.Video("White Trailer", "https://www.youtube.com/watch?v=Vt9vl8iAN5Q")

black_trailer = media.Video("Black Trailer", "https://www.youtube.com/watch?v=ImKCt7BD4U4")

yellow_trailer = media.Video("Yellow Trailer", "https://www.youtube.com/watch?v=QCw_aAS7vWI")

season1 = [
    media.Episode("Ruby Rose", 1, "https://www.youtube.com/watch?v=-sGiE10zNQM"),
    media.Episode("The Shining Beacon", 2, "https://www.youtube.com/watch?v=sLv6FfHlxmI"),
    media.Episode("The Shining Beacon, Part 2", 3, "https://www.youtube.com/watch?v=-ZwGeYu2pOQ"),
    media.Episode("The First Step", 4, "https://www.youtube.com/watch?v=H09KTtyElWQ"),
    media.Episode("The First Step, Part 2", 5, "https://www.youtube.com/watch?v=1JZgPfbKbU4"),
    media.Episode("The Emerald Forest", 6, "https://www.youtube.com/watch?v=N1TJ5YA3jfw"),
    media.Episode("The Emerald Forest, Part 2", 7, "https://www.youtube.com/watch?v=z8wPhihrzvU"),
    media.Episode("Players and Pieces", 8, "https://www.youtube.com/watch?v=ctiDu69kIho"),
    media.Episode("The Badge and The Burden", 9, "https://www.youtube.com/watch?v=-E6aeUjfBCM"),
    media.Episode("The Badge and The Burden Part 2", 10, "https://www.youtube.com/watch?v=57f_t1ioOws"),
    media.Episode("Jaunedice", 11, "https://www.youtube.com/watch?v=N5D0NDAR8sU"),
    media.Episode("Jaunedice, Part 2", 12, "https://www.youtube.com/watch?v=M_Loqu0jo7k"),
    media.Episode("Forever Fall", 13, "https://www.youtube.com/watch?v=h0QiT-GxN6k"),
    media.Episode("Forever Fall, Part 2", 14, "https://www.youtube.com/watch?v=PS9huFMmSoc"),
    media.Episode("The Stray", 15, "https://www.youtube.com/watch?v=KHynQoJgbgc"),
    media.Episode("Black and White", 16, "https://www.youtube.com/watch?v=3b1gs8KrM-M")
    ]


videos = [red_trailer, white_trailer, black_trailer, yellow_trailer]
fresh_tomatoes.open_videos_page(videos + season1)