marks = int(input("enter the marks"))
if marks <0 or marks>100:
    print("invalid marks")
elif marks>=90:
    print("grade A")
elif marks >=80:
    print("grade B")
elif marks >=70:
    print("grade c")
elif marks>=60:
    print("grade D")
elif marks>50:
    print("grade E")
else:
    print("fail")