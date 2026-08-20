class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cache = {}
        def canbreak(index): 
                # now the base case : when does it stops and gievs : true or false
            if index in cache: return cache[index]
            if index == len(s):
                return True
            result = False
            for end in range(index + 1, len(s) + 1):
                word = s[index:end]
                if word in wordDict and canbreak(end):
                        result = True
                        break
                # check if it is in dict : string slice
                # elif s[:index] in wordDict: 
                    # if found yes: that's the break point ( before string ends )
                    # return word(s,index + 1) # go and seach again for the next word
            cache[index] = result
            return result
                    
                # if not continue : tracing the string until end 
        return canbreak(0)