import moviedb
import fresh_tomatoes

toy_story = moviedb.Movie("Toy Story" , 
  "Story of a boy and his toys that come to life", 
  "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
  "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = moviedb.Movie("Avatar" , "A marine on an alien planet" , 
  "http://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
  "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

scarface = moviedb.Movie("Scarface" , 
  "A determined Cuban immigrant takes over a drug cartel while succumbing to greed." , 
  "http://upload.wikimedia.org/wikipedia/pt/9/9c/Scarfaceposter.jpg",
  "https://www.youtube.com/watch?v=a9LVwNum6rE")

school_of_rock = moviedb.Movie("School of Rock" , 
  "Using rock music to learn" , 
  "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
  "https://www.youtube.com/watch?v=3PsUJFEBC74")

ratatouille = moviedb.Movie("Ratatouille" , 
  "A rat is a chef in Paris" , 
  "http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
  "https://www.youtube.com/watch?v=c3sBBRxDAqk")

midnight_in_paris = moviedb.Movie("Midnight in Paris" , 
  "Going back in time to meet authors" , 
  "http://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
  "https://www.youtube.com/watch?v=BYRWfS2s2v4")

hunger_games = moviedb.Movie("Hunger Games" , 
  "A really real reality show" , 
  "http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
  "https://www.youtube.com/watch?v=PbA63a7H0bo")

movies = [toy_story , avatar , school_of_rock, ratatouille , hunger_games, midnight_in_paris , scarface]

fresh_tomatoes.open_movies_page(movies)