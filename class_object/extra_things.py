class Goa:
    no_beer = 0
    no_wine = 0
    no_spirit = 0
    no_cocktail = 0
    no_soda = 0
    
    def __str__(self):   # used to print the object  # convert object to string
        return f"{self.no_beer} {self.no_wine} {self.no_spirit} {self.no_cocktail} {self.no_soda}"
    
    def fun():
        print("We are having fun")                    

g = Goa()
print(g)

# del g.no_spirit

print(g)

del g
# print(g)  // give us error after deleting




