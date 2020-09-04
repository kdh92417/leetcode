# Solution 1.
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        # 링크드리스트의 값들을 빈리스트를 만들어 추가시켜주었다.
        linked = []
        while head is not None:
            linked.append(head.val)
            head = head.next
        linked = linked[::-1]

        # for문을 돌면서 비트연산을 하였다.
        result = 0
        for i in range(len(linked)):
            num = pow(2, i) * linked[i]
            result += num

        return result

# Solution 2. 비트연산자를 이용한 풀이
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        result = 0
        while head:
            result <<= 1
            result |= head.val
            head = head.next
        return result