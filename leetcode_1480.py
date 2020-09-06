# Solution 1. for문을 이용한 풀이
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum_list = []
        num = 0

        for i in range(len(nums)):
            num += nums[i]
            sum_list.append(num)

        return sum_list

# Solution 2. accumulate()함수를 이용한 풀이
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        return accumulate(nums)

# Solution 3. list comprehension 과 sum()함수를 이용한 풀
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        if not nums: return
        return [sum(nums[:num]) for num in range (1, len(nums) +1)]