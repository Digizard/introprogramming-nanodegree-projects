import fresh_tomatoes
from media import *

trailers = Playlist("Trailers", [
    Video("Red Trailer", "https://www.youtube.com/watch?v=pYW2GmHB5xs"),
    Video("White Trailer", "https://www.youtube.com/watch?v=Vt9vl8iAN5Q"),
    Video("Black Trailer", "https://www.youtube.com/watch?v=ImKCt7BD4U4"),
    Video("Yellow Trailer", "https://www.youtube.com/watch?v=QCw_aAS7vWI")
])

season1 = Playlist("Season 1", [
    Episode("Ruby Rose", 1, "https://www.youtube.com/watch?v=-sGiE10zNQM"),
    Episode("The Shining Beacon", 2, "https://www.youtube.com/watch?v=sLv6FfHlxmI"),
    Episode("The Shining Beacon, Part 2", 3, "https://www.youtube.com/watch?v=-ZwGeYu2pOQ"),
    Episode("The First Step", 4, "https://www.youtube.com/watch?v=H09KTtyElWQ"),
    Episode("The First Step, Part 2", 5, "https://www.youtube.com/watch?v=1JZgPfbKbU4"),
    Episode("The Emerald Forest", 6, "https://www.youtube.com/watch?v=N1TJ5YA3jfw"),
    Episode("The Emerald Forest, Part 2", 7, "https://www.youtube.com/watch?v=z8wPhihrzvU"),
    Episode("Players and Pieces", 8, "https://www.youtube.com/watch?v=ctiDu69kIho"),
    Episode("The Badge and The Burden", 9, "https://www.youtube.com/watch?v=-E6aeUjfBCM"),
    Episode("The Badge and The Burden Part 2", 10, "https://www.youtube.com/watch?v=57f_t1ioOws"),
    Episode("Jaunedice", 11, "https://www.youtube.com/watch?v=N5D0NDAR8sU"),
    Episode("Jaunedice, Part 2", 12, "https://www.youtube.com/watch?v=M_Loqu0jo7k"),
    Episode("Forever Fall", 13, "https://www.youtube.com/watch?v=h0QiT-GxN6k"),
    Episode("Forever Fall, Part 2", 14, "https://www.youtube.com/watch?v=PS9huFMmSoc"),
    Episode("The Stray", 15, "https://www.youtube.com/watch?v=KHynQoJgbgc"),
    Episode("Black and White", 16, "https://www.youtube.com/watch?v=3b1gs8KrM-M")
])


fresh_tomatoes.open_videos_page([trailers, season1])