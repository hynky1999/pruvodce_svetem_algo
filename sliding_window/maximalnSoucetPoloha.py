def maxSoucetPoloha(l):
    maximalSoucet = 0
    aktualniSoucet = 0
    rozsah = [0,0]
    for x in range(len(l)):
        if aktualniSoucet+l[x] > 0:
            aktualniSoucet = aktualniSoucet+l[x]
        else:
            aktualniSoucet = 0
            rozsah[0] = x
        if maximalSoucet < aktualniSoucet:
            maximalSoucet = aktualniSoucet
            rozsah[1] = x 
    return [maximalSoucet,*rozsah]
l = [1,4,2,-3,5]
print(maxSoucetPoloha(l))