gt=1
while True:
    n=int(input("Nhập 0<n<10:"))
    if n>0 and n<10:
        for i in range(1,n+1):
            gt=gt*i
        break
print(gt)
        
    
    