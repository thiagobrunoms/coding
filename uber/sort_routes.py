# Given a list of [origin, destination] pairs (you can think of them as plane tickets), sort them into a single continuous route


from audioop import reverse
from inspect import BoundArguments


class Solution:
    def __init__(self, origin_destinations):
        self.origin_destinations = origin_destinations

    def sort_hash_based(self):
        destinations = {}
        # The strategy: reverse 'from->to' destinations to 'to->from'.
        # Hence, the starting point will not be as a 'to' in the reversed 'to->from' list.
        reverse_destinations = {}
        for pair in self.origin_destinations:
            reverse_destinations[pair[1]] = pair[0]
            destinations[pair[0]] = pair[1]

        starting_point = None
        for routes in self.origin_destinations:
            if routes[0] not in reverse_destinations:
                starting_point = routes[0]

        while starting_point in destinations:
            print('starting_point', starting_point,
                  'next dest', destinations[starting_point])
            starting_point = destinations[starting_point]


origin_destinations = [["Chennai", "Banglore"], [
    "Bombay", "Delhi"], ["Goa", "Chennai"], ["Delhi", "Goa"]]

s = Solution(origin_destinations)
s.sort_hash_based()
