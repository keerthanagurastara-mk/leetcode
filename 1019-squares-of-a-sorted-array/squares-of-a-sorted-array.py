
class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        square = []

        for i in range(len(nums)):
            square.append(nums[i] * nums[i])

        square.sort()
        return square




        