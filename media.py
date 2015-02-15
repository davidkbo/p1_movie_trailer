import webbrowser 
class Movie():
  """Parent class to reuse (self, title, story_line, duration, poster_image, trailer_youtube) for TV series and movies"""
  
  #Initializing the variables for the class
  def __init__(self, title, story_line, poster_image, trailer_youtube):
    self.title = title
    self.story_line = story_line
    #self.duration = duration
    self.poster_image_url = poster_image
    self.trailer_youtube_url = trailer_youtube


# class Movie(Video):
#   """This class provides a way to store movie related information"""

#   def __init__(self, movie_title, movie_storyline, duration, poster_image, trailer_youtube):
#     Video.__init__(self, movie_title, duration, poster_image, trailer_youtube) 
#     self.movie_storyline = movie_storyline
    
   
# class TvShow(Video):
#   """This class creates a Tv show, """
  
#   def __init__(self, title, season, episode, tv_station):
#     Video.__init__(self, title, duration, poster_image, trailer_youtube)
#     self.season = season
#     self.episode = episode
#     self.tv_station = tv_station
  
#     print()
    