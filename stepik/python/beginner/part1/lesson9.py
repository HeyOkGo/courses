a = int(input())
b = int(input())
if b !=0:
    print(a / b)
else:
    print("Operation can't be performed")
    b = int(input('Print not null value'))
    if b == 0:
        print ("I said - not null!!!")
    else:
        print(a / b)