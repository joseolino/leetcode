from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        return "ListNode(val=" + str(self.val) + ", next={" + str(self.next) + "})"

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        base = None
        index = None
        overflow = 0
        while(l1 and l2):
            sum = l1.val + l2.val
            if(overflow == 1):
                sum += 1
            if(sum > 9):
                overflow = 1
                sum = sum % 10
            else:
                overflow = 0
            newNode = ListNode(sum)
            if(base is None):
                index = newNode
                base = index
            else:
                index.next = newNode
                index = index.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            if(overflow == 1):
                sum = l1.val + overflow
                if(sum > 9):
                    sum = sum % 10
                else:
                    overflow = 0
                index.next = ListNode(sum)
                index = index.next
                l1 = l1.next
            else:
                index.next = l1
                break
        while l2:
            if(overflow == 1):
                sum = l2.val + overflow
                if(sum > 9):
                    sum = sum % 10
                else:
                    overflow = 0
                index.next = ListNode(sum)
                index = index.next
                l2 = l2.next
            else:
                index.next = l2
                break
        if(overflow):
            index.next = ListNode(1)
        return base


def list_to_LL(arr) -> Optional[ListNode]:
    if len(arr) < 1:
        return None
    if len(arr) == 1:
        return ListNode(arr[0])
    return ListNode(arr[0], next=list_to_LL(arr[1:]))

s = Solution()

list1 = list_to_LL([1, 8])

list2 = list_to_LL([0])

r = s.addTwoNumbers(list1, list2)

print(r)


