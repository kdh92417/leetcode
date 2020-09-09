# Solution 1. for문을 이용한 풀이
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_nums = max(candies)
        result = []
        for i in range(len(candies)):
            if max_nums - (candies[i] + extraCandies) <= 0:
                result.append(True)
            else:
                result.append(False)
        return result

# Solution 2. list Comprehension으로 short coding
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_num = max(candies)

        return [(candy + extraCandies) >= max_num for candy in candies]