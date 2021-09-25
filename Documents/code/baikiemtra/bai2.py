A = [1,1,2,3,5,8,13,21,34,55,88]
A.sort();
B = [1,3,4,5,7,88,66,59,40,54]
B.sort();
C=[]
D=[]
E=[]
for i in range(0, len(A)):
    for j in range(0, len(B)):
        if A[i]==B[j]:
            C.append(A[i])
            break;
print('Các số trùng nhau:', C);
k = int();
for i in range(0, len(A)):
    k=0
    for j in range(0, len(C)):
        if A[i]==C[j]:
            k=1;
    if k != 1:
        D.append(A[i]);
for i in range(0, len(B)):
    k=0
    for j in range(0, len(C)):
        if B[i]==C[j]:
            k=1
    if k != 1:
        E.append(B[i]);
print('List A mới ', D)
print('List B mới ', E)