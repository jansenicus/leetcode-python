# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        https://leetcode.com/problems/add-two-numbers/

        You are given two non-empty linked lists representing two non-negative integers. 
        The digits are stored in reverse order, and each of their nodes contains a single digit. 
        Add the two numbers and return the sum as a linked list.
        You may assume the two numbers do not contain any leading zero, except the number 0 itself.

        Example 1:

        Input: l1 = [2,4,3], l2 = [5,6,4]
        Output: [7,0,8]
        Explanation: 342 + 465 = 807.

        Example 2:

        Input: l1 = [0], l2 = [0]
        Output: [0]

        Example 3:

        Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
        Output: [8,9,9,9,0,0,0,1]


        Constraints:

        The number of nodes in each linked list is in the range [1, 100].
        0 <= Node.val <= 9
        It is guaranteed that the list represents a number that does not have leading zeros.

        """        
        
        current = head = ListNode(0)                    # initialize `current` = `head` = linked list
        carry = 0                                       # initialize `carry` to 0
        
        while l1 or l2 or carry:                        # while there is value keep looping

            if l1:                                      
                carry = carry + l1.val                  # add `l1.val` to `carry`
                l1 = l1.next                            # move `l1` to the next node
                
            if l2:
                carry = carry + l2.val                  # add `l2.val` to `carry`
                l2 = l2.next                            # move `l2` to the next node
                
            q, r = divmod(carry, 10)                    # `quotient`, `remainder`
            carry = q                                   # `quotient` is the new `carry`

            current.next = ListNode(r)                  # `current.next` is a LL node with value `remainder`
            current = current.next                      # `current.next` is the new `current`

        return head.next                                # `head.next` is the sum
