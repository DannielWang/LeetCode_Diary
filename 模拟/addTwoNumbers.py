# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode(0)
        resTemp = res
        flag = 0
        nextSum = 0
        while l1 != None and l2 != None:
            if flag == 0:
                p = l1.val + l2.val
                res.val = p % 10
                nextSum = int(p / 10)
                flag += 1
            else:
                p = l1.val + l2.val +nextSum
                resTemp.next = ListNode(p % 10)
                resTemp = resTemp.next
                nextSum = int(p / 10)
            l1 = l1.next
            l2 = l2.next
        while l1:
            p = l1.val + nextSum
            resTemp.next = ListNode(p % 10)
            resTemp = resTemp.next
            nextSum = int(p / 10)
            l1 = l1.next
        while l2:
            p = l2.val + nextSum
            resTemp.next = ListNode(p % 10)
            resTemp = resTemp.next
            nextSum = int(p / 10)
            l2 = l2.next
        if nextSum != 0:
            resTemp.next = ListNode(1)
        return res