h=float(input("Nhập chiều dài hcn:"))
w=float(input("Nhập chiều rộng hcn:"))
if h>=100 or w<=0:
    print("vui lòng nhập lại")
else:
    C=(h+w)*2
    S=h*w
print("Chu vi hcn:",round(C,2))
print("Diện tích hcn:",round(S,2))