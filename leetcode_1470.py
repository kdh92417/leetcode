'''
LeetCode : 1470. Shuffle the Array
'''

# Solution 1. 리스트 슬라이싱을 이용한 풀
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        x1 = nums[:n]
        y1 = nums[n:]
        result = collections.deque()
        i = 0
        while i < n:
            result.append(x1[i])
            result.append(y1[i])
            i += 1

        return result

# Solution 2. 간단하게 풀기
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []
        for i in range(n):
            result.append(nums[i])
            result.append(nums[i + n])  # n만큼의 인덱스를 주어서 빈리스트에 추가한다.
        return  result

# Solution 3. chain 함수와 zip함수를 이용한 풀이
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]
        # chain함수와 zip함수이용하여 두개의 리스트를 연결하여 리스트로 만들어 리턴
        return list(chain.from_iterable(zip(nums[:n], nums[n:])))