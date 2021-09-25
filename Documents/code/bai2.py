A=[1,1,2,3,5,8,13,21,34,55,88]
B=[1,3,5,4,7,88,66,59,40,54]
C=list(set (A) & set(B))
print('Các phần tử trùng nhau trong A&B là:\n',C)
M = list(set(A)^set(C))
print("Các phần tử trong A không trùng B là:\n",M)
N = list(set(B)^set(C))
print("Các phần tử trong B không trùng A là:\n",N)