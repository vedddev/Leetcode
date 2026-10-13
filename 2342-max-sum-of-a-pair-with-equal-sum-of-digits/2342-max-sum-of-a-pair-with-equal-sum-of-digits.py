
class Solution(object):
    def maximumSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mp = {}
        max_value = -1

        for num in nums:
            temp = num
            digit_sum = 0

            while temp > 0:
                digit_sum += temp % 10
                temp //= 10

            if digit_sum in mp:
                pair_sum = mp[digit_sum] + num
                max_value = max(max_value, pair_sum)
                mp[digit_sum] = max(mp[digit_sum], num)
            else:
                mp[digit_sum] = num

        return max_value
