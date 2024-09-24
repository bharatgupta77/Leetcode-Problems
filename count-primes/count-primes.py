class Solution:
    def countPrimes(self, n: int) -> int:
        cnt=0
        l= [True for i in range(n+1)]
        a = 2
        while (a*a) <= n:
            if (l[a] == True):
                for i in range(a * a, n+1, a):
                    l[i] = False
            a += 1
        
        for j in range(2,n):
            if l[j]:
                cnt+=1
        return cnt

        
        