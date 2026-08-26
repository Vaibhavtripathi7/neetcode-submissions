class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        target = amount
        cache = {}
        def ways(index, target):

            if target == 0 : return 1
            if index > len(coins) - 1 or target < 0 : return 0
            if (index, target) in cache: return cache[(index,target)]

            # there are two possibilties either include or not included 

            result = ways(index, target - coins[index]) + ways(index + 1, target)
            cache[(index, target)] = result
            return result
        return ways(0,target)