class Solution:
    def missingNumber(self, nums: [int]) -> int:
        ln = len(nums)
        test_set = set()
        for i in range(len(nums)+1):
            test_set.add(i)
        for num in nums:
            if num in test_set:
                test_set.remove(num)
        return test_set.pop()
