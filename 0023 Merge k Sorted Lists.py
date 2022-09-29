# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        https://leetcode.com/problems/merge-k-sorted-lists/
        https://youtu.be/q5a5OiGbT6Q

        You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
        Merge all the linked-lists into one sorted linked-list and return it.

        Example 1:
        Input: lists = [[1,4,5],[1,3,4],[2,6]]
        Output: [1,1,2,3,4,4,5,6]
        Explanation: The linked-lists are:
        [
          1->4->5,
          1->3->4,
          2->6
        ]
        merging them into one sorted list:
        1->1->2->3->4->4->5->6

        Example 2:
        Input: lists = []
        Output: []

        Example 3:
        Input: lists = [[]]
        Output: []

        Constraints:
        k == lists.length
        0 <= k <= 104
        0 <= lists[i].length <= 500
        -104 <= lists[i][j] <= 104
        lists[i] is sorted in ascending order.
        The sum of lists[i].length will not exceed 104.
        """

        import heapq

        prev = dummy = ListNode(None)
        next_nodes, heap = [], []

        for i, node in enumerate(lists):
            next_nodes.append(node)
            if node:
                heap.append((node.val, i))
        heapq.heapify(heap)

        while heap:
            value, i = heapq.heappop(heap)
            node = next_nodes[i]
            prev.next = node
            prev = prev.next
            if node.next:
                next_nodes[i] = node.next
                heapq.heappush((heap, (node.next.val, i)))

        return dummy.next
