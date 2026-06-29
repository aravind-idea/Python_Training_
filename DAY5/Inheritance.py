class Grandfather:
    def Skill(self):
        print("Reading current Afffairs")
class Father(Grandfather):
    def Fatherskill(self):
        print("makes money")
class Son(Father):
    def Sonskill(self):
        print("watching reels")
son=Son()
son.Sonskill()
son.Fatherskill()
son.Skill()