#Solution
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # l1 과 l2를 비교하여 작은 값이 왼쪽에 오게한다.
        if (not l1) or (l2 and (l1.val > l2.val)):
            l1, l2 = l2, l1
        # next는 그다음 값이 엮이도록 재귀호출
        if l1:
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1