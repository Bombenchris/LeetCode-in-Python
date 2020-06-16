from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runningSum = nums
        for i in range(1, len(nums)):
            runningSum[i] = runningSum[i] + runningSum[i - 1]
        return runningSum

# Runtime: 32 ms, faster than 99.26% of Python3 online submissions for Running Sum of 1d Array.
# Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Running Sum of 1d Array.