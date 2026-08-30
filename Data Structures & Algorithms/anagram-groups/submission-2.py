class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # first create the hash map : as we have to look in history for comparison !
        # list_ = []

        # count = 0
        # for i in strs:
        #     dict_ = {}
        #     for k in i:
        #         if (dict_[k]): 
        #             dict_[k] += 1
        
        #         elif: 
        #             dict_[k] = 1
        #     list_.append(dict_)

        # for m in range(len(strs)): 
        #     for k in dict_:
        #         if (dict_[m] == k):
        #          # grp them !  

        res = defaultdict(list)

        for i in strs:
            count = [0] *26  
            for k in i: 
                count[ord(k) - ord("a")] +=1 

            res[tuple(count)].append(i)

        return list(res.values())

