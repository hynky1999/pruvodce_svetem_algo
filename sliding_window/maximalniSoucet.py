def maxSoucet(l):
    maximalSoucet = 0
    aktualniSoucet = 0
    for x in l:
        aktualniSoucet = max(0,aktualniSoucet +x)
        maximalSoucet = max(aktualniSoucet,maximalSoucet)
    return maximalSoucet
l = [1,2,-3,5]
print(maxSoucet(l))