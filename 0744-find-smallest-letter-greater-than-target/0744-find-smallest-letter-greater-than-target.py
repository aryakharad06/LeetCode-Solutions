class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        ans = letters[0]
        low = 0
        high = len(letters) - 1
        while low <= high:
            mid = (low + high) // 2
            
            if letters[mid] > target:
                ans = letters[mid]
                high = mid - 1
                
            else:
                low = mid + 1
        return ans
        