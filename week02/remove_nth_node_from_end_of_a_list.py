# Definition for singly-linked list.
# TC: O(N)
# SC: O(1)
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy_head = ListNode(val = 0 , next = head)
        s = dummy_head
        f = dummy_head
        for _ in range(n):
            f = f.next
        while f.next is not None:
            s = s.next
            f = f.next
        s.next = s.next.next
        return dummy_head.next
        