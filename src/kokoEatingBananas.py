class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def function(k, piles, h):
            time = 0
            for i in piles:
                time += (i + k - 1) // k  # Calculate the total hours required
            return time <= h

        ll, ul = 1, max(piles)  # Adjust the lower bound to 1
        while ll < ul:
            mid = ll + (ul - ll) // 2
            cond = function(mid, piles, h)
            if cond:
                ul = mid
            else:
                ll = mid + 1
        return ll
