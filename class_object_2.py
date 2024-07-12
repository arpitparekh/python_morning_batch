class Institute:
    # class holds
    # variables(atributes) and methods(memeber functions)
    
    name = ""
    age = 0
    no_student = 0
    
    def teaching(self,name):                        # self means the class itself
        print(f"Teaching is happening by {name}")
        

i = Institute()

i.name="Bascom"
i.age = 25
i.no_student = 35
i.teaching("Maulik")

i2 = Institute()

i2.name="Tops"
i2.age = 10
i2.no_student = 80
i2.teaching("Arpit")

i3 = Institute()
i3.name = "Red and White"
i3.age = 34
i3.no_student = 60
i3.teaching("Bhaumik")



        

        