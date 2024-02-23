# Imports
from Admin import Admin
from Doctor import Doctor
from Patient import Patient
from tkinter import END 
import tkinter as tk


class Main:
    """
    the main function to be ran when the program runs
    """
    def __init__(self):
    # Initialising the actors

        with open('admin.txt','r') as file:
            line = file.readline()
            line_list = line.split(',')
            admin_username = line_list[0]
            admin_password = line_list[1]
            admin_address = line_list[2]

        self.admin = Admin(admin_username,admin_password,admin_address) # username is 'admin', password is '123'
    

    # doctors = [Doctor('John','Smith','Internal Med.'), Doctor('Jone','Smith','Pediatrics'), Doctor('Jone','Carlos','Cardiology')]
        self.doctors = self.admin.load_doctor_file("doctor.txt")

    # patients = [Patient('Sara','Smith', 20, '07012345678','B1 234'), Patient('Mike','Jones', 37,'07555551234','L2 2AB'), Patient('Daivd','Smith', 15, '07123456789','C1 ABC')]
        self.patients = self.admin.load_patient_file("patient.txt")  # oading patient data from patient.txt file
  
        discharged_patients = []

        self.window = tk.Tk()
        self.window.geometry("350x350")

        self.on_start_show_admin_log_in()

    def on_start_show_admin_log_in(self):
        self.window.title("Admin Log In")

        self.total_text_label = tk.Label(self.window, text="-----Login-----")
        self.total_text_label.grid(row=0, column=0, columnspan=3)

        self.username_label = tk.Label(self.window, text="Enter the username:")
        self.username_label.grid(row=1, column=0)

        self.username_entry = tk.Entry(self.window)
        self.username_entry.grid(row=1, column=1)

        self.password_label = tk.Label(self.window, text="Enter the password:")
        self.password_label.grid(row=2, column=0)

        self.password_entry = tk.Entry(self.window)
        self.password_entry.grid(row=2, column=1)

        self.logIn_button = tk.Button(self.window, text="Log In", command=self.admin_logIn_action)
        self.logIn_button.grid(row=3, column=0, columnspan=3)

        self.alert_variable = tk.StringVar()
        self.alert_variable.set("")
        self.alert_label = tk.Label(self.window, textvariable=self.alert_variable)
        self.alert_label.grid(row=4, column=0, columnspan=3)
        # self.make_window_responsive(5,2)

    def admin_logIn_action(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if self.admin.login_for_GUI(username, password):
            self.home_window()
        else:
            self.username_entry.delete(0, "end") # Clearing userinput entry field
            self.password_entry.delete(0, "end") # Clearing userinput entry field

            self.alert_label.config(fg= "red")
            self.alert_variable.set("Incorrect username or password.")

    def clear_previous_widgets(self):
        for widget in self.window.winfo_children():
            widget.destroy()

    def home_window(self):
        self.clear_previous_widgets()
        self.window.geometry("320x350")

        self.window.title("Hospital Management System")

        index_options = [
            "Register/view/update/delete doctor",
            "Add patients",
            "View/Discharge patients",
            "View discharged patient",
            "Book appointment/check appointment status",
            "Assign doctor to a patient",
            "Relocate a patient from one doctor to another",
            "Update admin detais",
            "Request management report",
            "Quit"
        ]
        index_button_actions = [
            self.doctor_management_action,
            self.add_patient_action,
            self.view_or_discharge_patient_action,
            self.view_discharged_patient,
            self.appointment_management_action,
            self.assign_doctor_to_patient_action,
            self.relocate_patient_to_another_doctor_action,
            self.update_admin_details_action,
            self.request_management_report_action,
            self.stop,
        ]

        self.text_label = tk.Label(self.window, text="Choose the operation:")
        self.text_label.grid(row=0, column=0)

        self.add_multiple_widgets(1, index_options, index_button_actions)

        self.make_window_responsive(11,1)

    def start(self):
        self.window.mainloop()
window = Main()
window.start()

#     # keep trying to login tell the login details are correct
#     while True:
#         if admin.login():
#             running = True # allow the program to run
#             break
#         else:
#             print('Incorrect username or password.')

#     while running:
#         # print the menu
#         print("\n")
#         print('Choose the operation:')
#         print(' 1- Register/view/update/delete doctor')
#         print(' 2- Book appointments/ View appointments')
#         print(' 3- view/add patient/patient\'s family')
#         print(' 4- Discharge patients')
#         print(' 5- View discharged patient')
#         print(' 6- Assign doctor to a patient')
#         print(' 7- Update admin details')
#         print(' 8- Relocate the patient')
#         print(' 9- Show management report')
#         print(' 10- Quit')
        

#         # get the option
#         op = input('Option: ')

#         if op == '1':
#             # 1- Register/view/update/delete doctor
#             print("\n")
#             admin.doctor_management(doctors)

#         elif op == "2":
#             # 2- Book appointments/ View appointments
#             admin.appointments_management()


#         elif op == "3":
#             # 3- view/add patient/patient\'s family group
#             admin.patient_management(patients)

#         elif op == '4':
#             # 4- View or discharge patients            
#             patients = admin.load_patient_file("patient.txt")

#             admin.view_patient(patients)

#             while True:
#                 op = input('Do you want to discharge a patient(Y/N):').lower()
                
#                 if op == 'yes' or op == 'y':
                    
#                     discharged_status = admin.discharge(patients, discharged_patients)
#                     if discharged_status:
#                         print("The patient is discharged.")
                        
                    
#                     else:
#                         print("Index not found or invalid input.")

                    
                        

#                 elif op == 'no' or op == 'n':
#                     break

#                 # unexpected entry
#                 else:
#                     print('Please answer by yes or no.')
        
#         elif op == '5':
#             # 5 - view discharged patients
#             admin.view_discharge(discharged_patients)

#         elif op == '6':
#             # 6- Assign doctor to a patient
#             admin.assign_doctor_to_patient(patients, doctors)

#         elif op == '7':
#             # 7- Update admin detais
#             admin.update_details()

#         elif op == '8':
#             # 8- rellocate doctors        
#             admin.relocate_doctors(doctors, patients)

#         elif op == '9':


#             admin.management_report(doctors,patients)
        
#         elif op == '10':
#             # 6 - Quit
#             print("<------------ goodbye-------------->")
#             break

#         else:
#             # the user did not enter an option that exists in the menu
#             print('Invalid option. Try again')

# if __name__ == '__main__':
#     main()
