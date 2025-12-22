a,b,c=map(int,input("Nhập a,b,c:").split())
maxx=a
minx=a
if maxx<b :
    maxx=b
if maxx<c:
    maxx=c
print(maxx)
if minx>b:
    minx=b
if minx>c:
    minx=c
print(minx)