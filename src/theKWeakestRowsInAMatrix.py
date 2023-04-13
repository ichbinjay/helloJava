class Solution(object):
    def kWeakestRows(self, M, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        y, x = len(M), len(M[0])
        vis, ans = [0] * y, []
        for j in range(x+1):
            for i in range(y):
                if not vis[i] and (j == x or not M[i][j]):
                    ans.append(i)
                    vis[i] = 1
                if len(ans) == k: 
                    return ans