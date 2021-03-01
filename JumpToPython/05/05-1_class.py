class FourCal:
    def __init__(self, first=4, second=2):
        self.first = first
        self.second = second
    
    def __str__(self):
        return "{0}, {1}".format(self.first, self.second)
    
    def setdata(self, first, second): #self is not keyword, idiom=관용어
        self.first = first
        self.second = second
    
    def add(self):
        return self.first + self.second
    
    def mul(self):
        return self.first * self.second
    
    def sub(self):
        return self.first - self.second

    def div(self):
        return self.first / self.second

a = FourCal()
print(type(a)) #__main__FourCal
a.setdata(4,2)
FourCal.setdata(a, 4, 2) #same with a.setdata(4,2)
print("a.first : {0}, a.second : {1}".format(a.first, a.second))
print("a.id : {0}, a.first.id : {1}".format(id(a), id(a.first))) #a.id : 1899469771536, a.first.id : 140732132243328

print(a.add())
print(a.mul())
print(a.sub())
print(a.div())

b = FourCal()
print(b.add())
print(b.mul())
print(b.sub())
print(b.div())

print(b)

#inherit
class MoreFourCal(FourCal):
    def pow(self):
        return self.first ** self.second
    def div(self):
        if (self.second == 0):
            return None
        else: return self.first / self.second

c = MoreFourCal()
c.setdata(5,3)
print(c.pow())
c.setdata(4,0)
print(c.div())

class FamilyName:
    lastname = "kim" #class var looks like static class member var

a = FamilyName()
b = FamilyName()
print("{0}, {1}, {2}".format(FamilyName.lastname, a.lastname, b.lastname))
print("{0}, {1}, {2}".format(id(FamilyName.lastname), id(a.lastname), id(b.lastname)))
a.lastname = "park" # only a.lastname is changed
# if there is a modification class var, compiler alloc another memory to the instance.
# Or, every class var id are same.
print("{0}, {1}, {2}".format(FamilyName.lastname, a.lastname, b.lastname))
print("{0}, {1}, {2}".format(id(FamilyName.lastname), id(a.lastname), id(b.lastname)))