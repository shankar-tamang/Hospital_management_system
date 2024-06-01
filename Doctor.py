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
        self.__doctor_appointments = {}


    # def set_first_name(self,index,first_name,file_name):
    #     with open(file_name) as file:
    #         lines = file.readlines()
    #     for id,line in enumerate(lines):
    #         if id == index:
                
    #             lines[id] = f"{first_name},{self.get_surname()},{self.get_speciality()}\n"  # here \n new line which is in the list is not replaced so no \n is added here
    #     with open(file_name, 'w') as file:
    #         for line in lines:
    #             file.write(line)
        


    # def set_surname(self,index,surname,file_name):
    #     with open(file_name) as file:
    #         lines = file.readlines()
    #     for id,line in enumerate(lines):
    #         if id == index:
    #             lines[id] = f"{self.get_first_name()},{surname},{self.get_speciality()}\n"  # here \n new line which is in the list is not replaced so no \n is added here
    #     with open(file_name, 'w') as file:
    #         for line in lines:
    #             file.write(line)
    
    # def set_surname(self,new_surname):
    #     self.__surname = new_surname

    def get_speciality(self):        
        return self.__speciality

    # def set_speciality(self, index, new_speciality, file_name):        
    #     self.__speciality = new_speciality
    #     with open(file_name) as file:
    #         lines = file.readlines()
    #     for id,line in enumerate(lines):
    #         if index == id:
    #             lines[id] = f"{self.get_first_name()},{self.get_surname()},{new_speciality}\n"  # here \n new line which is in the list is not replaced so no \n is added here
    #     with open(file_name, 'w') as file:
    #         for line in lines:
    #             file.write(line)

    def set_speciality(self,new_speciality):
        self.__speciality = new_speciality

    def add_patient(self, patient):
        self.__patients.append(patient)

    def get_patients(self):      

        return self.__patients

    def show_patient(self):
        print("---------- Patient list -----------")
        print(f"ID |    Patient")
        
        for id, patient in enumerate(self.__patients, start=1):
            print(f"{id:<3}|    {patient:<10}")

    def get_appointments(self):
        return self.__appointments



    def set_appointments(self, appointment, month):
    
        if month not in self.__doctor_appointments:
            self.__doctor_appointments[month] = [appointment]
        else:
            self.__doctor_appointments[month].append(appointment)

        self.__appointments.append(appointment)
        # print(self.get_monthly_appointment())
        print("Appointment has been set.")

    def get_monthly_appointment(self):
       
        return self.__doctor_appointments

    def __str__(self) :
        return f'{self.get_full_name():^30}|{self.__speciality:^15}'

