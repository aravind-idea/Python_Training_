name=str(input("enter the string:"))
mid=len(name)//2

firstpart=name[0:mid]
secondpart=name[mid:0]
revfirstpart=firstpart[::-1]
revsecondpart=secondpart[::-1]
result=revfirstpart+revsecondpart
print(result)