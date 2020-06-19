from typing import List


class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        Output = []
        for i in range(0, len(nums), 2):
            freq, value = nums[i], nums[i + 1]
            sublist = [value] * freq
            Output.extend(sublist)

        return Output

# Runtime: 64 ms, faster than 89.67% of Python3 online submissions for Decompress Run-Length Encoded List.
# Memory Usage: 14.1 MB, less than 39.29% of Python3 online submissions for Decompress Run-Length Encoded List.