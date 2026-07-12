# Okay : first what is subsequence : it is a subset but not exactly : here relative order remains 
# same; no changes -- and it is not contiguous -- these two prop
# eg : l = [1, 2, 3, 4, 5] , subset = {2, 3 ,1}, substring = [1, 2, 3,] -- contiguous
# subseq : [1, 4, 5 ] -- relative order remains: but not contigous

# given an integer array: return length -- longest "increasing" subsequence 
# increasinf here adds : all element should be greater than previous ones : 
# LONGEST 

# Example study: 

# after normal example: let's generalise it 

# nums = [9, 1, 4, 2, 3, 3, 7] -- let me think ! 

# take 9, ith element -- then ( i + 1) and more with condition check ...   element -- larger than it ; none -- continue till the end of the list. 
# skip 9; skip ith element ; start with (i+1)the element -- take 1 let's -- and larger element then it to continue the sequence -- continue till the end 
# of the list

# stores their lengths -- in a index -- update it if we found greater; and return it in the last

# let's generalise and think more : 

# we take ith element : then actions : take next element ( check condition ): append -- then we take another element ; repeat 
# or we skip the element: then actions : take the next element (i+1) -- condition/append or skip -- then the next element() -- repeat 

# recursive pattern: -- task is repeating -- so we can solve it using recursion : 
# and DP -- as all are sub-problems -- let's try bottom-up approach: 

# path = []
# path.append(i) ; 
# length = 

# for i in nums: 
#     # either we take take or skip it :
#     length = max(dp[i], dp[i+1]); 
#     # where dp: takes eleement ; then next and condition check or skip it 


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)  # every element alone is a subsequence of length 1

        for i in range(len(nums)):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)
