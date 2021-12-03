class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        #(f[n-1]+k)%n
        #or (f[i]+k)%(i+1)
        ans =0
        for i in range(0, n):
            ans = (ans+k)%(i+1)
        return ans+1