# Importing json module to convert a JSON file and turn it into a dict
import json

# Importing urllib2 to handle http requests from the The Movie DB API
from urllib2 import Request, urlopen

# Initializing constant with the API URL and API Key
API_URL = 'http://api.themoviedb.org/3'
API_KEY = '&api_key=e3cef8188dbc6d7f4566943d1ee65a69'

#http://api.themoviedb.org/3/search/movie?query=Scarface&api_key=e3cef8188dbc6d7f4566943d1ee65a69
#http://api.themoviedb.org/3/search/movie?query=Scarface&api_key=e3cef8188dbc6d7f4566943d1ee65a69

# Function that connects to the API and returns the full JSON file converted into a dictionary 
def request_api_json(api_param):
  url = API_URL + api_param + API_KEY
  request = Request(url)
  response_body = urlopen(request).read()
  json_dict = json.loads(response_body)
  return json_dict

# Function that calls request_api_json() functions and returns a specific key from the JSON
def request_api_json_key(api_param, key):
  json_dict = request_api_json(api_param)  
  return json_dict[key]

class Movie():
  def __init__(self, title, story_line, poster_image, trailer_youtube):
    self.title = title
    self.story_line = story_line
    #self.duration = duration
    self.poster_image_url = poster_image
    self.trailer_youtube_url = trailer_youtube




