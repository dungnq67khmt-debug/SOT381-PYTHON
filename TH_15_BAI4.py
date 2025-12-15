n=int(input("Nhập n:"))
tong1=0
for i in range(1,n+1):
    tong1+=1/i
print(tong1)
tong2=10
for i in range(1,n+1):
    tong2+=(i-1)/i
print(tong2)