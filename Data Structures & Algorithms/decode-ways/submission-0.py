# As question says: we need to decode the message - from numbers to strings 
# One pattern is that : either you group 2 digits together as number can be only upto 26 : have to be in that range or we take only at each step : which makes it from 0 to 9:
# Two more restrictions : can't be 0 either in single or even doublr group start -- you can't start with zero 

# So how do we decode : let's solve using brute force -- recursion first: 
# We have to find number of ways to decode :
# for each index or number : we have two options -- either we include it or take it with the group 
# with given constraint is that : no starting zero ; ending can be zero 
# reoccurence relation for it :  no_of_ways = way(new-string excluding one only) + way(excluding two)
# talk about constraints: when does it stops : when it is just a single number or last index : answer becomes = 1 ; and if no number after it, becomes 0  -- that's the base case (general)
# conditions for two grouping : number should be in limit : 10 <= x <= 26
# condition for single number: 0 < x <= 9  

# it should return the number of ways in last 

# function protoype: input -- string and index : for being update where to start 
class Solution:
    def numDecodings(self, s: str) -> int:
        cache = {}
        def ways(index):
            if index == len(s):
                return 1
            if s[index] == '0' : return 0
            # form the number:
            if index in cache: 
                return cache[index]

            branch1 = ways(index + 1)
            branch2 = 0 

            if index + 1 and 10 <= int(s[index: index + 2]) <= 26: branch2 = ways(index + 2)
            # now grouping rules : as in this we may group a number like 41 ; so can't do that
            no_of_ways = branch1 + branch2
            cache[index] = no_of_ways 
            return no_of_ways
        return ways(0)