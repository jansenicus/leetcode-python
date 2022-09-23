# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """

        https://leetcode.com/problems/remove-nth-node-from-end-of-list/

        Given the head of a linked list, remove the nth node from the end of the list and return its head.

        Example 1:
        Input: head = [1,2,3,4,5], n = 2
        Output: [1,2,3,5]

        Example 2:
        Input: head = [1], n = 1
        Output: []

        Example 3:
        Input: head = [1,2], n = 1
        Output: [1]


        Constraints:

        The number of nodes in the list is sz.
        1 <= sz <= 30
        0 <= Node.val <= 100
        1 <= n <= sz

        https://www.youtube.com/watch?v=W4GHixVXNao&ab_channel=thecodingworld
        """

        front = rear = head                 # starting from the `head`

        for i in range(n):                  # moving `front` node
            front = front.next              # to the next `front` node

        if front is None:                   # special case when linked list only has 1 or 2 nodes
            return head.next                # `head` node will be replaced with `head.next`

        while front.next:                   # while value of `front.next` is not `None`
            front = front.next              # keep moving `front` to the next `front` node
            rear = rear.next                # keep moving `rear` to the next `rear` node
            
        rear.next = rear.next.next          # bypassing/ removing the nth node

        return head                         # the `head` with the nth node removed
