'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.'''

class ListNode(object):
    def __init__(self,value):
        self.value = value
        self.next = None

class Solution:
    def addTwo(self,l1,l2):

        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        
        add_num = l1.value + l2.value

        if add_num < 10:
            answer_node = ListNode(add_num)
            answer_node.next = self.addTwo(l1.next, l2.next)
            return answer_node
        else:
            carry = l1.value + l2.value -10
            answer_node = ListNode(carry)
            answer_node.next = self.addTwo(ListNode(l1), self.addTwo(l1.next,l2.next))
            return answer_node
        
