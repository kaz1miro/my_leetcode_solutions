class Solution:
    def intersect(self, nums1, nums2):
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        counts = {}
        for num in nums1:
            counts[num] = counts.get(num, 0) + 1

        intersection = []
        for num in nums2:
            if counts.get(num, 0) > 0:
                intersection.append(num)
                counts[num] -= 1

        return intersection