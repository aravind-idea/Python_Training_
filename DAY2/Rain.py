amount=int(input("rain on mm"))
if amount<1:
    print("no rain")
elif 1<=amount<5:
    print("light rain")
elif 5<=amount<10:
    print("moderate rain")
else:
    print("heavy rain")
