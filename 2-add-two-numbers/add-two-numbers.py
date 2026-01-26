# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        x,y, carry,s = 0,0,0,0
        temp1= l1
        temp2 = l2
        temp = ListNode(0)
        curr = temp
        while temp1 != None or temp2 != None or carry!=0:
            if temp1 == None:
                x = 0
            else:
                x = temp1.val
            if temp2 == None:
                y = 0
            else:
                y = temp2.val
            s = x + y + carry

            carry = s//10

            curr.next = ListNode(s%10)
            curr = curr.next
            if temp1 !=None:
                temp1 = temp1.next
            if temp2 !=None:
                temp2 = temp2.next
        
        return temp.next
