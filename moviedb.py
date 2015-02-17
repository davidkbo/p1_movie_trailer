#!/usr/bin/env python

# # Import the imdb package.
# import imdb

# # Create the object that will be used to access the IMDb's database.
# ia = imdb.IMDb()

# # Search for a movie (get a list of Movie objects).
# s_result = ia.search_movie('The Untouchables')

# # Print the long imdb canonical title and movieID of the results.
# for item in s_result:
#    print item

# # Retrieves default information for the first result (a Movie object).


class Movie():  
  #Initializing the variables for the class
  def __init__(self, title, story_line, poster_image, trailer_youtube):
    self.title = title
    self.story_line = story_line
    self.poster_image_url = poster_image
    self.trailer_youtube_url = trailer_youtube
