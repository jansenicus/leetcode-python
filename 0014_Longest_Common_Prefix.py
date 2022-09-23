class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        https://leetcode.com/problems/longest-common-prefix/

        Write a function to find the longest common prefix string amongst an array of strings.
        If there is no common prefix, return an empty string.

        Example 1:
        Input: strs = ['flower', 'flow', 'flight']
        Output: 'fl'

        Example 2:
        Input: strs = ['dog', 'racecar', 'car']
        Output: ''

        Explanation: There is no common prefix among the input strings.

        Constraints:
        1 <= strs.length <= 200
        0 <= strs[i].length <= 200

        strs[i] consists of only lowercase English letters.

        """

        prefix = strs[0] if len(strs) else ""               # initialize `prefix` equals to the first `strs`
        
        for i, word in enumerate(strs, 1):              	# enumerate `strs` from index 1
            
            previous_len = len(prefix)                      # `previous_len` to be the len of previous prefix

            if previous_len == 0:                           # if `previous_len` = 0
                break                                       # no need to continue

            current_prefix = ""                             # initialize `current_prefix`
                
            for j, e in enumerate(word):                	# for each element `e` in `word`
                
                if j < previous_len and e == prefix[j]:     # if current element `e` equals prefix element
                    current_prefix += e                     # update `current_prefix`
                else:
                    break                                   # otherwise break the loop
                    
            prefix = current_prefix                         # update `prefix` to `current_prefix`
            
        return prefix
