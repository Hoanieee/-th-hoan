def tong(x):
    S=0;
    while(x>0):
        S=S+x%10;
        x=int(x/10);
    return S;
x=int(input("Nhập 1 số nguyên dương:"));
print('Tổng các chữ số trong',x,'là:',tong(x));

