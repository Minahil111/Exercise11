#!/usr/bin/python

Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'
print(Belgium)

# using len, define a variable that refers to length of the string
# create a variable that multiplies the length of string with a hyphen
# this will print as many hyphens as needed for the length of string
belgium_length = len(Belgium)
hyphen_line = belgium_length * '-'
print(hyphen_line)

# define the original separator in the string - comma
# define desired new separator - colon
# use .replace method to replace the old with the new
# i.e. string.replace(original, new)
comma = ','
colon = ':'
print(Belgium.replace(comma, colon))

# .split method splits the string at a defined seperator
# so here it is a comma, therefore at each occurrence of a comma, the string will split
elements = Belgium.split(',')

# the int function converts a given string value to an integer
# define two populations as integers, so they can be added
# elements[1] retrieves the 2nd value in 'elements' as they have now been split
# elements it is essentially a list
# elements[0] would retrieve 1st value and so forth
population_belgium = int(elements[1])
population_brussels = int(elements[3])

# use addition to add the two  integer variables and print sum
total_population = population_brussels + population_belgium
print(total_population)