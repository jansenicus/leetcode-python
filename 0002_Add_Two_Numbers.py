# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        You are given two non-empty linked lists representing two non-negative integers. 
        The digits are stored in reverse order, and each of their nodes contains a single digit. 
        Add the two numbers and return the sum as a linked list.
        You may assume the two numbers do not contain any leading zero, except the number 0 itself.
        """        
        
        current = head = ListNode(0)                    # initialize `current` = `head` = linked list
        carry = 0                                       # initialize `carry` to 0
        
        while (l1 or l2 or carry):                      # while there is value keep looping

            if l1:                                      
                carry  += l1.val                        # add `l1.val` to `carry` 
                l1 = l1.next                            # move `l1` to the next node
                
            if l2:
                carry += l2.val                         # add `l2.val` to `carry` 
                l2 = l2.next                            # move `l2` to the next node
                
            current.next = ListNode(carry % 10)         # set next node to contain `carry % 10`
            current = current.next                      # set `current` to the next node
            carry //= 10                                # set value of `carry`

        return head.next
