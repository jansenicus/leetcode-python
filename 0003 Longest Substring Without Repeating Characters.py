class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        https://leetcode.com/problems/longest-substring-without-repeating-characters/

        Given a string s, find the length of the longest substring without repeating characters.

        Example 1:

        Input: s = 'abcabcbb'
        Output: 3
        Explanation: The answer is "abc", with the length of 3.

        Example 2:

        Input: s = 'bbbbb'
        Output: 1
        Explanation: The answer is "b", with the length of 1.

        Example 3:

        Input: s = 'pwwkew'
        Output: 3
        Explanation: The answer is "wke", with the length of 3.
        Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


        Constraints:

        0 <= s.length <= 5 * 104
        s consists of English letters, digits, symbols and spaces.

        Success Details:

        Runtime: 55 ms, faster than 98.09% of Python3 online submissions for Longest Substring Without Repeating Characters.
        Memory Usage: 14 MB, less than 49.67% of Python3 online submissions for Longest Substring Without Repeating Characters.

        https://youtu.be/wiGpQwVHdE0
        """
        
        latest_id = {}                          # let `latest_idx` be the mapping of {element: latest index}
        ix = 0                                  # let `ix` be the index of each element
        delta = 0                               # let `delta` be the placeholder for distance
        
        for i, e in enumerate(s):

            if e in latest_id:                  # if element `e` already exists in `latest_id`
                ix = max(latest_id[e], ix)      # update `ix` to keep its maximum possible value

            delta = max(delta, i-ix + 1)        # update `delta` to keep its maximum possible value
            latest_id[e] = i + 1                # update `latest_id` to `i+1`
            
        return delta                            # the final `delta` value is the length of the longest substring
        
        
        
