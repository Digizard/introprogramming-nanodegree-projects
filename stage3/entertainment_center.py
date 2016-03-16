import fresh_tomatoes
from media import *

page_title = "RWBY Theater"

trailers = Playlist("Trailers", "Trailer", [
    Video("Red Trailer",    "https://www.youtube.com/watch?v=pYW2GmHB5xs"),
    Video("White Trailer",  "https://www.youtube.com/watch?v=Vt9vl8iAN5Q"),
    Video("Black Trailer",  "https://www.youtube.com/watch?v=ImKCt7BD4U4"),
    Video("Yellow Trailer", "https://www.youtube.com/watch?v=QCw_aAS7vWI")
])

volume1 = Playlist("Volume 1", "Chapter", [
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

volume2 = Playlist("Volume 2", "Chapter", [
    Episode(1,    "Best Day Ever",
                  "https://www.youtube.com/watch?v=PzPZ6joXq5Y"),
    Episode(2,    "Welcome to Beacon",
                  "https://www.youtube.com/watch?v=bdiV-w3yXos"),
    Episode(3,    "A Minor Hiccup",
                  "https://www.youtube.com/watch?v=mj3jfqPwJEk"),
    Episode(4,    "Painting the Town...",
                  "https://www.youtube.com/watch?v=a1EuyliSO_Q"),
    Episode(4.5,  "World of Remnant: Dust",
                  "https://www.youtube.com/watch?v=9BJc7nrMnc4"),
    Episode(5,    "Extracurricular",
                  "https://www.youtube.com/watch?v=nur1pCHD4hU"),
    Episode(6,    "Burning the Candle",
                  "https://www.youtube.com/watch?v=i7wkw3yEbvQ"),
    Episode(7,    "Dance Dance Infiltration",
                  "https://www.youtube.com/watch?v=0-f-mGvOba8"),
    Episode(7.5,  "World of Remnant: Kingdoms",
                  "https://www.youtube.com/watch?v=AvUT2rHKJDs"),
    Episode(8,    "Field Trip",
                  "https://www.youtube.com/watch?v=bSdejzDaQEU"),
    Episode(9,    "Search and Destroy",
                  "https://www.youtube.com/watch?v=GJGSywhNk8Q"),
    Episode(10,   "Mountain Glenn",
                  "https://www.youtube.com/watch?v=lD4x6NiTiM4"),
    Episode(10.5, "World of Remnant: Grimm",
                  "https://www.youtube.com/watch?v=-PE66fmjZ0I"),
    Episode(11,   "No Brakes",
                  "https://www.youtube.com/watch?v=CUYhvPoxuas"),
    Episode(12,   "Breach",
                  "https://www.youtube.com/watch?v=-p4iS_p3b8E")
])

volume3 = Playlist("Volume 3", "Chapter", [
    Episode(0.5,  "World of Remnant: Vytal Festival Tournament",
                  "https://www.youtube.com/watch?v=946xgoU4fkQ"),
    Episode(1,    "Round One",
                  "https://www.youtube.com/watch?v=W9wyWgvyp0s"),
    Episode(2,    "New Challengers...",
                  "https://www.youtube.com/watch?v=RzEo0F8thL4"),
    Episode(3,    "It's Brawl in the Family",
                  "https://www.youtube.com/watch?v=vCO2mw4SlDM"),
    Episode(3.5,  "World of Remnant: Huntsmen",
                  "https://www.youtube.com/watch?v=k6rZFLYHZfI"),
    Episode(4,    "Lessons Learned",
                  "https://www.youtube.com/watch?v=fBy2W99zaLQ"),
    Episode(5,    "Never Miss a Beat",
                  "https://www.youtube.com/watch?v=G5uFH7gIClw"),
    Episode(6,    "Fall",
                  "https://www.youtube.com/watch?v=moxtu3AuA4s"),
    Episode(6.5,  "World of Remnant: Cross Continental Transmit System",
                  "https://www.youtube.com/watch?v=yiJU9QeG89g"),
    Episode(7,    "Beginning of the End",
                  "https://www.youtube.com/watch?v=FFf7qoIDYuQ"),
    Episode(8,    "Destiny",
                  "https://www.youtube.com/watch?v=u7uU_tKYHiM"),
    Episode(9,    "PvP",
                  "https://www.youtube.com/watch?v=_iq4xplqeI0"),
    Episode(9.5,  "World of Remnant: The Four Maidens",
                  "https://www.youtube.com/watch?v=2bBSQA3uXVo"),
    Episode(10,   "Battle of Beacon",
                  "https://www.youtube.com/watch?v=bIKyZi2q8w8"),
    Episode(11,   "Heroes and Monsters",
                  "https://www.youtube.com/watch?v=pT1XiUbJu_Y"),
    Episode(12,   "End of the Beginning",
                  "https://www.youtube.com/watch?v=hq1lk-QWxNg")
])

playlists = [trailers, volume1, volume2, volume3]
fresh_tomatoes.open_playlists_page(page_title, playlists)
