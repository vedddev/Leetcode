class Solution(object):
    def mostFrequent(self, nums, key):
        mp = {}

        for i in range(len(nums) - 1):
            if nums[i] == key:
                target = nums[i + 1]
                mp[target] = mp.get(target, 0) + 1

        return max(mp, key=mp.get)