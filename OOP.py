class Apple:
    color = ""
    flavor = ""
    num = 0
    def count(self):
        self.num+=1

janogold = Apple()
janogold.color = "Red"
janogold.flavor = "sweet"

golden = Apple()
golden.color = "White"
golden.flavor = "Sweet"

print(Apple.count)

class Flower:
    def __init__(self , color , flavor):
        self.color = color
        self.flavor = flavor
    def __str__(self):
        return "Color is {} and Flavor is {}".format(self.color,self.flavor)

rose = Flower("red" , "bad")
print(rose.color)
print(rose)

