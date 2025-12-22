h=float(input("Nhập chiều dài hcn:"))
w=float(input("Nhập chiều rộng hcn:"))
while True:
    h=float(input("Nhập chiều dài hcn:"))
    w=float(input("Nhập chiều rộng hcn:"))
    if w>=0 and h<=100:
        C=(h+w)*2
        S=h*w
        break
print("Chu vi hcn:",round(C,2))
print("Diện tích hcn:",round(S,2))