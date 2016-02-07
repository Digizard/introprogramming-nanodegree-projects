import fresh_tomatoes
from media import *

trailers = Playlist("Trailers", [
    Video("Red Trailer",    "https://www.youtube.com/watch?v=pYW2GmHB5xs"),
    Video("White Trailer",  "https://www.youtube.com/watch?v=Vt9vl8iAN5Q"),
    Video("Black Trailer",  "https://www.youtube.com/watch?v=ImKCt7BD4U4"),
    Video("Yellow Trailer", "https://www.youtube.com/watch?v=QCw_aAS7vWI")
])

season1 = Playlist("Season 1", [
    Episode(1,  "Ruby Rose",
                "https://www.youtube.com/watch?v=-sGiE10zNQM"),
    Episode(2,  "The Shining Beacon",
                "https://www.youtube.com/watch?v=sLv6FfHlxmI"),
    Episode(3,  "The Shining Beacon, Part 2",
                "https://www.youtube.com/watch?v=-ZwGeYu2pOQ"),
    Episode(4,  "The First Step",
                "https://www.youtube.com/watch?v=H09KTtyElWQ"),
    Episode(5,  "The First Step, Part 2",
                "https://www.youtube.com/watch?v=1JZgPfbKbU4"),
    Episode(6,  "The Emerald Forest",
                "https://www.youtube.com/watch?v=N1TJ5YA3jfw"),
    Episode(7,  "The Emerald Forest, Part 2",
                "https://www.youtube.com/watch?v=z8wPhihrzvU"),
    Episode(8,  "Players and Pieces",
                "https://www.youtube.com/watch?v=ctiDu69kIho"),
    Episode(9,  "The Badge and The Burden",
                "https://www.youtube.com/watch?v=-E6aeUjfBCM"),
    Episode(10, "The Badge and The Burden Part 2",
                "https://www.youtube.com/watch?v=57f_t1ioOws"),
    Episode(11, "Jaunedice",
                "https://www.youtube.com/watch?v=N5D0NDAR8sU"),
    Episode(12, "Jaunedice, Part 2",
                "https://www.youtube.com/watch?v=M_Loqu0jo7k"),
    Episode(13, "Forever Fall",
                "https://www.youtube.com/watch?v=h0QiT-GxN6k"),
    Episode(14, "Forever Fall, Part 2",
                "https://www.youtube.com/watch?v=PS9huFMmSoc"),
    Episode(15, "The Stray",
                "https://www.youtube.com/watch?v=KHynQoJgbgc"),
    Episode(16, "Black and White",
                "https://www.youtube.com/watch?v=3b1gs8KrM-M")
])


fresh_tomatoes.open_playlists_page([trailers, season1])
