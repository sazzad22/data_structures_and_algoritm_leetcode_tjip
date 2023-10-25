# TC = O(N)
# SC = O(1)


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # base case
        if head == None:
            return None
        prev = None
        curr = head
        while curr is not None:
            node_forward = curr.next
            curr.next = prev

            # move forward
            prev = curr
            curr = node_forward
        return prev
        
