#Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode(0)
        temp = 0
        temp_list = result
        while l1 or l2 or temp:
            val1 = (l1.val if l1 else 0)
            val2 = (l2.val if l2 else 0)
            temp, remainder = divmod(val1 + val2 + temp, 10)
            temp_list.next = ListNode(remainder)
            temp_list = temp_list.next
            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)

        return result.next
