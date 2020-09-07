# Solution 1. Stack을 이용한 풀이
class Solution:
    def isValid(self, s: str) -> bool:
        table = {
            '}': '{',
            ']': '[',
            ')': '('
        }
        stack = []

        # 스택 이용 예외 처리 및 일치 여부 판별
        for char in s:
            if char not in table:
                stack.append(char)
            elif not stack or table[char] != stack.pop():
                return False
        return len(stack) == 0

