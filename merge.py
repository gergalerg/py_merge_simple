import random

LEN = 32 
l = [random.randint(1,100) for i in range(1,LEN)]

t = list(range(100, 100 - LEN, -1))

def merge(A, p, q, r):
    n1 = q - p 
    n2 = r - q
    L = A[:n1]
    R = A[n2:]
    i = 0
    j = 0
    for k in range(p, q):
        if L[i] <= R[i]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1

def merge_sort(A, p = 0, r = LEN-1):
    if p < r:
        q = (p + r) // 2
        merge_sort(A, p, q)
        merge_sort(A, q+1, r)
        merge(A, p, q, r)
    else:
        pass

merge_sort(t)
#merge(t, 0, LEN//2 , LEN)
print(t)
