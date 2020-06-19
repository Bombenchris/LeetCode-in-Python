from typing import List
import copy


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sortedList = copy.deepcopy(nums)
        sortedList.sort()
        Output = []
        for n in nums:
            count = sortedList.index(n)
            Output.append(count)
        return Output


# Runtime: 76 ms, faster than 69.58% of Python3 online submissions for How Many Numbers Are Smaller Than the Current Number.
# Memory Usage: 13.9 MB, less than 38.08% of Python3 online submissions for How Many Numbers Are Smaller Than the Current Number.

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        dic = {}
        sorted_list = sorted(nums)

        for i, n in enumerate(sorted_list):
            if n not in dic:
                dic[n] = i
        return [dic[n] for n in nums]

# Runtime: 52 ms, faster than 91.62% of Python3 online submissions for How Many Numbers Are Smaller Than the Current Number.
# Memory Usage: 13.8 MB, less than 66.31% of Python3 online submissions for How Many Numbers Are Smaller Than the Current Number.