class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)

        # Previous greater
        left_greater = [-1] * n
        stack = []

        for i in range(n):
            while stack and nums[stack[-1]] <= nums[i]:
                stack.pop()

            if stack:
                left_greater[i] = stack[-1]

            stack.append(i)

        # Next greater
        right_greater = [n] * n
        stack = []

        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] < nums[i]:
                stack.pop()

            if stack:
                right_greater[i] = stack[-1]

            stack.append(i)

        # Previous smaller
        left_smaller = [-1] * n
        stack = []

        for i in range(n):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()

            if stack:
                left_smaller[i] = stack[-1]

            stack.append(i)

        # Next smaller
        right_smaller = [n] * n
        stack = []

        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] > nums[i]:
                stack.pop()

            if stack:
                right_smaller[i] = stack[-1]

            stack.append(i)

        sum_max = 0
        sum_min = 0

        for i in range(n):
            # Contribution as maximum
            count_max = (i - left_greater[i]) * (right_greater[i] - i)
            sum_max += count_max * nums[i]

            # Contribution as minimum
            count_min = (i - left_smaller[i]) * (right_smaller[i] - i)
            sum_min += count_min * nums[i]

        return sum_max - sum_min