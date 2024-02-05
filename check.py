# class Person:
#     def __init__(self,fn, ln):
#         self.first_name = fn
#         self.last_name = ln
#         self.age = age

#     def full_details(self):
#         return f"{self.first_name} {self.last_name}"
    

# class Student(Person):
#     def __init__(self, fn, ln, cls):
#         super().__init__(fn, ln)

#     def full_details(self):
#         pass  # to check if using pass will help override the super class function
# # p = Person("shankar", "tamang", 25)
# # s = Student("hari","ram", 20, 10 )

# # # print(p.full_details())
# # print(s.full_details())


# def check(n):
#     print(p)

# p = 5
# check(6)


# to check if the except block will return any value or not
def Check_no(no):

    try:
        if int(no) > 5:
            return "Greater than 5."

        else:
            return False
    except ValueError:
        print("Only numbers are accepted.")
        return False
        
Check_no(10)