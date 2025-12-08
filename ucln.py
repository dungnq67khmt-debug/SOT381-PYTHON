a_nhap = input("Nhập số thứ nhất (a): ")
b_nhap = input("Nhập số thứ hai (b): ")
a = abs(int(a_nhap))
b = abs(int(b_nhap))
maxx=a
minx=b
if a==0 and b==0:
    ucln=0
elif a==0:
    ucln=b
elif b==0:
    ucln=a
else:
    while minx!=0:
        so_du=maxx%minx
        maxx=minx
        minx=so_du
    ucln=maxx
print(f"ƯCLN của {a} và {b} là: {ucln}")