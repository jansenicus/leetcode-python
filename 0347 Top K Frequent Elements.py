class Solution(object):
    def topKFrequent(self, nums, k):
        """
        https://leetcode.com/problems/top-k-frequent-elements/

        Given an integer array nums and an integer k, return the k most frequent elements.
        You may return the answer in any order.

        Example 1:
        Input: nums = [1,1,1,2,2,3], k = 2
        Output: [1,2]

        Example 2:
        Input: nums = [1], k = 1
        Output: [1]

        Constraints:
        1 <= nums.length <= 105
        -104 <= nums[i] <= 104
        k is in the range [1, the number of unique elements in the array].
        It is guaranteed that the answer is unique.

        Follow up:
        Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

        Runtime: 86 ms, faster than 92.46% of Python online submissions for Top K Frequent Elements.
        Memory Usage: 17 MB, less than 46.64% of Python online submissions for Top K Frequent Elements.

        https://youtu.be/YPTqKIgVk-k
        """
        from collections import defaultdict
        n_freq = defaultdict(lambda: 0)

        for num in nums:
            n_freq[num] += 1

        return [key for key, val in sorted(n_freq.items(), key=lambda item: item[1], reverse=True)][:k]

