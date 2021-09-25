list=[1,1,2,6,8,9,4,5,6,45,34,66,44,37,78]
list.sort()
number=[]
for x in list:
    if (x <30):
        number.append(x)
    else:
        break
print('list \n',number)

print("Nhập số bất kì:")
a = int(input())
for x in list:
    if (x > a):
        print(' ',x)