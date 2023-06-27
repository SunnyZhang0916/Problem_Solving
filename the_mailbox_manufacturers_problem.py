# k,m = identical mailbox prototypes, each fitting up to crackers.

# memo[k][start][end]
memo = [[[0 for _ in range(101)] for _ in range(101)] for _ in range(11)]

def solve(k, start, end):
    #邮箱的数量已经用完，没有剩余可放置的邮箱。在这种情况下，返回正无穷大
    if k == 0:
        return float('inf')
    
    #只剩下一个邮箱可放置。在这种情况下，计算并返回将剩余的炸药放置在起始位置和结束位置之间的成本
    if k == 1:
        return (end * (end + 1) // 2) - (start * (start + 1) // 2)
    
    # 当前区间只有一个炸药，即区间长度为 1。
    # 在这种情况下，不需要进行任何操作，返回 0 表示不需要放置炸药。
    if start == end:
        return 0
    
    # 之前没有计算过当前情况下的最小成本。
    # 进入这个条件块中，我们会尝试计算最小成本，并将结果保存在 memo 列表中，
    # 以便以后的调用可以直接使用，避免重复计算。
    if memo[k][start][end] == 0:
        result = float('inf')

        for i in range(start + 1, end + 1):
            result = min(result, i + max(solve(k - 1, start, i - 1), solve(k, i, end)))
        
        memo[k][start][end] = result
    
    return memo[k][start][end]

try:
    # The first line
    N = int(input())
    
    if N < 1 or N > 100:
        raise ValueError("N should be between 1 and 100")
    
    for _ in range(N):
        k, m = map(int, input().split())
        
        if k < 1 or k > 10 or m < 1 or m > 100:
            raise ValueError("out of the range of k or m")
        
        min_crackers = solve(k, 0, m)
        print(min_crackers)

except ValueError as e:
    print("input error", str(e))

