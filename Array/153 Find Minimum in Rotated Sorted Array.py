class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_index = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                min_index = i + 1
        return nums[min_index]
#
# Runtime: 36 ms, faster than 90.03% of Python3 online submissions for Find Minimum in Rotated Sorted Array.
# Memory Usage: 14 MB, less than 53.36% of Python3 online submissions for Find Minimum in Rotated Sorted Array.

#   binary - search solution
    def findMin(self, num):
        first, last = 0, len(num) - 1
        while first < last:
            midpoint = (first + last) // 2
            if num[midpoint] > num[last]:
                first = midpoint + 1
            else:
                last = midpoint
        return num[first]