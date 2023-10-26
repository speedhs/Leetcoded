class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        i =1
        op = '0'
        def solve(n,k):
            if n== 1 and k == 1:
                return 0
            mid =2**(n-2)
            if k<=mid:
                return solve(n-1,k)
            else:
                return  int( not solve(n-1,k-mid)) 
            
        return solve(n,k)
