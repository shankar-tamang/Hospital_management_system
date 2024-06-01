import datetime
from Doctor import Doctor
from Patient import Patient
import matplotlib.pyplot as plt


class Admin:
    """A class that deals with the Admin operations"""
    def __init__(self, username, password, address = ''):
        """
        Args:
            username (string): Username
            password (string): Password
            address (string, optional): Address Defaults to ''
        """

        self.__username = username
        self.__password = password
        self.__address =  address

    def view(self,a_list):
        """
        print a list
        Args:
            a_list (list): a list of printables
        """
        for index, item in enumerate(a_list):
            
            print(f'{index+1:3}|{item}')

    def get_username(self):
        return self.__username
    
    def get_password(self):
        return self.__password
    
    def get_address(self):
        return self.__address
    

    def login(self) :
        """
        A method that deals with the login
        Raises:
            Exception: returned when the username and the password ...
                    ... don`t match the data registered
        Returns:
            string: the username
        """
    
        print("-----Login-----")
        #Get the details of the admin
        username = input('Enter the username: ')
        password = input('Enter the password: ')
        return self.__username == username and password == self.__password
       
    def login_for_GUI(self, username, password) :
        # check if the username and password match the registered ones
        return self.__username in username and self.__password == password
    def find_index(self,index,doctors):
        
            # check that the doctor id exists  
        return index in range(0,len(doctors))
            
    def get_doctor_details(self) :
        """
        Get the details needed to add a doctor
        Returns:
            first name, surname and ...
                            ... the speciality of the doctor in that order.
        """
        
        first_name = input("Enter the first name: ")
        surname = input("Enter the surname: ")
        speciality = input("Enter the specaility: ")





        return first_name, surname, speciality

    def doctor_management(self, doctors):
        """
        A method that deals with registering, viewing, updating, deleting doctors
        Args:
            doctors (list<Doctor>): the list of all the doctors names
        """

        print("-----Doctor Management-----")

        # menu
        print('Choose the operation:')
        print(' 1 - Register')
        print(' 2 - View')
        print(' 3 - Update')
        print(' 4 - Delete')

        
        op = input("Enter you option: ")


        # register
        if op == '1':
            print("-----Register-----")

            # get the doctor details
            print('Enter the doctor\'s details:')
            #ToDo4

            first_name, surname, speciality = self.get_doctor_details()

            # check if the name is already registered
            name_exists = False
            for doctor in doctors:
                if first_name == doctor.get_first_name() and surname == doctor.get_surname():
                    print('Name already exists.')                    
                    break # save time and end the loop
                else:
                    with open("doctor.txt",'a') as file:
                        file.write(f"\n")
                        file.write(f"{first_name},{surname},{speciality}")  # appending the newly registered doctor details in doctor.txt

                    print('Doctor registered.')
                    break

        # View
        elif op == '2':
            print("-----List of Doctors-----")
            
            print('ID |          Full name           |  Speciality')
            
            # doctors = self.load_doctor_file("doctor.txt")    #loading doctors details from doctor.txt and creating a list of instance called doctors    
            self.view(doctors)                 
 

        # Update
        elif op == '3':
            while True:
                print("-----Update Doctor`s Details-----")
                print('ID |          Full name           |  Speciality')

                # doctors = self.load_doctor_file("doctor.txt")
                
                self.view(doctors)
                try:
                    index = int(input('Enter the ID of the doctor: ')) - 1
                    doctor_index=self.find_index(index,doctors)  # checks if the id exists or not
                    if doctor_index!=False:  
                
                        break
                        
                    else:
                        print("Doctor not found")

                    
                        # doctor_index is the ID mines one (-1)
                        

                except ValueError: # the entered id could not be changed into an int
                    print('The ID entered is incorrect')

            # menu
            print('Choose the field to be updated:')
            print(' 1 First name')
            print(' 2 Surname')
            print(' 3 Speciality')
             

            try:
                op = int(input('Input: '))
                if op == 1:
                    new_first_name = input("Enter the new first name:")
                    # doctors[index].set_first_name(index,new_first_name,'doctor.txt')
                    doctors[index].set_first_name(new_first_name)
                    print("Doctors first name has been updated.")

                elif op == 2:
                    new_surname = input("Enter the new surname: ")
                    # doctors[index].set_surname(index,new_surname,'doctor.txt')
                    doctors[index].set_surname(new_surname)
                    print("Doctors surname has been updated.")



                elif op == 3:
                    new_speciality = input("Enter the new Speciality:")
                    # doctors[index].set_speciality(index,new_speciality,'doctor.txt')
                    doctors[index].set_speciality(new_speciality)
                    print(f"")
                    print("Doctors speciality has been updated.")


                else: 
                    print("Invalid input.")
            except ValueError:
                print("Only numbers are allowed.")

        # Delete
        elif op == '4':
            print("-----Delete Doctor-----")
            print('ID |          Full Name           |  Speciality')
            
            # doctors = self.load_doctor_file("doctor.txt")
            self.view(doctors)

            doctor_index = input('Enter the ID of the doctor to be deleted: ')
            
            if int(doctor_index) in range(1,len(doctors)+1):
                deleted_name = doctors.pop(int(doctor_index)-1)
                with open('doctor.txt','w') as file:
                    for id,doctor in enumerate(doctors):

                        if  id!= len(doctors) - 1:
                            file.write(f"{doctor.get_first_name()},{doctor.get_surname()},{doctor.get_speciality()}\n")

                        else:
                            file.write(f"{doctor.get_first_name()},{doctor.get_surname()},{doctor.get_speciality()}")

                    print("Doctor has been deleted.")

                return  # to check again as the returning True isn't of much value

           
            print('The id entered is incorrect')




        # if the id is not in the list of patients
        else:
            print('Invalid operation choosen. Check your spelling!')

    def appointments_management(self,doctors):
            

            print("1. Book Appointments\n2. View Appointment")
            op = input("Enter your options: ")

            if op == '1':

                print("------ Book Appointments ------")

                patients = self.load_patient_file("patient.txt")   

                self.view_patient(patients)

                patient_id = input("Enter the patient you want to appoint to: ")

                if self.find_index(int(patient_id) - 1, patients):
                    patient_to_appoint = patients[int(patient_id) - 1]
                
                    # doctors = self.load_doctor_file('doctor.txt')
                    print('ID |          Full Name           |  Speciality')

                    self.view(doctors)

            
                    doctor_id = input("Enter the doctor id: ")

                    new_index = int(doctor_id) - 1
                    current_date = datetime.date.today()
                    month_name = current_date.strftime("%B")
                    day_of_month = current_date.day
                    appointment_date =(month_name,day_of_month)
                    #patient data is send to set appointment
                    if self.find_index(new_index,doctors):
                        doctors[new_index].set_appointments(patient_to_appoint,month_name)
                    else:
                        print("Doctor ID not found!")
                
                else:
                    print("Patient ID not found !")

            elif op == '2':
                print("------- View Appointment -------")

                for id, doctor in enumerate(doctors):
                    appointment = doctor.get_appointments()
                    
                    print(f"{doctor.get_full_name()}: {len(appointment)} appointments")

            else:
                print("Invalid input!")

    def view_patient(self, patients):
        """
        print a list of patients
        Args:
            patients (list<Patients>): list of all the active patients
        """
        print("-----View Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        
        self.view(patients)

    def sort_by_surname_gui(self):
        patients = self.load_patient_file("patient.txt")   
        surnames = {}
        for patient in patients:
            if patient.get_surname() not in surnames:
                surnames[patient.get_surname()] = [patient]  # adding the patient object to the surname dictionary value by creating a new key
                
            else:
                surnames[patient.get_surname()].append(patient)
                #add the patient object to the surname key tha thas already appeared

        # print(surnames)
        return surnames
        
        # for surname in surnames:
        #     print(f"The {surname.capitalize()} Family:")
        #     # for fam in surnames[surname]: #accessing individual patient from the list
        #     self.view_patient(surnames[surname])
        #     print("\n")


    def patient_management(self,patients):
        print("1. View Patient")
        print("2. Add Patient")
        print("3. Patient family")
        op = input("Enter your option: ")

        if op == '1':

            # view patient
            patients = self.load_patient_file("patient.txt")   

            self.view_patient(patients)

        elif op == '2':

            # add patient 

            with open("patient.txt",'a') as file:
                first_name = input("Enter first name: ")
                surname = input("Enter surname: ")
                age = input("age: ")
                mobile = input("mobile: ")
                postcode = input("postcode: ")
                symptom = input("Enter symptoms(first_symptoms, second_symptoms): ")
                symptoms = symptom.split(", ")

                file.write("\n")
                file.write(
                    f"{first_name},{surname},{age},{mobile},{postcode},None,{','.join(symptoms)}"
                    )


            patients = self.load_patient_file("patient.txt")   
            print("Patient added successfully.")

        elif op == '3':
            patients = self.load_patient_file("patient.txt")   
            surnames = {}
            for patient in patients:
                if patient.get_surname() not in surnames:
                    surnames[patient.get_surname()] = [patient]  # adding the patient object to the surname dictionary value by creating a new key
                    
                else:
                    surnames[patient.get_surname()].append(patient)
                    #add the patient object to the surname key tha thas already appeared
            
            
            for surname in surnames:
                print(f"The {surname.capitalize()} Family:")
                # for fam in surnames[surname]: #accessing individual patient from the list
                self.view_patient(surnames[surname])
                print("\n")


    def assign_doctor_to_patient(self, patients, doctors):
        """
        Allow the admin to assign a doctor to a patient
        Args:
            patients (list<Patients>): the list of all the active patients
            doctors (list<Doctor>): the list of all the doctors
        """
        print("-----Assign-----")

        print("-----Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')


        self.view(patients)

        patient_index = input('Please enter the patient ID: ')

        try:
            # patient_index is the patient ID mines one (-1)
            patient_index = int(patient_index) -1

            # check if the id is not in the list of patients
            if patient_index not in range(len(patients)):
                print('The id entered was not found.')
                return # stop the procedures

        except ValueError: # the entered id could not be changed into an int
            print('The id entered is incorrect')
            return # stop the procedures

        print("-----Doctors Select-----")
        print('Select the doctor that fits these symptoms:')
        patients[patient_index].print_symptoms() # print the patient symptoms

        print('--------------------------------------------------')
        print('ID |          Full Name           |  Speciality   ')
        self.view(doctors)
        doctor_index = input('Please enter the doctor ID: ')

        try:
            # doctor_index is the patient ID mines one (-1)
            doctor_index = int(doctor_index) -1

            # check if the id is in the list of doctors
            if self.find_index(doctor_index,doctors)!=False:
                    
                # link the patients to the doctor and vice versa
                #ToDo11
                patients[patient_index].link(doctors[doctor_index].get_full_name())
                doctors[doctor_index].add_patient(patients[patient_index].get_full_name)     
                # .append(patients[patient_index].get_full_name())

                print('The patient is now assign to the doctor.')

            # if the id is not in the list of doctors
            else:
                print('The id entered was not found.')

        except ValueError: # the entered id could not be changed into an in
            print('The id entered is incorrect')




    def discharge(self, patients, discharged_patients):
        """
        Allow the admin to discharge a patient when treatment is done
        Args:
            patients (list<Patients>): the list of all the active patients
            discharge_patients (list<Patients>): the list of all the non-active patients
        """
        print("-----Discharge Patient-----")


      
        try:
            patient_index = int(input('Please enter the patient ID: '))

            if self.find_index(patient_index-1,patients):

                discharge_patient = patients.pop(patient_index - 1)
                discharged_patients.append(discharge_patient)
                with open("patient.txt","w") as file:

                    for n, patient in enumerate(patients):

                        if n != len(patients)-1:

                            row = f"{patient.get_first_name()},{patient.get_surname()},{patient.get_age()},{patient.get_mobile()},{patient.get_postcode()},{patient.get_doctor()},{','.join(patient.get_symptoms())}"

                            file.write(row + '\n')   

                        else:

                            row = f"{patient.get_first_name()},{patient.get_surname()},{patient.get_age()},{patient.get_mobile()},{patient.get_postcode()},{patient.get_doctor()},{','.join(patient.get_symptoms())}"

                            file.write(row)
            
                return True
            else: 
                return False

        except ValueError:
            print("Only numbers are allowed (1, 2, ...)")
        
        except Exception as e:
            print(e)



    def view_discharge(self, discharged_patients):
        """
        Prints the list of all discharged patients
        Args:
            discharge_patients (list<Patients>): the list of all the non-active patients
        """
        if discharged_patients :
            print("-----Discharged Patients-----")
            print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
            
            self.view(discharged_patients)

        else: 
            print("No patients are discharged yet.")

            
    def relocate_doctors(self, doctors, patients):
        print("-----Relocate-----")

        print("-----Patients to new doctor -----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        self.view(patients)

        patient_index = input('Please enter the patient ID: ')

        try:
            # patient_index is the patient ID mines one (-1)
            patient_index = int(patient_index) -1

            # check if the id is not in the list of patients
            if patient_index not in range(len(patients)):
                print('The id entered was not found.')
                return # stop the procedures

        except ValueError: # the entered id could not be changed into an int
            print('The id entered is incorrect')
            return # stop the procedures

        print("-----Doctors Select-----")
        print('Select new doctor:')
        # patients[patient_index].print_symptoms() # print the patient symptoms

        print('--------------------------------------------------')
        print('ID |          Full Name           |  Speciality   ')
        self.view(doctors)
        doctor_index = input('Please enter the doctor ID: ')

        try:
            # doctor_index is the patient ID mines one (-1)
            doctor_index = int(doctor_index) -1

            # check if the id is in the list of doctors
            if self.find_index(doctor_index,doctors)!=False:
                    
                # link the patients to the doctor and vice versa
                
                patients[patient_index].link(doctors[doctor_index].get_full_name())
                doctors[doctor_index].add_patient(patients[patient_index].get_full_name)     
                # .append(patients[patient_index].get_full_name())

                print('The patient is now assign to the doctor.')

            # if the id is not in the list of doctors
            else:
                print('The id entered was not found.')

        except ValueError: # the entered id could not be changed into an in
            print('The id entered is incorrect')

    def management_report(self, doctors,patients):


        # doctors = self.load_doctor_file("doctor.txt")
        # patients = self.load_patient_file("patient.txt")
        print('<----------- Management Report ------------>\n')

        print("----- Doctors info -----")
        print('--------------------------------------------------')
        print('ID |          Full Name           |  Speciality   ')
        self.view(doctors)
        print(f"The total no. of doctor : {len(doctors)}\n") # shows the total no. of doctor in the system.



        print("--- Patients per Doctor ---")

        for doctor in doctors:
            # print(doctor)
            if doctor.get_patients():
            
                # doctor.show_patient()
                print(f'Dr. {doctor.get_full_name()}: {len(doctor.get_patients())} patients')  #prints the total no. of patients per doctor
            else:
                print(f"Dr. {doctor.get_full_name()}: 0 patients.")

        doctor_names = [f"Dr. {doctor.get_full_name()}" for doctor in doctors]
        patient_counts = [len(doctor.get_patients()) for doctor in doctors]
        plt.bar(doctor_names, patient_counts)
        print("\n")



        print("----- Monthly appointments per doctor --------")


        for id, doctor in enumerate(doctors):
            monthly_patient = doctor.get_monthly_appointment().items()
            print(f"{id+1:>3}) {doctor.get_full_name()}")

            
            if monthly_patient:
                for month, patient in doctor.get_monthly_appointment().items():
                    
                    print(f"      {month}: {len(patient)} appointments")
                    print("\n")
                    

            else:
                print("    0 appointments for any months")
                print("\n")
        


        
        print(" ----- Illness type ------")

        patients_per_illness = self.sort_ilness(patients)

        for symptom,patient_no in patients_per_illness.items():
            print(f"{symptom:<10}: {patient_no} patients")


        plt.xlabel('Doctors')
        plt.ylabel('Number of Patients')
        plt.title('Patients per Doctor')
        plt.xticks(rotation=45, ha='right')
        plt.show()
            

        symptoms = list(patients_per_illness.keys())
        patient_numbers = list(patients_per_illness.values())
        plt.bar(symptoms, patient_numbers)
        plt.xlabel('Illness Type')
        plt.ylabel('Number of Patients')
        plt.title('Illness Type')
        plt.xticks(rotation=45, ha='right')
        plt.show()
         
        



    def update_details(self):
        """
        Allows the user to update and change username, password and address
        """

        print('Choose the field to be updated:')
        print(' 1 Username')
        print(' 2 Password')
        print(' 3 Address')

        try:
            op = int(input('Input: '))

            if op == 1:
                # set user name
                
                username = input("Enter the new username: ")
                if username == input("Enter the new username again: "):
                    with open('admin.txt', 'w') as file:
                        file.write(f"{username},{self.__password},{self.__address}")
                    print("New username has been set.")

                else: 
                    print("New username confirmation failed.")

                
            elif op == 2:
                password = input('Enter the new password: ')
                # validate the password
                if password == input('Enter the new password again: '):
                    with open('admin.txt', 'w') as file:
                        file.write(f"{self.__username},{password},{self.__address}")
                    print("New password has been set.")

                else:
                    print("New password has been set.")

            elif op == 3:   
                # set new address             
                address = input("Enter the new address: ")
                if address == input("Enter the new address again: "):
                    with open('admin.txt', 'w') as file:
                        file.write(f"{self.__username},{self.__password},{address}")
                    print("New address has been set.")

                else:
                    print("New address confirmation failed.")

            else:
                
                print("Invalid response. Enter(1/2/3)")

        except ValueError:
            print("Invalid response. Enter(1/2/3)")

        except Exception as e:
            print(e)

    


    def load_patient_file(self,file_name):
        patient_list = []

        try:
            with open(file_name, 'r') as file:
                for line in file:
                    # Split the line by comma to extract patient attributes
                    
                    string_list = line.split(",")
                    
                    # Create a new Patient object and append it to the patient_list
                    symptoms = string_list[6:]
                    symptoms = [symptom.lower() for symptom in symptoms]

                    symptoms[-1] = symptoms[-1].replace('\n', '')
                    patient_list.append(                     
                        Patient(string_list[0],string_list[1],string_list[2],string_list[3],string_list[4],string_list[5],symptoms)
                    )
        except Exception as e:
            print(f"Error: yes {e}")
        
        return patient_list
    
    def load_doctor_file(self,file_name):
        doctor_list = []

        try:
            with open(file_name, 'r') as file:
                for line in file:
                    # Split the line by comma to extract patient attributes
                    string_list = line.split(",")
                    # Create a new Patient object and append it to the patient_list
                    string_list[-1] = string_list[-1].replace('\n','')
                    
                    doctor_list.append(
                        Doctor(
                            first_name = string_list[0], 
                            surname = string_list[1], 
                            speciality = string_list[2], 
                            
                        )
                    )

        except Exception as e:
            print(f"Error: {e}")
            
        

       
        return doctor_list
    
    # def load_admin_file(self,file_name):

    
    def sort_ilness(self, patients):
        symptoms_and_patient = {}

        for patient in patients:
            for symptom in patient.get_symptoms():
                if symptom not in symptoms_and_patient:
                    symptoms_and_patient[symptom] = 1

                else:
                    symptoms_and_patient[symptom] += 1

        return symptoms_and_patient

