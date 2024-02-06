from person import Person

class Patient(Person):
    """Patient class"""

    def __init__(self, first_name, surname, age, mobile, postcode, symptoms=[]):
        """
        Args:
            first_name (string): First name
            surname (string): Surname
            age (int): Age
            mobile (string): the mobile number
            address (string): address
        """

        #ToDo1
        super().__init__(first_name, surname)
        self.__age = age
        self.__mobile = mobile
        self.__postcode = postcode
        self.__doctor = 'None'
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

    def get_doctor(self) :
        #ToDo3
        return self.__doctor
    
    def get_family_details(self):
        pass

    def link(self, doctor):
        """Args: doctor(string): the doctor full name"""
        self.__doctor = doctor
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
