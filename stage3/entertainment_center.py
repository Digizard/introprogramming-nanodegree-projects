import media
import fresh_tomatoes

red_trailer = media.Movie("Red Trailer", "Show of RWBY concept with the character Ruby Rose.",
                  "http://lorempixel.com/400/200/", "https://www.youtube.com/watch?v=pYW2GmHB5xs")

white_trailer = media.Movie("White Trailer", "Second RWBY trailer, about character Weiss Schnee.",
                  "http://lorempixel.com/400/200/", "https://www.youtube.com/watch?v=Vt9vl8iAN5Q")

black_trailer = media.Movie("Black Trailer", "Third RWBY trailer, about character Blake Belladonna.",
                  "http://lorempixel.com/400/200/", "https://www.youtube.com/watch?v=ImKCt7BD4U4")

yellow_trailer = media.Movie("Yellow Trailer", "Final RWBY trailer, about character Yang Xiao Long.",
                  "http://lorempixel.com/400/200/", "https://www.youtube.com/watch?v=QCw_aAS7vWI")


movies = [red_trailer, white_trailer, black_trailer, yellow_trailer]
fresh_tomatoes.open_movies_page(movies)