'''
Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.

Return the decimal value of the number in the linked list.'''

'''
Input: head = [1,0,1]
Output: 5
Explanation: (101) in base 2 = (5) in base 10'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        binary = ""
        while head:
            binary = binary + str(head.val)
            head = head.next

        return int(binary,2)