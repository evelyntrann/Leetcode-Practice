# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        values = [] #create a stack
        current = head
# traverse the linked list and store the value in the stack 
        while current: 
            values.append(current.val)
            current = current.next
# the first node from the start is twin node with the first node from the end
# the second node from the start is twin node with the second node from the end
        max_sum = 0
        i = 0 
        j = len(values) - 1 
        #use two pointer techniques to find the sum of twin nodes
        while i < j: 
            max_sum = max(max_sum, values[i] + values[j])
            i += 1
            j -= 1
        return max_sum

    #Space Complexity: O(n) because we push all the nodes into the stack 
    #Time Complexity: O(n) because it traverse through the list then compare it
    