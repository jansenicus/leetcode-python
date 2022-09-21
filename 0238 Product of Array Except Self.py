class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]

        https://leetcode.com/problems/product-of-array-except-self/
        """
        n = len(nums)                           #
        prod = [1] * n                          # initialize the `product` with identity 1
        prefix, postfix = 1, 1                  # initialize `prefix` and `postfix` to 1

        for i in range(n):                      # traverse forward from first element
            prod[i] = prefix                    # initialize the product with prefix
            prefix *= nums[i]                   # update `prefix`, multiplied with `nums[i]`

        for i in range(n - 1, -1, -1):          # traverse backward from last element
            prod[i] *= postfix                  # update `prod` multiplied by `postfix`
            postfix *= nums[i]                  # update `postfix` multiplied with `nums[i]`

        return prod
