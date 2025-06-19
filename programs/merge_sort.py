def merge_sorted(l1,l2):
    m,n=len(l1),len(l2)
    C,i,j,k=[],0,0,0
    while k<m+n:# remember it is not less than or equal to 
        if i==m:
            C.extend(l2[j:])
            k=k+(n-j)
        elif j==n:
            C.extend(l1[i:])
            k=k+(m-i)
        elif l1[i]<l2[j]:
            C.append(l1[i])
            i,k=i+1,k+1
        else:
            C.append(l2[j])
            j,k=j+1,k+1
    return C

l1=[1,2,3,4]
l2=[2,3,4]
merge_sorted(l1,l2)