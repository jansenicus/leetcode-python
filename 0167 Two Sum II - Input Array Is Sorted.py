class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
        """

        l, r = 0, len(numbers) - 1

        while l < r:

            csum = numbers[l] + numbers[r]

            if csum < target:
                l += 1

            elif csum > target:
                r = r - 1

            else:

                return [l + 1, r + 1]