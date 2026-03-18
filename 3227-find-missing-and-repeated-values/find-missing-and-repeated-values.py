class Solution:
    def findMissingAndRepeatedValues(self, grid):
        n = len(grid)
        seen = set()
        duplicate = -1
        
        # Step 1: Find duplicate
        for row in grid:
            for num in row:
                if num in seen:
                    duplicate = num
                seen.add(num)
        
        # Step 2: Find missing
        total_numbers = n * n
        for i in range(1, total_numbers + 1):
            if i not in seen:
                missing = i
                break
        
        return [duplicate, missing]