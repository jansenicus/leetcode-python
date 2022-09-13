class Solution:
    def longestPalindrome(self, S: str) -> str:
        """
        Manacher's Algorithm Implementation in Python
        O(n) algorithm to find longest palindrome substring

        :param S: string to process
        :return: longest palindrome
        
        LC Runtime: 229 ms, faster than 94.98% of Python3 online submissions for Longest Palindromic Substring.
        """

        # Create a copy of array with sentinel chars in between and around
        # Also include space for starting and ending nodes
        T = [0] * (2 * (len(S)) + 3)

        # Fill odd indices with sentinel chars evens with real chars
        sen_char = "@"
        start_sen = "!"
        end_sen = "#"
        for i in range(len(T)):
            if i == 0:
                T[i] = start_sen
            elif i % 2 == 0 and i < len(T) - 1:
                s_index = (i - 1) // 2
                T[i] = S[s_index]
            elif i % 2 == 1 and i < len(T) - 1:
                T[i] = sen_char
            else:
                T[i] = end_sen

        # Also track the expand length around all indices
        P = [0] * len(T)

        # Track center of largest palin yet
        # and its right boundary
        center = right = 0

        # Track largest expansion length
        # and it index
        max_len = index = 0

        # Loop through word array to
        # update expand length around each index
        for i in range(1, len(T) - 1):

            # Check to see if new palin
            # around i lies within a bigger one
            # If so, copy expand length of its mirror
            mirror = 2 * center - i
            if i < right:
                P[i] = min(right - i, P[mirror])

            # Expand around new center
            # Update expand length at i as needed
            while T[i + P[i] + 1] == T[i - (P[i] + 1)]:
                P[i] += 1

            # If we breached previous right boundary
            # Make i the new center of the longest palin
            # and update right boundary
            if i + P[i] > right:
                right = i + P[i]
                center = i

            # Update max_len
            if P[i] > max_len:
                max_len = P[i]
                index = i

        t_arr = T[ index - max_len: index + max_len + 1 ]
        word_arr = [ c for c in t_arr if c != sen_char and c != start_sen and c != end_sen ]
        word = "".join(word_arr)

        return word




