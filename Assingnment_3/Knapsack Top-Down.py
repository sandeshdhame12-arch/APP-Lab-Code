def knapsack_topdown(wt, val, W):
    memo = {}
    def solve(i, w):
        if i == 0 or w == 0:
            return 0
        if (i, w) in memo:
            return memo[(i, w)]
        if wt[i]>W:
            res=solve(i - 1, w)
        else:
            res=max(solve(i-1,w),
                        val[i]+solve(i-1,w-wt[i]))
            memo[(i,w)] = res
        return res
    return solve(len(wt)-1, W)
print (knapsack_topdown([2,3,4,5],[3,4,5,6],5))