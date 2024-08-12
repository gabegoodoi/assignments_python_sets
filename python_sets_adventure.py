'''
Objective: The aim of this assignment is to deepen your understanding and application of Python sets.

Task 1: Flight Route Comparison 
Imagine you work for an airline and need to compare the flight routes of your airline with a competitor. You have two sets of flight destinations, one for each airline. Write a Python program to find out:

1. Destinations that both airlines fly to.
2. Destinations unique to your airline.
3. Whether there are any destinations that neither airline shares.

Example Code:

our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

'''
our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

# 1. Destinations that both airlines fly to.
shared_dest = our_routes.intersection(competitor_routes)

# 2. Destinations unique to your airline.
my_exclusives = our_routes.difference(competitor_routes)

# 3. Whether there are any destinations that neither airline shares. This question confused me so I'm going to solve it in two ways (A) & (B)

# (A) This returns a single set to us containing which destinations are unique to our_routes and which routes a are unique to our competitors.
exclusive_dest = our_routes.symmetric_difference(competitor_routes)

# (B) This is a conditional that prints whether a user inputted destination is in either set.
dest_query = input("What destination would you like to check? (enter 3-digit airport code): ").upper()
if dest_query not in our_routes.union(competitor_routes):
    print(f"neither airline goes to {dest_query}")
else:
    print(f"an airline goes to {dest_query}")
