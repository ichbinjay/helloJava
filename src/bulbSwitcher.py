class Solution:
    def bulbSwitch(self, n: int) -> int:
        arr = [0 for x in range(n)]
        for i in range(1,n+1):
            for j in range(1,n+1):
                if j%i==0:
                    if arr[j-1]==0:
                        arr[j-1]=1
                    else:
                        arr[j-1]=0
        return arr.count(1) # to overcome TLE, return sqrt(n)
