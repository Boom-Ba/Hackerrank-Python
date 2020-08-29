# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        curr = head
        #if fit the reverse condition
        for _ in range(k):
            if not curr:
                return head
            curr=curr.next
        #reverse  
        prev, curr = None, head
        for _ in range(k):
            nextN = curr.next
            curr.next=prev
            prev, curr= curr, nextN
        head.next = self.reverseKGroup(curr,k)
        return prev
        
        