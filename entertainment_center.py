import media
import fresh_tomatoes

# Creating objects of Class "Movie", defined in "media" file.

tfios = media.Movie("The Fault in Our Stars",
                    "Teenager Hazel Grace's life changes when she meets "
                    "Augustus Waters at a cancer support group.",
                    "https://s-media-cache-ak0.pinimg.com/564x/57/21/0d/57210dc6091a28891e257242afd36eac.jpg",  # NOQA
                    "https://www.youtube.com/watch?v=9ItBvH5J6ss")

interstellar = media.Movie("Interstellar",
                           "In the future, Earth is slowly becoming "
                           "uninhabitable.",
                           "http://t1.gstatic.com/images?q=tbn:ANd9GcRf61mker2o4KH3CbVE7Zw5B1-VogMH8LfZHEaq3UdCMLxARZAB",  # NOQA
                           "https://www.youtube.com/watch?v=zSWdZVtXT7E")

inception = media.Movie("Inception",
                        "Cobb steals information from his targets by entering "
                        "their dreams.",
                        "http://t2.gstatic.com/images?q=tbn:ANd9GcRo9vfJCM6dzPkZHIHBVCtlJnAnew9Ai26kEdrli0-tfmatmciD",  # NOQA
                        "https://www.youtube.com/watch?v=66TuSJo4dZM")

tdknight = media.Movie("The Dark Knight",
                       "Batman has a new foe, the Joker, who is an "
                       "accomplished criminal hell-bent on decimating "
                       "Gotham City.",
                       "http://www.gstatic.com/tv/thumb/movieposters/173378/p173378_p_v8_aa.jpg",  # NOQA
                       "https://www.youtube.com/watch?v=EXeTwQWrcwY")

tmfe = media.Movie("The Man from Earth",
                   "College professors discuss many topics with a colleague "
                   "who claims to be thousands of years old.",
                   "http://www.gstatic.com/tv/thumb/dvdboxart/174565/p174565_d_v8_aa.jpg",  # NOQA
                   "https://www.youtube.com/watch?v=9mOIxyRTY5I")

avatar = media.Movie("Avatar",
                     "Jake, a paraplegic marine, replaces his brother on the "
                     "Na'vi inhabited Pandora for a corporate mission.",
                     "http://t0.gstatic.com/images?q=tbn:ANd9GcQCfmvrE4fMo2cd8esc7mDZPtFSJThAujddMPkRtti1_ij6u-jp",  # NOQA
                     "https://www.youtube.com/watch?v=cRdxXPV9GNQ")


movies = [tfios, interstellar, inception, tdknight, tmfe, avatar]

# Parsing "movies" array into "open_movies_page" function from
# "fresh_tomatoes.py" file

fresh_tomatoes.open_movies_page(movies)
