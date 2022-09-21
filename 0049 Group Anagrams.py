class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]

        https://leetcode.com/problems/group-anagrams/
        """
        from collections import defaultdict
        
        anagrams = defaultdict(list)

        for word in strs:

            count = [0] * 26

            for c in word:
                count[ord(c) - ord("a")] += 1

            anagrams[tuple(count)].append(word)

        return anagrams.values()
