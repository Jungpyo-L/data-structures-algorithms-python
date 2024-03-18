def find_sum(n):
    if n==1:
        return 1
    return n + find_sum(n-1)

def fib(n):
    # 0,1,1,2,3,5,8 <-- fibonacci numbers
    # --------------
    # 0,1,2,3,4,5,6 <-- index
    if n==0 or n==1:
        return n
    return fib(n-1) + fib(n-2)

# if we use dynamic programming (memoize)
def fib_2(n, memo):
    if memo[n] is not None:
        return memo[n]
    if n==0 or n==1:
        return n
    result = fib_2(n-1, memo) + fib_2(n-2, memo)
    memo[n] = result
    return result

def fib_memo(n):
    memo = [None] * (n+1)
    return fib_2(n,memo)

def fib_bottom_up(n):
    if n == 0 or n == 1:
        return n
    bottom_up = [None] * (n+1)
    bottom_up[0] = 0
    bottom_up[1] = 1
    for i in range(2, n+1):
        bottom_up[i] = bottom_up[i-1] + bottom_up[i-2]
    return bottom_up[n]

if __name__=='__main__':
    print(find_sum(5))
    print(fib(10))
    print(fib_memo(10))
    print(fib_bottom_up(10))