from Admin import Admin
from Doctor import Doctor
from Patient import Patient
from tkinter import messagebox
from tkinter import *
import tkinter as tk
import os

window = tk.Tk()
window.title("Login form")
window.geometry("340x440")
window.configure(bg="black")

frame = tk.Frame(bg="black")

# Getting the root directory
root_dir = os.path.dirname(__file__)

with open(os.path.join(root_dir, 'admin.txt'), 'r') as file:
    line = file.readline()
    line_list = line.split(',')
    admin_username = line_list[0]
    admin_password = line_list[1]
    admin_address = line_list[2]

admin = Admin(admin_username, admin_password, admin_address)
# doctors = admin.load_doctor_file("doctor.txt")
# patients = admin.load_doctor_file("patient.txt")

doctor_file_path = os.path.join(root_dir, "doctor.txt")
patient_file_path = os.path.join(root_dir, "patient.txt")
# Load the files
doctors = admin.load_doctor_file(doctor_file_path)
patients = admin.load_patient_file(patient_file_path)

discharged_patients = []

# Define username_entry and password_entry as global variables
username_entry = None
password_entry = None




def main_operations():
    main_window = tk.Tk()
    main_window.title("Main Operations")
    menu_frame = tk.Frame(main_window)
    menu_frame.pack(expand=True)

    # Create buttons for each operation
    operations = [
        ("Register/view/update/delete doctor", doctor_management),
        ("Book appointments/View appointments", appointments_management),
        ("View/add patient/patient's family", patient_management),
        ("Discharge patients", discharge),
        ("View discharged patient", view_discharge),
        ("Assign doctor to a patient", assign_doctor_to_patient),
        ("Update admin details",update_details),
        # ("Store patient details", add_patient_data),
        ("Relocate the patient", relocate_doctors),
        ("Show management report", management_report),
    ]

    # Calculate number of rows and columns
    num_rows = (len(operations) + 1) // 2  # Add 1 for the Quit button
    num_columns = 2

    # Create and place buttons
    for i, (text, command) in enumerate(operations):
        button = tk.Button(
            menu_frame, text=text, font=("Arial", 12), command=command,
            bg="#2E8BC0", fg="white", bd=0, padx=10, pady=5,
            relief=tk.RIDGE, borderwidth=3, width=30
        )

        row = i // num_columns
        column = i % num_columns
        button.grid(row=row, column=column, padx=5, pady=5)

    quit_button = tk.Button(
            menu_frame, text="Quit", font=("Arial", 12),
            command=quit_application, bg="#2E8BC0", fg="white",
            bd=0, padx=10, pady=5, relief=tk.RIDGE, borderwidth=3, width=60
        )
    quit_button.grid(row=num_rows, columnspan=num_columns, padx=5, pady=5)
    
def doctor_management():   
    
    doctor_window = Toplevel()
    doctor_window.title("Doctor Management")
    doctor_window.geometry('400x300')
    doctor_window.configure(bg='#333333')

    # Create a frame to hold widgets
    doctor_frame = Frame(doctor_window, bg='#333333')
    doctor_frame.pack(expand=True)

    # Create buttons for each doctor operation
    operations = [
        ("Register Doctor", register_doctor),
        ("View Doctors", view_doctors),
        ("Update Doctor", update_doctor),
        ("Delete Doctor", delete_doctor)
    ]

    # Calculate number of rows and columns for button placement
    num_rows = len(operations)
    num_columns = 1

    # Create and place buttons
    for i, (text, command) in enumerate(operations):
        button = Button(
            doctor_frame, text=text, font=("Arial", 12), command=command,
            bg="#2E8BC0", fg="white", bd=0, padx=10, pady=5,
            relief=RIDGE, borderwidth=3, width=30
        )

        row = i
        column = 0
        button.grid(row=row, column=column, padx=5, pady=5)

def register_doctor():
    register_window = Toplevel()
    register_window.title("Register Doctor")
    register_window.geometry('300x200')
    register_window.configure(bg='#333333')

    register_frame = Frame(register_window, bg='#333333')
    register_frame.pack(expand=True)

    title_label = Label(register_frame, text="Register Doctor", fg="#ffffff", bg="#333333", font='Arial,16')
    title_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

    first_name_label = Label(register_frame, text="First Name", fg="#ffffff", bg="#333333", font='Arial,12')
    first_name_label.grid(row=1, column=0)
    first_name_entry = Entry(register_frame)
    first_name_entry.grid(row=1, column=1, pady=10)

    surname_label = Label(register_frame, text="Surname", fg="#ffffff", bg="#333333", font='Arial,12')
    surname_label.grid(row=2, column=0)
    surname_entry = Entry(register_frame)
    surname_entry.grid(row=2, column=1, pady=10)

    speciality_label = Label(register_frame, text="Speciality", fg="#ffffff", bg="#333333", font='Arial,12')
    speciality_label.grid(row=3, column=0)
    speciality_entry = Entry(register_frame)
    speciality_entry.grid(row=3, column=1, pady=10)

    def add_doctor():
        first_name = first_name_entry.get()
        surname = surname_entry.get()
        speciality = speciality_entry.get()

        if first_name and surname and speciality:
            
            doctors.append(Doctor(first_name,surname,speciality))
            messagebox.showinfo("Success", "Doctor registered successfully!")
            register_window.destroy()
        else:
            messagebox.showerror("Error", "Please fill in all fields.")

    register_button = Button(register_frame, text="Register", bg='#ff3399', fg='#fff', padx=10, pady=0, font='Arial,12', command=add_doctor)
    register_button.grid(row=4, column=0, columnspan=2, pady=10)


def view_doctors():
    view_window = Toplevel()
    view_window.title("View Doctors")
    view_window.geometry('400x300')
    view_window.configure(bg='#333333')

    view_frame = Frame(view_window, bg='#333333')
    view_frame.pack(expand=True)

    title_label = Label(view_frame, text="List of Doctors", fg="#ffffff", bg="#333333", font='Arial,16')
    title_label.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

    id_label = Label(view_frame, text="ID", fg="#ffffff", bg="#333333", font='Arial,12', width=5)
    id_label.grid(row=1, column=0)
    name_label = Label(view_frame, text="Name", fg="#ffffff", bg="#333333", font='Arial,12', width=20)
    name_label.grid(row=1, column=1)
    speciality_label = Label(view_frame, text="Speciality", fg="#ffffff", bg="#333333", font='Arial,12', width=15)
    speciality_label.grid(row=1, column=2)

    def display_doctor_details():
        for i, doctor in enumerate(doctors, start=2):
            id_label = Label(view_frame, text=i-1, fg="#ffffff", bg="#333333", font='Arial,12')
            id_label.grid(row=i, column=0)
            name_label = Label(view_frame, text=doctor.get_full_name(), fg="#ffffff", bg="#333333", font='Arial,12')
            name_label.grid(row=i, column=1)
            speciality_label = Label(view_frame, text=doctor.get_speciality(), fg="#ffffff", bg="#333333", font='Arial,12')
            speciality_label.grid(row=i, column=2)

    display_doctor_details()
    
def update_doctor():
    update_window = Toplevel()
    update_window.title("Update Doctor")
    update_window.geometry('300x200')
    update_window.configure(bg='#333333')

    update_frame = Frame(update_window, bg='#333333')
    update_frame.pack(expand=True)

    title_label = Label(update_frame, text="Update Doctor", fg="#ffffff", bg="#333333", font='Arial,16')
    title_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

    select_label = Label(update_frame, text="Select Doctor", fg="#ffffff", bg="#333333", font='Arial,12')
    select_label.grid(row=1, column=0)
    select_entry = Entry(update_frame)
    select_entry.grid(row=1, column=1, pady=10)

    first_name_label = Label(update_frame, text="First Name", fg="#ffffff", bg="#333333", font='Arial,12')
    first_name_label.grid(row=2, column=0)
    first_name_entry = Entry(update_frame)
    first_name_entry.grid(row=2, column=1, pady=10)

    surname_label = Label(update_frame, text="Surname", fg="#ffffff", bg="#333333", font='Arial,12')
    surname_label.grid(row=3, column=0)
    surname_entry = Entry(update_frame)
    surname_entry.grid(row=3, column=1, pady=10)

    speciality_label = Label(update_frame, text="Speciality", fg="#ffffff", bg="#333333", font='Arial,12')
    speciality_label.grid(row=4, column=0)
    speciality_entry = Entry(update_frame)
    speciality_entry.grid(row=4, column=1, pady=10)

    def find_doctor():
        index = int(select_entry.get()) - 1
        index_status = admin.find_index(index,doctors)
        if index_status:
            doctor = doctors[index]
            first_name_entry.delete(0, END)
            first_name_entry.insert(0, doctor.get_first_name())
            surname_entry.delete(0, END)
            surname_entry.insert(0, doctor.get_surname())
            speciality_entry.delete(0, END)
            speciality_entry.insert(0, doctor.get_speciality())
        else:
            messagebox.showerror("Error", "Invalid doctor ID.")

    def update_doctor_details():
        global doctors
        index = int(select_entry.get()) - 1
        if 0 <= index < len(doctors):
            first_name = first_name_entry.get()
            surname = surname_entry.get()
            speciality = speciality_entry.get()

            if first_name and surname and speciality:
                doctors[index].set_first_name(first_name)
                doctors[index].set_surname(surname)
                doctors[index].set_speciality(speciality)



                messagebox.showinfo("Success", "Doctor details updated successfully!")
                update_window.destroy()
            else:
                messagebox.showerror("Error", "Please fill in all fields.")
        else:
            messagebox.showerror("Error", "Invalid doctor ID.")

    select_button = Button(update_frame, text="Select", bg='#ff3399', fg='#fff', padx=10, pady=0, font='Arial,12', command=find_doctor)
    select_button.grid(row=1, column=2, pady=10)

    update_button = Button(update_frame, text="Update", bg='#ff3399', fg='#fff', padx=10, pady=0, font='Arial,12', command=update_doctor_details)
    update_button.grid(row=5, column=0, columnspan=2, pady=10)

def delete_doctor():
    delete_window = Toplevel()
    delete_window.title("Delete Doctor")
    delete_window.geometry('300x200')
    delete_window.configure(bg='#333333')

    delete_frame = Frame(delete_window, bg='#333333')
    delete_frame.pack(expand=True)

    title_label = Label(delete_frame, text="Delete Doctor", fg="#ffffff", bg="#333333", font='Arial,16')
    title_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

    # Function to display the list of doctors
    def display_doctors():
        doctors_listbox.delete(0, END)
        for i, doctor in enumerate(doctors, 1):
            doctors_listbox.insert(END, f"{i}. {doctor.get_full_name()} - {doctor.get_speciality()}")

    select_label = Label(delete_frame, text="Select Doctor to Delete:", fg="#ffffff", bg="#333333", font='Arial,12')
    select_label.grid(row=1, column=0, columnspan=2, pady=(0, 5))

    # Listbox to display doctors
    doctors_listbox = Listbox(delete_frame, bg="#ffffff", fg="#333333", font='Arial,12', selectmode=SINGLE, height=5, width=30)
    doctors_listbox.grid(row=2, column=0, columnspan=2, pady=(0, 5))

    display_doctors()

    def delete_selected_doctor():
        selected_index = doctors_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            confirm = messagebox.askyesno("Confirm Deletion", "Are you sure you want to delete this doctor?")
            if confirm:
                del doctors[index]
                messagebox.showinfo("Success", "Doctor deleted successfully!")
                display_doctors()
        else:
            messagebox.showerror("Error", "Please select a doctor to delete.")

    delete_button = Button(delete_frame, text="Delete", bg='#ff3399', fg='#fff', padx=10, pady=0, font='Arial,12', command=delete_selected_doctor)
    delete_button.grid(row=3, column=0, columnspan=2, pady=10)


# def delete_doctor():
#     # Implement functionality to delete a doctor
#     pass


def appointments_management():
    pass




def patient_management():
    def view_patients():
        

        # Create a new window for displaying patient information
        patient_window = tk.Toplevel()
        patient_window.title("View Patients")
        patient_window.configure(bg="black")
        patient_window.geometry("500x300")
        # Create a frame to hold the patient information
        frame = tk.Frame(patient_window)
        frame.pack()

        # Create labels for column headings
        headings = ['ID', 'Full Name', 'Doctor', 'Age', 'Mobile', 'Postcode']
        for i, heading in enumerate(headings):
            label = tk.Label(frame, text=heading, font=('Arial', 12, 'bold'))
            label.grid(row=0, column=i, padx=5, pady=5)

        # Display patient information
        for i, patient in enumerate(patients):
            # Get patient details
            patient_id = i + 1
            full_name = patient.get_full_name()
            doctor_assigned = patient.get_doctor()
            age = patient.get_age()
            mobile = patient.get_mobile()
            postcode = patient.get_postcode()

            # Display patient details in labels
            tk.Label(frame, text=patient_id).grid(row=i+1, column=0, padx=5, pady=5)
            tk.Label(frame, text=full_name).grid(row=i+1, column=1, padx=5, pady=5)
            tk.Label(frame, text=doctor_assigned).grid(row=i+1, column=2, padx=5, pady=5)
            tk.Label(frame, text=age).grid(row=i+1, column=3, padx=5, pady=5)
            tk.Label(frame, text=mobile).grid(row=i+1, column=4, padx=5, pady=5)
            tk.Label(frame, text=postcode).grid(row=i+1, column=5, padx=5, pady=5)



    def add_patient():
        def save_patient():
            # Get patient details from entry fields
            first_name = first_name_entry.get()
            surname = surname_entry.get()
            symptoms = symptoms_entry.get()
            age = int(age_entry.get())
            mobile = mobile_entry.get()
            postcode = postcode_entry.get()

            # Create a new Patient object with the provided details
            new_patient = Patient(first_name, surname, symptoms, age, mobile, postcode)

            # Append the new patient to the list of patients
            patients.append(new_patient)

            # Display a confirmation message
            tk.messagebox.showinfo("Success", "Patient added successfully!")

            # Close the add patient window
            add_patient_window.destroy()

        # Create a new window for adding a patient
        add_patient_window = tk.Toplevel()
        add_patient_window.title("Add Patient")

        # Create a frame to hold patient entry fields
        frame = tk.Frame(add_patient_window)
        frame.pack(padx=10, pady=10)

        # Labels and entry fields for patient details
        tk.Label(frame, text="First Name:").grid(row=0, column=0, padx=5, pady=5)
        first_name_entry = tk.Entry(frame)
        first_name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame, text="Surname:").grid(row=1, column=0, padx=5, pady=5)
        surname_entry = tk.Entry(frame)
        surname_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(frame, text="Symptoms:").grid(row=2, column=0, padx=5, pady=5)
        symptoms_entry = tk.Entry(frame)
        symptoms_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(frame, text="Age:").grid(row=3, column=0, padx=5, pady=5)
        age_entry = tk.Entry(frame)
        age_entry.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(frame, text="Mobile:").grid(row=4, column=0, padx=5, pady=5)
        mobile_entry = tk.Entry(frame)
        mobile_entry.grid(row=4, column=1, padx=5, pady=5)

        tk.Label(frame, text="Postcode:").grid(row=5, column=0, padx=5, pady=5)
        postcode_entry = tk.Entry(frame)
        postcode_entry.grid(row=5, column=1, padx=5, pady=5)

        # Button to save the patient details
        save_button = tk.Button(add_patient_window, text="Save", command=save_patient)
        save_button.pack(pady=10)

      # Your code for adding a patient goes here

    def group_by_surname_gui():
        # Create a new window for displaying grouped patient data
        group_window = Toplevel()
        group_window.title("Group Patients by Surname")
        
        # Create a frame to hold the grouped patient data
        group_frame = Frame(group_window)
        group_frame.pack()

        # Create labels and entry fields to display grouped patient data
        Label(group_frame, text="Surname", font=("Arial", 12, "bold")).grid(row=0, column=0, padx=10, pady=5)
        Label(group_frame, text="Patients", font=("Arial", 12, "bold")).grid(row=0, column=1, padx=10, pady=5)

        # Group patients by surname
        
        grouped_patients= admin.sort_by_surname_gui()
        print(grouped_patients)
        # Display grouped patient data
        # row_num = 1
        # for surname, patients_list in grouped_patients.items():
        #     Label(group_frame, text=surname).grid(row=row_num, column=0, padx=10, pady=5)
        #     patients_text = "\n".join([f"{patient.get_full_name()} - {patient.get_doctor()}" for patient in patients_list])
        #     Label(group_frame, text=patients_text, justify=LEFT).grid(row=row_num, column=1, padx=10, pady=5)
        #     row_num += 1
  # Your code for grouping patient data by surname goes here

    # Create the main window for patient management
    patient_window = tk.Toplevel()
    patient_window.title("Patient Management")
    
    # Create a frame to hold the patient management options
    frame = tk.Frame(patient_window)
    frame.pack()

    # Create buttons for each patient management option
    view_button = tk.Button(frame, text="View Patients", command=view_patients, bg="blue", fg="red")
    view_button.pack(pady=5)
    
    add_button = tk.Button(frame, text="Add Patient", command=add_patient, bg="blue", fg="red")
    add_button.pack(pady=5)
    
    group_button = tk.Button(frame, text="Group by Surname", command=group_by_surname_gui, bg="blue", fg="red")
    group_button.pack(pady=5)

# Example usage
# Assuming 'patients' is a list of Patient objects
# patient_management(patients)




def discharge():
    pass

def view_discharge():
    pass

def assign_doctor_to_patient():
    pass

def update_details():
    update_details_window = Toplevel()
    update_details_window.title("Update Details")
    update_details_window.geometry('300x200')
    update_details_window.configure(bg='#333333')

    update_details_frame = Frame(update_details_window, bg='#333333')
    update_details_frame.pack(expand=True)

    title_label = Label(update_details_frame, text="Update Details", fg="#ffffff", bg="#333333", font='Arial,16')
    title_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

    # Function to handle updating details
    def update():
        new_username = username_entry.get()
        new_password = password_entry.get()
        confirm_password = confirm_password_entry.get()

        if new_password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match.")
            return
        
       
        with open(os.path.join(root_dir, 'admin.txt'), 'w') as file:        
            file.write(f"{new_username},{new_password},{admin.get_address()}")
        # Update username and password (replace with your logic)
        # For demonstration purposes, printing the updated details

        messagebox.showinfo("Success", "Details updated successfully.")

    username_label = Label(update_details_frame, text="New Username:", fg="#ffffff", bg="#333333", font='Arial,12')
    username_label.grid(row=1, column=0, padx=10, pady=5)
    username_entry = Entry(update_details_frame)
    username_entry.grid(row=1, column=1, padx=10, pady=5)

    password_label = Label(update_details_frame, text="New Password:", fg="#ffffff", bg="#333333", font='Arial,12')
    password_label.grid(row=2, column=0, padx=10, pady=5)
    password_entry = Entry(update_details_frame, show='*')
    password_entry.grid(row=2, column=1, padx=10, pady=5)

    confirm_password_label = Label(update_details_frame, text="Confirm Password:", fg="#ffffff", bg="#333333", font='Arial,12')
    confirm_password_label.grid(row=3, column=0, padx=10, pady=5)
    confirm_password_entry = Entry(update_details_frame, show='*')
    confirm_password_entry.grid(row=3, column=1, padx=10, pady=5)

    update_button = Button(update_details_frame, text="Update", bg='#ff3399', fg='#fff', font='Arial,12', command=update)
    update_button.grid(row=4, column=0, columnspan=2, pady=10)

def add_patient_data():
    pass

def relocate_doctors():
    pass

def management_report():
    pass

def quit_application():
    window.quit()

def login():
    global username_entry, password_entry
    username = admin.get_username()
    password = admin.get_password()
    if username_entry.get() == username and password_entry.get() == password:
        messagebox.showinfo(title="Login Success", message="You are successfully logged in.")
        
        window.withdraw()
        main_operations()
    else:
        messagebox.showinfo(title="Error", message="Invalid login.")

#creating widgets
def start():
    global username_entry, password_entry
    login_label = tk.Label(frame, text="Admin  Login", bg="black", fg="#FF3399", font=("Arial", 30))
    username_label = tk.Label(frame, text="Username", bg="black", fg="white", font=("Arial", 16))
    username_entry = tk.Entry(frame)
    password_label = tk.Label(frame, text="Password", bg="black", fg="white", font=("Arial", 16))
    password_entry = tk.Entry(frame, show="*")
    login_button = tk.Button(frame, text="Login", bg="#FF3399", fg="white", font=("Arial", 16), command=login)

    #placing widgets on the screen
    login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
    username_label.grid(row=1, column=0)
    username_entry.grid(row=1, column=1, pady=20)
    password_label.grid(row=2, column=0)
    password_entry.grid(row=2, column=1, pady=20)
    login_button.grid(row=3, column=0, columnspan=2, pady=30)

    frame.pack()

# Define empty functions for each operation


start()

window.mainloop()
