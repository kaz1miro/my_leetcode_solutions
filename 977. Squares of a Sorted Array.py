class Solution:
    def sortedSquares(self, nums: [int]) -> [int]:
        negativ = []
        positive = []
        for i in range(len(nums)):
            if nums[i] >= 0:
                positive.append(nums[i])
            else:
                negativ.append(nums[i])
        for num in negativ:
            i = 0
            while (num * -1) < positive[i] and i < len(positive)-1 and len(positive) > 0:
                i+=1
            positive.insert(i,num * -1)
        for i in range(len(nums)):
            positive[i] *= positive[i]

        return positive