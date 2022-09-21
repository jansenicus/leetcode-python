class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]

        https://leetcode.com/problems/top-k-frequent-elements/submissions/

        Runtime: 86 ms, faster than 92.46% of Python online submissions for Top K Frequent Elements.
        Memory Usage: 17 MB, less than 46.64% of Python online submissions for Top K Frequent Elements.

        """

        nfreq = defaultdict(lambda: 0)

        for num in nums:
            nfreq[num] += 1

        return [key for key, val in sorted(nfreq.items(), key=lambda item: item[1], reverse=True)][:k]

