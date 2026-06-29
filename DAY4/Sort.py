products=eval(input("enter the dictionary"))
choice=input("key/price")
def get_value(item):
    return item[1]

if choice=="key":
    sorted_dic=dict(sorted(products.items()))
    print("sorted dictionary:",sorted_dic)

elif choice=="price":
    sorted_dic=dict(sorted(products.items(),key=get_value))
    print(sorted_dic)

else:
    print("invaild choice")