# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        original_head = ListNode(0)
        dummy.next = head
        original_head = dummy
        
        while dummy.next and dummy.next.next:
            first = dummy.next
            second = first.next
            
            first.next = second.next
            second.next = first
            dummy.next = second
            
            dummy = dummy.next.next
        return original_head.next
