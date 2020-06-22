from typing import List
import collections


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        Count = dict(collections.Counter(nums))
        times = len(nums)//3
        Output = []
        for key,value in Count.items():
            if value > times and len(Output)<2:
                Output.append(key)
        return Output


# Runtime: 120 ms, faster than 76.14% of Python3 online submissions for Majority Element II.
# Memory Usage: 14.8 MB, less than 86.53% of Python3 online submissions for Majority Element II.

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        Count = dict(collections.Counter(nums))
        Output = []
        Output = [key for key,value in Count.items() if value > len(nums) // 3 and len(Output)<2]
        return Output
#
# Runtime: 112 ms, faster than 95.95% of Python3 online submissions for Majority Element II.
# Memory Usage: 14.9 MB, less than 75.26% of Python3 online submissions for Majority Element II.