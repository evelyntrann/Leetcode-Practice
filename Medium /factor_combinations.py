class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        def backtrack(n, ans):
            if ans: 
                res.append(ans + [n]) 
            for i in range(2, int(sqrt(n)) + 1):
                if n % i == 0:
                    if not ans or i >= ans[-1]:
                        backtrack(n // i, ans + [i])


        res = []
        backtrack(n, [])
        return res
        
        