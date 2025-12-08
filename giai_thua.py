n=int(input("Nhập một số nguyên dương n để tính giai thừa: "))
if n<0:
    print("Vui lòng nhập số nguyên dương")
elif n==0:
    print("Giai thừa của 0 là: 1")
else:
    fac= 1
    for i in range(1, n + 1):
        fac*= i 
    print(f"Giai thừa của {n} là: {fac}")