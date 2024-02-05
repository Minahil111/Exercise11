#!/usr/bin/python

Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'

# Part A
# used len to cound the number of characters in the string and returned them as a hypen using * wild card
belgium_count = len(Belgium)
print("-" * (belgium_count))

# Part B
# used .replace to find 'old' criteria the comma and replace with new criteria the colon
belgium_replace = Belgium.replace(",", ":")
print(belgium_replace)

# Part c
# list will need to be split as there are no spaces or individual speach marks separating them
# using int and number position to return the numbers and added them together
# used f string to comment what the value being returned is
Belgium_list = Belgium.split(",")
print(Belgium_list)

Belgium_population = int(Belgium_list[1])
Brussels_population = int(Belgium_list[3])
total_population = Belgium_population + Brussels_population
print(f"Total combined population:", total_population)
