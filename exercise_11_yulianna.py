# Defining the string containing information about Belgium
Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'

#  Print a line of hyphens the same length as the Belgium string
print('-' * len(Belgium))

#  Print the string with comma separators replaced by colons
# Replace commas with colons using the replace() method
print(Belgium.replace(',', ':'))

#  Calculate and print the total population of Belgium and Brussels
# Split the string into a list using commas as the separator
list = Belgium.split(',')

# Extract the population of Belgium (index 1) and Brussels (index 3) from the list
belgium_population = int(list[1])
brussels_population = int(list[3])

# Calculate the total population by adding the populations of Belgium and Brussels
total_population = belgium_population + brussels_population

# Print the total population
print("Total population of Belgium and Brussels:", total_population)
