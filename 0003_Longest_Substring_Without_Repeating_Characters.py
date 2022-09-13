class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        G = {}                                # let `G` be the mapping of {element: greatest index}
        g = 0                                 # let `g` be the index to increase greatness
        delta = 0                             # let `delta` be the placeholder for distance
        
        for i in range(0, len(s)):            # loop from 0 to the length of string `s`
            
            e = s[i]                          # element `e` is the string `s` at the index `i`
            if e in G:                        # if element `e` already exists in map `G`
                g = max( G[e], g)             # we need to update `g` value to its maximum possible value
                
            delta = max(delta, i-g + 1)       # we need to update `delta` to its maximum possible value
            G[e] = i + 1                      # update the index value of dictionary `G` for element `e`
            
        return delta                          # the final `delta` value is the length of longest subtring
        
        
        
