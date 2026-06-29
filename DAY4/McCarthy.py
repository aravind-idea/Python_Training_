def mcCarthy(n):
    if n>100:
        return n-10
    
    return mcCarthy(mcCarthy(n+11))
n=int(input("enter a number"))
print("number",mcCarthy(n))