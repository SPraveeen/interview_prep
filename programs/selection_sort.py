def sorting_manual(l):
    n=len(l)
    if n <1:
        return l
    for i in range(n):
        mpos=i
        for j in range(i+1,n):
            if l[j]<l[mpos]:
                mpos=j
        l[i],l[mpos]=l[mpos],l[i]
    return l

print(sorting_manual([4,3,2,6,1]))