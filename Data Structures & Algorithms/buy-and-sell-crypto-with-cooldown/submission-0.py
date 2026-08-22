class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cache = {}
        def profit(i, state):
            if i == len(prices):
                return 0
            if (i, state) in cache:
                return cache[(i, state)]

            if state == "holding":
                sell = prices[i] + profit(i + 1, "cooldown")
                skip = profit(i + 1, "holding")
                result = max(sell, skip)
            elif state == "free":
                buy = -prices[i] + profit(i + 1, "holding")
                skip = profit(i + 1, "free")
                result = max(buy, skip)
            else:  # cooldown
                result = profit(i + 1, "free")

            cache[(i, state)] = result
            return result

        return profit(0, "free")