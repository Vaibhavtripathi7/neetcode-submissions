class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_ = {} # this will store count of the numbers: key number -- values -- count !

        # for i in nums:
        #     if (dict_[i]):
        #         dict_[i] += 1 
        #     else:
        #         dict_[i] = 1
        # for i in dict_.values():
        # hashmap used but sorting -- causes time complexity to be O(nlogn)
        # that's why here bucket sort is used : for bucket sort -- 
        # mostly pattern is when you want sorting to be btter or o(n)
        # and also top k , most freq problems -- having an upper bound like 
        # freq can;t be more than N, like this bucket sort is used.

        # study bucket sort ! 
        count = {}
        
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums: 
            count[num] = 1 + count.get(num,0)

        for num, cnt in count.items():
            freq[cnt].append(num)

        res = []
        for i in range(len(freq) - 1 , 0, -1):
            for num in freq[i]:
                res.append(num)
                if (len(res) == k):
                    return res