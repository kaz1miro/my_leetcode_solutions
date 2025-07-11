class Solution:
    def twoSum(self, nums: [int], target: int) -> [int]:
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []