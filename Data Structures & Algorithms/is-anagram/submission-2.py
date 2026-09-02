class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # brute force soln is -- using two loops check -- O(n^2) -- worst case

        if (len(s) != len(t)):
            return False
        
        # using hashmaps -- creating a size of 26 chars -- using both an list. 
        # maintaining two states -- two hash for each string -- 
        # weak topic -- hash map and hash table 

        countS = {}
        countT = {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT

