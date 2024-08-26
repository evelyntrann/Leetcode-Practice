# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None: 
            return head
        even = head
        odd = head.next 
        odd_list = odd
        
        while odd and odd.next: 
            even.next = odd.next
            even = even.next
            odd.next = even.next
            odd = odd.next

        even.next = odd_list

        return head
        
            
            
            
        