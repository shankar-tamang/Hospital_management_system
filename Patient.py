from person import Person

class Patient(Person):
    """Patient class"""

    def __init__(self, first_name, surname, age, mobile, postcode, doctor, symptoms=[]):
        """
        Args:
            first_name (string): First name
            surname (string): Surname
            age (int): Age
            mobile (string): the mobile number
            address (string): address
        """

        
        super().__init__(first_name, surname)
        self.__age = age
        self.__mobile = mobile
        self.__postcode = postcode
        self.__doctor = doctor
        self.__symptoms = symptoms
        

    
    # def full_name(self) :
    #     """full name is first_name and surname"""
    #     #ToDo2
    #     pass
        
        
    def get_age(self):
        return self.__age
    
    def get_mobile(self):
        return self.__mobile
    
    def get_postcode(self):
        return self.__postcode

    def get_doctor(self):        
        return self.__doctor
    
    def get_family_details(self):
        pass


    
    def link(self, doctor):
        """Link the patient to a doctor"""
        self.__doctor = doctor
        # Update the patient's data file
        self.update_patient_file()

    def update_patient_file(self):
        """Update the patient's data file with the assigned doctor"""
        # Open the patient data file in read mode
        with open("patient.txt", "r") as file:
            lines = file.readlines()

        # Find the line corresponding to the current patient
        for i, line in enumerate(lines):
            # Extract first name and surname from the line
            patient_name = line.split(",")[0] + "," + line.split(",")[1]
            if patient_name == f"{self.get_first_name()},{self.get_surname()}":
            
                print(line)

                line_list = line.split(",")
                line_list[5] = self.__doctor 
                updated_line = ",".join(line_list)
                lines[i] = updated_line
                print(updated_line)
                break

        # Write the updated lines back to the file
        with open("patient.txt", "w") as file:
            file.writelines(lines)



    def get_symptoms(self):
        return self.__symptoms
    
    def print_symptoms(self):
        """prints all the symptoms"""
        #ToDo4
        for symptom in self.__symptoms:
            print(symptom, end=", ")

    def __str__(self):
        return f'{self.get_full_name():^30}|{self.__doctor:^30}|{self.__age:^5}|{self.__mobile:^15}|{self.__postcode:^10}'
    

# pa = Patient("shankar", "tamang", 19, 98888, '0w23', ["cough", "cold", "sweat"])

# print(pa)
# pa.link("Anderson")
# print(pa)
# pa.print_symptoms()
