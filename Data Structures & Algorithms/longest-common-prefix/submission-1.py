class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs1 = []
        j = len(strs) - 1 
        i = 0
        while i < j and j > 0: 
            element1 = strs[i]
            element2 = strs[j]
            
            if len(element2) < len(element1):
                k = len(element2)
            else: 
                k = len(element1) 
            for l in range(k):
                if element1[l] == element2[l]:
                    strs1.append(element1[l])            
                elif (l == 0): 
                    return ""
            i = i + 1 
            j = j - 1 

        m = len(strs1)
        prefix = set(strs1)
        len_set = len(prefix)
        diff = m - len_set
        final_prefix = ""
        for i in range(diff):
            final_prefix = final_prefix + strs1[i]
        return final_prefix



        