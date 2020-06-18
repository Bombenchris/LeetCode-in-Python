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
