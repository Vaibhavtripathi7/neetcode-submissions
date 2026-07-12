class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        havezero = 0
        zero_index = []
        for i in range(len(nums)): 
            if nums[i] == 0: 
                havezero += 1
                zero_index.append(i)
            else: 
                continue 

        def total_product_fn(nums, havezero): 
            total_product = 1
            total_product_zero = 1

            if havezero == 0: 
                for i in nums:
                    total_product = total_product * i
                return total_product

            elif havezero == 1:
                for i in nums:
                    if i == 0:
                        i += 1  
                    total_product_zero = total_product_zero * i 
                return total_product_zero

        total_product = total_product_fn(nums, havezero)

        if havezero > 1:
            nums = [0] * len(nums) 
            return nums 

        elif havezero == 0: 
            for i in range(len(nums)): 
                nums[i] = int(total_product / nums[i])
        elif havezero == 1:
            for i in range(len(nums)): 
                nums[i] = 0
                nums[zero_index[0]] = total_product
        return nums