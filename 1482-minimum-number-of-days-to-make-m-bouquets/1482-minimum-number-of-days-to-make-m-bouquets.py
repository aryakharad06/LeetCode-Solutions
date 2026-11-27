class Solution:
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        

        low = min(bloomDay)
        high = max(bloomDay)
        ans = -1

        while low <= high:
            mid = (low + high) // 2

            count = 0
            bouquets = 0

            for bloom in bloomDay:
                if bloom <= mid:
                    count += 1

                    if count == k:
                        bouquets += 1
                        count = 0
                else:
                    count = 0

            if bouquets >= m:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans


        