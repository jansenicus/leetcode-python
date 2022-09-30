class Solution:
    def isValid(self, s: str) -> bool:
        """
        https://leetcode.com/problems/valid-parentheses/
        https://youtu.be/WTzjTskDFMg

        Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
        determine if the input string is valid.

        An input string is valid if:

        Open brackets must be closed by the same type of brackets.
        Open brackets must be closed in the correct order.
        Every close bracket has a corresponding open bracket of the same type.

        """

        if len(s) % 2:                              # if the length is odd
            return False                            # the string `s`` must be invalid

        pair = {                                    # pair = {open: close}
            '(': ')',                               # opening and closing pairs of parentheses
            '{': '}',
            '[': ']'
        }

        stack = []                                  # stack to store every opening elements in `s`

        for _ in s:                                 # loop for every element in `s`

            if _ in pair.keys():                    # if current element is an opening element
                stack.append(_)                     # put current opening element into the stack

            else:                                   # otherwise current element is a closing element

                if not stack:                       # check if stack is empty
                    return False                    # which means no opening element available

                last_opening = stack.pop()          # retrieve last opening element in the stack and remove it

                if pair[last_opening] != _:         # the pair for last opening element in the stack should
                    return False                    # equal the current closing element, otherwise return False

        return stack == []                          # opening elements stack must be empty due to pop removal
