# Imports
from Admin import Admin
from Doctor import Doctor
from Patient import Patient


def main():
    """
    the main function to be ran when the program runs
    """

    # Initialising the actors

    with open('admin.txt','r') as file:
        line = file.readline()
        line_list = line.split(',')
        admin_username = line_list[0]
        admin_password = line_list[1]
        admin_address = line_list[2]

    admin = Admin(admin_username,admin_password,admin_address) # username is 'admin', password is '123'
    

    # doctors = [Doctor('John','Smith','Internal Med.'), Doctor('Jone','Smith','Pediatrics'), Doctor('Jone','Carlos','Cardiology')]
    doctors = admin.load_doctor_file("doctor.txt")

    # patients = [Patient('Sara','Smith', 20, '07012345678','B1 234'), Patient('Mike','Jones', 37,'07555551234','L2 2AB'), Patient('Daivd','Smith', 15, '07123456789','C1 ABC')]
    patients = admin.load_patient_file("patient.txt")  # oading patient data from patient.txt file
  
    discharged_patients = []

    # keep trying to login tell the login details are correct
    while True:
        if admin.login():
            running = True # allow the program to run
            break
        else:
            print('Incorrect username or password.')

    while running:
        # print the menu
        print("\n")
        print('Choose the operation:')
        print(' 1- Register/view/update/delete doctor')
        print(' 2- Book appointments/ View appointments')
        print(' 3- view/add patient/patient\'s family')
        print(' 4- Discharge patients')
        print(' 5- View discharged patient')
        print(' 6- Assign doctor to a patient')
        print(' 7- Update admin details')
        print(' 8- Relocate the patient')
        print(' 9- Show management report')
        print(' 10- Quit')
        

        # get the option
        op = input('Option: ')

        if op == '1':
            # 1- Register/view/update/delete doctor
            print("\n")
            admin.doctor_management(doctors)

        elif op == "2":
            # 2- Book appointments/ View appointments
            admin.appointments_management(doctors)


        elif op == "3":
            # 3- view/add patient/patient\'s family group
            admin.patient_management(patients)

        elif op == '4':
            # 4- View or discharge patients            
            patients = admin.load_patient_file("patient.txt")

            admin.view_patient(patients)

            while True:
                op = input('Do you want to discharge a patient(Y/N):').lower()
                
                if op == 'yes' or op == 'y':
                    
                    discharged_status = admin.discharge(patients, discharged_patients)
                    if discharged_status:
                        print("The patient is discharged.")
                        
                    
                    else:
                        print("Index not found or invalid input.")

                    
                        

                elif op == 'no' or op == 'n':
                    break

                # unexpected entry
                else:
                    print('Please answer by yes or no.')
        
        elif op == '5':
            # 5 - view discharged patients
            admin.view_discharge(discharged_patients)

        elif op == '6':
            # 6- Assign doctor to a patient
            admin.assign_doctor_to_patient(patients, doctors)

        elif op == '7':
            # 7- Update admin detais
            admin.update_details()

        elif op == '8':
            # 8- rellocate doctors        
            admin.relocate_doctors(doctors, patients)

        elif op == '9':


            admin.management_report(doctors,patients)
        
        elif op == '10':
            # 6 - Quit
            print("<------------ goodbye-------------->")
            break

        else:
            # the user did not enter an option that exists in the menu
            print('Invalid option. Try again')

if __name__ == '__main__':
    main()
