def GT(a,b,c):
    maxx=a
    minx=a
    if maxx<b:
        maxx=b
    if maxx<c:
        maxx=c
    if minx>b:
        minx=b
    if minx>c:
        minx=c
    return maxx,minx
m,n,k=map(int,input("Nhập m,n,k:").split())
m=GT(m,n,k)
print("Giá trị lớn nhất",m)