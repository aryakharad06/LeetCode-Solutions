class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        n = len(nums)
        ans = [-1] * n

        for i in range(2 * n):
            idx = i % n

            while stack and nums[stack[-1]] < nums[idx]:
                index = stack.pop()
                ans[index] = nums[idx]

            if i < n:
                stack.append(idx)

        return ans