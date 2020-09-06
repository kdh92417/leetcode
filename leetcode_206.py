# Solution 1. prev 변수를 이용한 스왑
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        while head:
            cur = head
            head = head.next
            cur.next = prev
            prev = cur
        return prev

# Solution 2. 재귀 구조를 이용한 풀이
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        def reverse(node: ListNode, prev: ListNode = None):
            if not node:
                return prev
            next, node.next = node.next, prev
            return reverse(next, node)

        return reverse(head)