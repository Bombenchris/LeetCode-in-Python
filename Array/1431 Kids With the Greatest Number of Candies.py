from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        Output = []
        greatestNum = max(candies)
        for candy in candies:
            condition = candy + extraCandies
            if condition >= greatestNum:
                Output.append(True)
            else:
                Output.append(False)
        return Output

#
# Runtime: 32 ms, faster than 92.48% of Python3 online submissions for Kids With the Greatest Number of Candies.
# Memory Usage: 13.7 MB, less than 82.73% of Python3 online submissions for Kids With the Greatest Number of Candies.