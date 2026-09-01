# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = 0
        cur = head
        while cur:
            size+=1
            cur = cur.next
        idx = size-n
        if idx == 0:
            return head.next
        check = 0
        cur = head
        prev = None
        while cur:
            if check == idx:
                prev.next = cur.next
                break
            check+=1
            prev = cur
            cur = cur.next
        return head
