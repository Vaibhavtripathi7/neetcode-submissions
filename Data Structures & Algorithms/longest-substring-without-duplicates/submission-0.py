class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set() # this is our hash , for checking history 

        left = 0
        res = 0 

        # now implementing sliding window algorithm: 
        for right in range(len(s)): 
            
            #  check, if s[right] present in char_set or not!
            while s[right] in char_set: # this will check until every removed not only one
                # if same then , remove it: 
                char_set.remove(s[left]) # remove left most always, then check again after updating left 
                left += 1 
                # now this will remove same elements

            char_set.add(s[right]) # this will increase the window only -- after checked by above block

            #no need for right + 1 , as for loops goes to next iteration itself! 
            # but we update here the size ! -- which is our result 
            if ( right - left + 1 > res): 
                res = right - left + 1
                

        return res






