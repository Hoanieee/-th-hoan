def Tong(x):
    S=0;
    while(x>0):
        S=S+x%10;
        x=int(x/10);
    return S;
x=int(input("Nhap 1 so ng.duong:"));
print('Tổng các chữ số trong',x,'là:',Tong(x));