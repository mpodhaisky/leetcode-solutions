def kthFactor(n: int, k: int) -> int:
    cnt = i =1
    while cnt < k and i <n:
        i = n//(n//(i+1))
        cnt+= n%i == 0
    return -1 if cnt!=k else i
