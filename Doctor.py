from person import Person

class Doctor(Person):
    """A class that deals with the Doctor operations"""

    def __init__(self, first_name, surname, speciality):
        """
        Args:
            first_name (string): First name
            surname (string): Surname
            speciality (string): Doctor`s speciality
        """
        
        super().__init__(first_name, surname)
        
        self.__speciality = speciality
        self.__patients = []
        self.__appointments = []

    
    # def full_name(self) :
    #     #ToDo1
    #     pass

    # def get_first_name(self) :
    #     #ToDo2
    #     pass

    # def set_first_name(self, new_first_name):
    #     #ToDo3
    #     pass

    # def get_surname(self) :
    #     #ToDo4
    #     pass

    # def set_surname(self, new_surname):
    #     #ToDo5
    #     pass

    def get_speciality(self) :
        #ToDo6
        return self.__speciality

    def set_speciality(self, new_speciality):
        #ToDo7
        self.__speciality = new_speciality

    def add_patient(self, patient):
        self.__patients.append(patient)

    def show_patient(self):
        print("---------- Patient list -----------")
        print(f"ID |    Patient")
        
        for id, patient in enumerate(self.__patients, start=1):
            print(f"{id:<3}|    {patient:<10}")


    def __str__(self) :
        return f'{self.get_full_name():^30}|{self.__speciality:^15}'


# d = Doctor("Shankr", "Tamang", "cardio")

# # # print(d)
# # # print(d.get_speciality())
# # # d.set_speciality("neuro")
# # # print(d.get_speciality())
    
# d.add_patient("hari")
# d.show_patient()