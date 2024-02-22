# # # # # # class Person:
# # # # # #     def __init__(self,fn, ln):
# # # # # #         self.first_name = fn
# # # # # #         self.last_name = ln
# # # # # #         self.age = age

# # # # # #     def full_details(self):
# # # # # #         return f"{self.first_name} {self.last_name}"
    

# # # # # # class Student(Person):
# # # # # #     def __init__(self, fn, ln, cls):
# # # # # #         super().__init__(fn, ln)

# # # # # #     def full_details(self):
# # # # # #         pass  # to check if using pass will help override the super class function
# # # # # # # p = Person("shankar", "tamang", 25)
# # # # # # # s = Student("hari","ram", 20, 10 )

# # # # # # # # print(p.full_details())
# # # # # # # print(s.full_details())


# # # # # # def check(n):
# # # # # #     print(p)

# # # # # # p = 5
# # # # # # check(6)


# # # # # # to check if the except block will return any value or not
# # # # # def Check_no(no):

# # # # #     try:
# # # # #         if int(no) > 5:
# # # # #             return "Greater than 5."

# # # # #         else:
# # # # #             return False
# # # # #     except ValueError:
# # # # #         print("Only numbers are accepted.")
# # # # #         return False
        
# # # # # Check_no(10)

# # # # # from Hospital_Management_System_1st_sem_project.person import Person
# # # # # from Hospital_Management_System_1st_sem_project.person import Person



# # # # # to read each line of patient


# # # from Patient import Patient

# # # patient_list = []



# # # # # shankar,tamang,19,98888,0w23,["cough", "cold", "sweat"]
# # # # # to add value in the txt file


# # # with open("check_list.txt",'a') as file:
# # #     first_name = input("Enter first name: ")
# # #     surname = input("Enter surname: ")
# # #     age = input("age: ")
# # #     mobile = input("mobile: ")
# # #     address = input("address: ")
# # #     # symtoms = input("Enter sumptoms separated by comma (eg. cough,vomit) ")
# # #     symptom1 = input("Enter first symptoms: ")
# # #     symptom2 = input("Enter second symptoms: ")
# # #     file.write("\n")
# # #     file.write(f"{first_name},{surname},{age},{mobile},{address},{[symptom1, symptom2]}")



      
# # # # to load patient
    
# # # def load_patient(file_name):
# # #     with open(file_name) as file:

# # #         for x in file:
        
# # #             string_list = x.split(",")
# # #             # patient_list.append(Patient(string_list[0],string_list[1],string_list[2],string_list[3],string_list[4],string_list[5]))
# # #             patient_list.append(Patient(*string_list))
# # #     return patient_list



    
# # name = ['shankar','tamang',"hari"]

# # name_one = name[1]
# # name_two = name[1:]

# # print(name_one)
# # print(name_two)


# from Admin import Admin

# def sort_ilness(patients):
#     symptoms_and_patient = {}

#     for patient in patients:
#         for symptom in patient.get_symptoms():
#             if symptom not in symptoms_and_patient:
#                 symptoms_and_patient[symptom] = 1

#             else:
#                 symptoms_and_patient[symptom] += 1

#     return symptoms_and_patient


# patients = Admin.load_patient_file("patient.txt")

# print(sort_ilness(patients))

print("an" in "shankar")