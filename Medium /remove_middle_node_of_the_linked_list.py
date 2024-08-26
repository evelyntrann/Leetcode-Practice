# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #iterate over the entire linked list to get the total number of nodes
        if head is None or head.next is None: 
            return None
        length = 0 #count the number of index
        current = head 
        #p1
        while current: 
            length += 1 
            current = current.next #move to next node to count for exp [1,2,3] to [2,3]
        middle_index = length // 2 #floor length over 2
        #p2
        current=head 
        for i in range (middle_index - 1): #run to the node before the middle node, then connect with the rest of the linked list
            current = current.next 
        current.next = current.next.next #when the loop stop, connect current with current next.next
        return head #return head without the middle node
