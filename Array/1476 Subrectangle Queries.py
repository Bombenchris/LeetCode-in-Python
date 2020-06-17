from typing import List
import copy


class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.rectangle = copy.deepcopy(rectangle)

    # it's better and safer to deepcopy the rectangle in __init__ to prevent self.rectangle
    # and rectangle from sharing the same memory. otherwise, changing rectangle,
    # would change self.rectangle (object's rectangle) as they share same memory.
    # Also passing the same rectangle to separate objects (in __init__) would mean
    # they all share the same memory which is not what we would want."

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        for row in range(row1, row2 + 1):
            for col in range(col1, col2 + 1):
                self.rectangle[row][col] = newValue

    def getValue(self, row: int, col: int) -> int:
        return self.rectangle[row][col]

# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries(rectangle)
# obj.updateSubrectangle(row1,col1,row2,col2,newValue)
# param_2 = obj.getValue(row,col)

# Runtime: 208 ms, faster than 90.27% of Python3 online submissions for Subrectangle Queries.
# Memory Usage: 15.6 MB, less than 60.00% of Python3 online submissions for Subrectangle Queries.
