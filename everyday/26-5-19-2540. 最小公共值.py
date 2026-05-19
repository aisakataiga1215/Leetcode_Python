class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i, n = 0, len(nums1)
        j, m = 0, len(nums2)
        while i < n and j < m:
            if nums1[i] == nums2[j]:
                return nums1[i]
            if nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return -1
