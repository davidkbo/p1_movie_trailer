#!/usr/bin/env python

# Import the imdb package.
import imdb

# Create the object that will be used to access the IMDb's database.
ia = imdb.IMDb()

# Search for a movie (get a list of Movie objects).
s_result = ia.search_movie('The Untouchables')

# Print the long imdb canonical title and movieID of the results.
for item in s_result:
   print item

# Retrieves default information for the first result (a Movie object).
the_unt = s_result[0]
ia.update(the_unt)

# # Print some information.
print the_unt['full-size cover url']

# # Get the first item listed as a "goof".
# ia.update(the_unt, 'goofs')
# print the_unt['goofs'][0]

# # The first "trivia" for the first director.
# b_depalma = director[0]
# ia.update(b_depalma)
# print b_depalma['trivia'][0]