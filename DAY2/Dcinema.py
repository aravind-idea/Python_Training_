price=float(input("enter the price"))
numberoftickets=int(input("enter the no of tickets"))
category=int(input("category"))



amount=price*numberoftickets
discount=0

if numberoftickets>15:
    discount+=20
if category==1:
    discount+=5

if discount>0:
    amount=amount-(amount*discount/100)
    if numberoftickets>15 and category==1:
        print("discount applied")
    elif numberoftickets>15:
        print("maximum discount")
    else:
        print("student")
else:
    print("no discount")
print("total amount:",amount)