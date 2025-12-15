n=int(input("Nhập n:"))
if n%2==0:
    if n%3==0:
        print("n là số chẵn và chia hết cho 3")
    else:
        print("n là số chẵn nhưng không chia hết cho 3")
elif n%3==0:
    print("n chia hết cho 3 nhưng không phải là số chẵn")
else:
    print("n không phải là số chẵn và không chia hết cho 3")