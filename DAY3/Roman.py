inputroman=input("enter the roman value:")

romandict={
    'I':1,
    'V':5,
    'X':10,
    'L':50,
    'C':100,
    'D':500,
    'M':1000,

}
total=0
for i in range(len(inputroman)-1):
    if romandict[inputroman[i]]<romandict[inputroman[i+1]]:
        total=total-romandict[inputroman[i]]
    else:
        total=total+romandict[inputroman[i]]
total=total+romandict[inputroman[i]]
print(total)
romandict