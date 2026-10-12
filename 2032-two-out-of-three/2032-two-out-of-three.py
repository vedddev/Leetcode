class Solution(object):
    def twoOutOfThree(self, nums1, nums2, nums3):
        result=[]
        for i in nums1:
            if i in nums2 or i in nums3:
                result.append(i)
        for i  in nums2:
            if i in nums1 or i in nums3:
                result.append(i)
        for i  in nums3:
            if i in nums1 or i in nums2:
                result.append(i)
        return list(set(result))
        