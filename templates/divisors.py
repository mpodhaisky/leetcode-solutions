def divisors(n):
    res = [1]
    i = 1
    while i <n:
        i = n//(n//(i+1))
        if n%i ==0:
            res.append(i)
    return res
