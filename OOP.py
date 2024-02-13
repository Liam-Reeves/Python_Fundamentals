# object -oriented programming

# class Person:
#     def __init__(self):
#         self.name ="Doe"
#         self.age = 50
#         self.email ="doemike@gmail.com"
#         self.location ="Westlands"
#         self.phone = "0123456789"
#
# person = Person()
# person.name = "Liam Reeves"
# print(person.name)
class People:
    def __init__(self,name,age,email,phone):
        self.name = name
        self.age = age
        self.email = email
        self.phone = phone
person1 = People("John",80,"john@gmail.com",1234)
person2 = People("Liam",90,"liam@gmail.com",7970)
person3 = People("Bob",80,"bob@gmail.com",7888)
person4 = People("Kelvin",90,"kelvin@gmail",9789)
print(f"I am {person1.name} , I am {person1.age} years old and you can reach me through {person1.email} or call on {person1.phone}")
print(f"My colleague is {person2.name} , a great web developer, you can reach him on {person2.email} or call on {person2.phone}")




