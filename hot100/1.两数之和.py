class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for index, number in enumerate(nums):
            if target - number in hash:
                return [hash[target - number], index]
            hash[number] = index
