"""creating a classdescribing thr behaviour of a movie
  Args:
    movie_title: name of a picture to which it is related to
    poster_image: URL of an imaga displayed on the screen
    trailer_youtube: link of a video that will be played when user clicks on
    the image
 Methods:
  show_trailer(): to play the video"""


# !usr/bin/env python
import webbrowser


class Movie():
    # creating a list that have 4 elements
    VALID_RATINGS = ["EXCELLENT", "GOOD", "BAD", "AVERAGE"]
    # defining a constructor to initialise the passed values

    def __init__(self, movie_title, poster_image, trailer_youtube):
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
