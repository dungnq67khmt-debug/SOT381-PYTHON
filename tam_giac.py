n=int(input("Nhập chiều cao của tam giác (n):"))
if n<=0:
    print("Vui lòng nhập số nguyên dương.")
else:
    for i in range(1,n+1):
        print(" "*(n-i),end="")
        print("*"*(2*i - 1))