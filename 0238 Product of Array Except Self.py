class Solution(object):
    def productExceptSelf(self, nums):
        """
        https://leetcode.com/problems/product-of-array-except-self/

        Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

        The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

        You must write an algorithm that runs in O(n) time and without using the division operation.



        Example 1:

        Input: nums = [1,2,3,4]
        Output: [24,12,8,6]
        Example 2:

        Input: nums = [-1,1,0,-3,3]
        Output: [0,0,9,0,0]


        Constraints:

        2 <= nums.length <= 105
        -30 <= nums[i] <= 30
        The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.


        Follow up: Can you solve the problem in O(1) extra space complexity?
        (The output array does not count as extra space for space complexity analysis.)
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