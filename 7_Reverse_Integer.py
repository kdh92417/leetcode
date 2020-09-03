# Solution 1.
class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return x

        reverse_nums = str(x)[::-1]
        i = 0
        while True:
            if reverse_nums[i] != '0':
                break
            i += 1

        reverse_nums = list(reverse_nums[i:])
        if reverse_nums[-1] == '-':
            reverse_nums.remove('-')
            reverse_nums.insert(0, '-')
        reverse_nums = int(''.join(reverse_nums))

        max_size = pow(2, 31)
        if -max_size < reverse_nums < max_size - 1:
            result = reverse_nums
        else:
            result = 0

        return result

# Solution 2. 인덱스 0번째의 숫자를 i로 나누면 거꾸로 되는 원리를 이용해서
class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0

        is_nagative = False

        if x < 0:
            is_nagative = True

        x = str(abs(x))
        i = 1
        result = 0

        for num in x:
            result += i * (int(num))
            i *= 10

        if is_nagative == True:
            result *= -1

        max_num = pow(2, 31)
        if -max_num < result < max_num:
            return result
        else:
            return 0