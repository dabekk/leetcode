# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        current = head
        # get erase position
        length = 0
        while(isinstance(current, precompiled.listnode.ListNode)):
            print(current.val)
            current = current.next
            length += 1
        erase_pos = length - n
        print("erase pos: ", erase_pos)
        current = head      # restart at head
        
        # if start
        if (erase_pos == 0):
            print("deleting start...")
            head = current.next
        # if middle    
        elif (erase_pos > 0 and erase_pos < length):
            print("deleting middle...")
            for j in range (0, erase_pos - 1):  # we're looking for the index before erase_pos
                print(j)
                current = current.next
            current.next = current.next.next

        return head
