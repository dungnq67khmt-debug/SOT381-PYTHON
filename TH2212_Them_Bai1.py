import math
while True:
    a=float(input("Nhập cạnh a:"))
    b=float(input("Nhập cạnh b:"))
    c=float(input("Nhập cạnh c:"))
    if a+b>c and a+c>b and b+c>a:
        p=a+b+c
        ncv=p/2
        s=math.sqrt(ncv*(ncv-a)*(ncv-b)*(ncv-c))
        break
print(round(p,2))
print(round(s,2))


