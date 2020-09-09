'''
LeetCode 1. Two Sum (Easy)
Blog : https://velog.io/@wind1992
'''
# Solution 1. Brute Force
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


# Solution 2. in과 enumerate()함수를 이용한 탐
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for inde, num in enumerate(nums):
            complement = target - num

            if complement in nums[inde + 1:]:
                return nums.index(num), nums[inde + 1:].index(complement) + (inde + 1)

# Solution 3. dictionary를 이용한 풀
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}

        for i, num in enumerate(nums):
            if target - num in nums_map:
                return [nums_map[target - num], i]
            nums_map[num] = i