# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None: #check is the linked list is empty
            return head #when the linked list contains only 1 node, still return the node, not return None
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
 Time complexity: O(n)
#The condition while odd and odd.next ensures that the loop continues until all nodes have been processed.
#Since each node is processed once (either as odd or even), the loop runs for n/2 iterations for odd nodes and n/2 iterations for even nodes in the worst case.
#Therefore, the loop has a time complexity of O(n).
#example: 
head = [1, 2, 3, 4, 5]
even = [1, 2, 3, 4, 5]
odd = [2, 3, 4, 5]
#1st iteration 
even.next=[3, 4, 5]
even = [1,3,4,5]
odd.next=[4,5]
odd=[2,4,5]
#2nd iteration
even.next= [5]
even = [1,3,5]
odd.next = null
odd = [2,4] = odd_list
#when odd is none, connect even with odd
even.next = odd_list = [1,3,5,2,4]
return head 

            
            
            
        
