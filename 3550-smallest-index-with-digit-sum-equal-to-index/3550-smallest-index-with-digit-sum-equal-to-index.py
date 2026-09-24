class Solution(object):
    def smallestIndex(self, nums):

        for i in range(len(nums)):
            num = nums[i]
            digit_sum = 0

            while num > 0:
                digit = num % 10
                digit_sum += digit
                num //= 10

            if digit_sum == i:
                return i

        return -1