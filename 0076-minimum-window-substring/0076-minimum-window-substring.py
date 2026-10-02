class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        m = len(t)
        l = 0
        r = 0
        hash = {}
        count = 0
        s_index = -1
        min_len = float("inf")
        for i in range(m):
            hash[t[i]] = hash.get(t[i], 0) + 1 
        while r < n:
            if hash.get(s[r], 0) > 0:
                count += 1
            hash[s[r]] = hash.get(s[r], 0) - 1
            while count == m: 
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    s_index = l
                
                hash[s[l]] = hash.get(s[l], 0) + 1
                if hash[s[l]] > 0:
                    count -= 1
                l += 1
            r += 1
        
        if s_index == -1:
            return ""
        return s[s_index:s_index + min_len]
        










        