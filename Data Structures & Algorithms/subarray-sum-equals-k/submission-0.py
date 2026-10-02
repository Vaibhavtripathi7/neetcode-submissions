class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # creating the hashmap : 
        map = { 0 : 1 } # with first element
        count = 0
        prefix = 0 
        # now i have to iterate through nums: 
        for i in range(len(nums)):
            # for each : index we do operations: 
            prefix = prefix + nums[i]

            if prefix - k in map: 
                count += map[prefix - k]

            map[prefix] = map.get(prefix, 0) + 1 

        return count