import webbrowser


class Movie():
    """This class is made to define functions needed for movie project"""

# Defining "Movie" class with all four attributes

    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """Additional Function"""
        webbrowser.open(self.trailer_youtube_url)
