from Admin import Admin
from Doctor import Doctor
from Patient import Patient
from tkinter import messagebox
from tkinter import *
import tkinter as tk
import os
import datetime
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

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
        ("Book appointments/View appointments", appointment_management),
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


from tkinter import *
from tkinter import ttk

from tkinter import *
from tkinter import messagebox

def appointment_management():
    appointment_window = Toplevel()
    appointment_window.title("Appointment Management")

    selected_patient = None
    selected_doctor = None

    def book_appointment():
        if selected_patient and selected_doctor:
            # Book appointment logic here
            messagebox.showinfo("Success", "Appointment booked successfully!")
        else:
            messagebox.showerror("Error", "Please select a patient and a doctor.")

    def select_patient():
        nonlocal selected_patient
        selected_patient_index = patient_listbox.curselection()
        if selected_patient_index:
            selected_patient = patients[selected_patient_index[0]]
            patient_selected_label.config(text=f"Patient Selected: {selected_patient.get_full_name()}")
        else:
            messagebox.showerror("Error", "Please select a patient.")

    def select_doctor():
        nonlocal selected_doctor
        selected_doctor_index = doctor_listbox.curselection()
        if selected_doctor_index:

            
            current_date = datetime.date.today()
            month_name = current_date.strftime("%B")
            day_of_month = current_date.day
            appointment_date =(month_name,day_of_month)
            selected_doctor = doctors[selected_doctor_index[0] - 1]
            selected_doctor.set_appointments(selected_patient,month_name)
            
            doctor_selected_label.config(text=f"Doctor Selected: {selected_doctor.get_full_name()}")
        else:
            messagebox.showerror("Error", "Please select a doctor.")

    def view_appointments():
        view_appointments_window = Toplevel()
        view_appointments_window.title("View Appointments")

        appointments_text = ""
        for id, doctor in enumerate(doctors):
            appointments = doctor.get_appointments()
            appointments_text += f"Dr. {doctor.get_full_name()}: {len(appointments)} appointments\n"

        appointments_label = Label(view_appointments_window, text=appointments_text)
        appointments_label.pack(padx=10, pady=10)

    book_appointment_button = Button(appointment_window, text="Book Appointment", command=book_appointment)
    book_appointment_button.pack(pady=5)

    view_appointments_button = Button(appointment_window, text="View Appointments", command=view_appointments)
    view_appointments_button.pack(pady=5)

    # Frame for patient selection
    patient_frame = Frame(appointment_window)
    patient_frame.pack(pady=10)

    patient_label = Label(patient_frame, text="Select Patient:")
    patient_label.grid(row=0, column=0)

    patient_listbox = Listbox(patient_frame, height=5)
    for patient in patients:
        patient_listbox.insert(END, patient.get_full_name())
    patient_listbox.grid(row=0, column=1)

    select_patient_button = Button(patient_frame, text="Select Patient", command=select_patient)
    select_patient_button.grid(row=1, columnspan=2, pady=5)

    patient_selected_label = Label(patient_frame, text="")
    patient_selected_label.grid(row=2, columnspan=2)

    # Frame for doctor selection
    doctor_frame = Frame(appointment_window)
    doctor_frame.pack(pady=10)

    doctor_label = Label(doctor_frame, text="Select Doctor:")
    doctor_label.grid(row=0, column=0)

    doctor_listbox = Listbox(doctor_frame, height=5)
    for doctor in doctors:
        doctor_listbox.insert(END, doctor.get_full_name())
    doctor_listbox.grid(row=0, column=1)

    select_doctor_button = Button(doctor_frame, text="Select Doctor", command=select_doctor)
    select_doctor_button.grid(row=1, columnspan=2, pady=5)

    doctor_selected_label = Label(doctor_frame, text="")
    doctor_selected_label.grid(row=2, columnspan=2)

    appointment_window.mainloop()

# Assuming `doctors` and `patients` are lists of Doctor and Patient objects respectively









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
        # print(grouped_patients)
        # Display grouped patient data
        row_num = 1
        for surname, patients_list in grouped_patients.items():
            Label(group_frame, text=surname).grid(row=row_num, column=0, padx=10, pady=5)
            patients_text = "\n".join([f"{patient.get_full_name()} - {patient.get_doctor()}" for patient in patients_list])
            Label(group_frame, text=patients_text, justify=LEFT).grid(row=row_num, column=1, padx=10, pady=5)
            row_num += 1
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


# Function to discharge a patient
def discharge():
    discharge_window = Toplevel()
    discharge_window.title("Discharge Patient")
    discharge_window.geometry('400x300')
    discharge_window.configure(bg='#333333')

    discharge_frame = Frame(discharge_window, bg='#333333')
    discharge_frame.pack(expand=True)

    title_label = Label(discharge_frame, text="Discharge Patient", fg="#ffffff", bg="#333333", font='Arial,16')
    title_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

    # Function to display the list of patients
    def display_patients():
        patients_listbox.delete(0, END)
        for i, patient in enumerate(patients, 1):
            patients_listbox.insert(END, f"{i}. {patient.get_full_name()} - Dr. {patient.get_doctor()}")

    select_label = Label(discharge_frame, text="Select Patient to Discharge:", fg="#ffffff", bg="#333333", font='Arial,12')
    select_label.grid(row=1, column=0, columnspan=2, pady=(0, 5))

    # Listbox to display patients
    patients_listbox = Listbox(discharge_frame, bg="#ffffff", fg="#333333", font='Arial,12', selectmode=SINGLE, height=5, width=50)
    patients_listbox.grid(row=2, column=0, columnspan=2, pady=(0, 5))

    display_patients()

    def discharge_selected_patient():
        selected_index = patients_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            confirm = messagebox.askyesno("Confirm Discharge", "Are you sure you want to discharge this patient?")
            if confirm:
                discharge_patients =  patients.pop(index)
                discharged_patients.append(discharge_patients)
                messagebox.showinfo("Success", "Patient discharged successfully!")
                display_patients()
        else:
            messagebox.showerror("Error", "Please select a patient to discharge.")

    discharge_button = Button(discharge_frame, text="Discharge", bg='#ff3399', fg='#fff', padx=10, pady=0, font='Arial,12', command=discharge_selected_patient)
    discharge_button.grid(row=3, column=0, columnspan=2, pady=10)




# Function to view discharged patients
def view_discharge():
    view_discharge_window = Toplevel()
    view_discharge_window.title("View Discharged Patients")
    view_discharge_window.geometry('400x300')
    view_discharge_window.configure(bg='#333333')

    view_discharge_frame = Frame(view_discharge_window, bg='#333333')
    view_discharge_frame.pack(expand=True)

    title_label = Label(view_discharge_frame, text="Discharged Patients", fg="#ffffff", bg="#333333", font='Arial,16')
    title_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

    print(discharged_patients)

    # Function to display the list of discharged patients
    def display_discharged_patients():
        discharged_patients_listbox.delete(0, END)
        for i, patient in enumerate(discharged_patients, 1):
            discharged_patients_listbox.insert(END, f"{i}. {patient.get_full_name()}")

    select_label = Label(view_discharge_frame, text="Discharged Patients:", fg="#ffffff", bg="#333333", font='Arial,12')
    select_label.grid(row=1, column=0, columnspan=2, pady=(0, 5))

    # Listbox to display discharged patients
    discharged_patients_listbox = Listbox(view_discharge_frame, bg="#ffffff", fg="#333333", font='Arial,12', selectmode=SINGLE, height=5, width=50)
    discharged_patients_listbox.grid(row=2, column=0, columnspan=2, pady=(0, 5))

    display_discharged_patients()



def assign_doctor_to_patient():
    # Create a new window for assigning doctors to patients
    assign_window = Toplevel()
    assign_window.title("Assign Doctor to Patient")
    
    # Create a frame to hold the assignment widgets
    assign_frame = Frame(assign_window)
    assign_frame.pack()

    # Create labels and dropdown menus for selecting patient and doctor
    Label(assign_frame, text="Select Patient:", font=("Arial", 12, "bold")).grid(row=0, column=0, padx=10, pady=5)
    patient_var = StringVar()
    patient_dropdown = OptionMenu(assign_frame, patient_var, *[patient.get_full_name() for patient in patients])
    patient_dropdown.grid(row=0, column=1, padx=10, pady=5)

    Label(assign_frame, text="Select Doctor:", font=("Arial", 12, "bold")).grid(row=1, column=0, padx=10, pady=5)
    doctor_var = StringVar()
    doctor_dropdown = OptionMenu(assign_frame, doctor_var, *[doctor.get_full_name() for doctor in doctors])
    doctor_dropdown.grid(row=1, column=1, padx=10, pady=5)

    # Function to handle assignment
    def assign_doctor():
        selected_patient_name = patient_var.get()
        selected_doctor_name = doctor_var.get()
        selected_patient = next((patient for patient in patients if patient.get_full_name() == selected_patient_name), None)
        selected_doctor = next((doctor for doctor in doctors if doctor.get_full_name() == selected_doctor_name), None)
        if selected_patient and selected_doctor:
            selected_patient.link(selected_doctor.get_full_name())
            messagebox.showinfo("Success", f"Doctor {selected_doctor.get_full_name()} assigned to patient {selected_patient.get_full_name()}")
            assign_window.destroy()
        else:
            messagebox.showerror("Error", "Please select both patient and doctor")

    # Create a button to perform the assignment
    assign_button = Button(assign_frame, text="Assign Doctor", font=("Arial", 12), command=assign_doctor)
    assign_button.grid(row=2, columnspan=2, padx=10, pady=10)






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



def relocate_doctors():
    # Create a new window for relocating doctors
    relocate_window = Toplevel()
    relocate_window.title("Relocate Doctors")

    # Create a frame to hold the relocation widgets
    relocate_frame = Frame(relocate_window)
    relocate_frame.pack()

    # Create a label and dropdown menu for selecting a patient
    Label(relocate_frame, text="Select Patient:", font=("Arial", 12, "bold")).grid(row=0, column=0, padx=10, pady=5)
    patient_var = StringVar()
    patient_dropdown = OptionMenu(relocate_frame, patient_var, *[patient.get_full_name() for patient in patients])
    patient_dropdown.grid(row=0, column=1, padx=10, pady=5)

    # Function to handle patient selection
    def select_patient():
        selected_patient_name = patient_var.get()
        selected_patient = next((patient for patient in patients if patient.get_full_name() == selected_patient_name), None)
        if selected_patient:
            assign_new_doctor(selected_patient)
        else:
            messagebox.showerror("Error", "Please select a patient")

    # Create a button to proceed after selecting a patient
    select_button = Button(relocate_frame, text="Select Patient", font=("Arial", 12), command=select_patient)
    select_button.grid(row=1, columnspan=2, padx=10, pady=10)

    # Function to assign a new doctor to the selected patient
    def assign_new_doctor(patient):
        # Clear the frame for selecting a patient
        relocate_frame.destroy()

        # Create a new frame for selecting a new doctor
        assign_frame = Frame(relocate_window)
        assign_frame.pack()

        # Create labels and dropdown menus for selecting a new doctor
        Label(assign_frame, text=f"Assign new doctor for {patient.get_full_name()}:", font=("Arial", 12, "bold")).grid(row=0, column=0, padx=10, pady=5)
        new_doctor_var = StringVar()
        new_doctor_dropdown = OptionMenu(assign_frame, new_doctor_var, *[doctor.get_full_name() for doctor in doctors])
        new_doctor_dropdown.grid(row=0, column=1, padx=10, pady=5)

        # Function to handle assigning a new doctor
        def assign_new_doctor_to_patient():
            new_doctor_name = new_doctor_var.get()
            new_doctor = next((doctor for doctor in doctors if doctor.get_full_name() == new_doctor_name), None)
            if new_doctor:
                patient.link(new_doctor.get_full_name())
                messagebox.showinfo("Success", f"New doctor {new_doctor.get_full_name()} assigned to patient {patient.get_full_name()}")
                relocate_window.destroy()
            else:
                messagebox.showerror("Error", "Please select a new doctor")

        # Create a button to assign a new doctor
        assign_button = Button(assign_frame, text="Assign Doctor", font=("Arial", 12), command=assign_new_doctor_to_patient)
        assign_button.grid(row=1, columnspan=2, padx=10, pady=10)





from tkinter import *
from tkinter import ttk

from tkinter import *
from tkinter import ttk

def toggle_section(event):
    # Get the section frame associated with the clicked label
    section_frame = event.widget.master

    # Toggle the visibility of the section
    if section_frame.cget("height") == 0:
        # Expand the section
        section_frame.config(height=section_frame.winfo_reqheight())
    else:
        # Collapse the section
        section_frame.config(height=0)

def management_report():
    # Create a new window for the management report
    report_window = Toplevel()
    report_window.title("Management Report")

    # Create a canvas with scrollbar
    canvas = Canvas(report_window)
    scrollbar = Scrollbar(report_window, orient="vertical", command=canvas.yview)
    scrollable_frame = Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Define the sections
    sections = [
        ("Doctors Info", doctors_info, plot_doctors_info),
        ("Patients per Doctor", patients_per_doctor, plot_patients_per_doctor),
        ("Monthly Appointments per Doctor", monthly_appointments, plot_monthly_appointments),
        ("Illness Type", illness_type, plot_illness_type)
        # Add more sections as needed
    ]

    # Create and pack the sections
    for i, (section_title, section_data, plot_function) in enumerate(sections):
        # Create a frame for the section
        section_frame = Frame(scrollable_frame, bd=1, relief="solid")
        section_frame.pack(fill="x", padx=10, pady=(10, 5))

        # Create a label for the section title
        section_label = Label(section_frame, text=section_title, font=("Arial", 12, "bold"), anchor="w", cursor="hand2")
        section_label.pack(fill="x")
        section_label.bind("<Button-1>", toggle_section)

        # Create a frame for the section data (hidden by default)
        data_frame = Frame(section_frame)
        data_frame.pack(fill="both", padx=10, pady=(0, 10), expand=True)

        # Add the section data to the data frame
        section_data(data_frame)

        # Plot diagram if plot function is provided
        if plot_function:
            plot_frame = Frame(scrollable_frame)
            plot_frame.pack(fill="both", padx=10, pady=(0, 10), expand=True)
            plot_function(plot_frame)

def plot_doctors_info(frame):
    # Plot total number of doctors
    fig, ax = plt.subplots()
    ax.bar(["Total No. of Doctors"], [len(doctors)])
    ax.set_ylabel('Number of Doctors')
    ax.set_title('Doctors Info')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)

def plot_patients_per_doctor(frame):
    # Plot patients per doctor
    fig, ax = plt.subplots()
    doctor_names = [f"Dr. {doctor.get_full_name()}" for doctor in doctors]
    patient_counts = [len(doctor.get_patients()) for doctor in doctors]
    ax.bar(doctor_names, patient_counts)
    ax.set_xlabel('Doctors')
    ax.set_ylabel('Number of Patients')
    ax.set_title('Patients per Doctor')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)


def plot_monthly_appointments(frame):
    # Plot monthly appointments per doctor
    fig, ax = plt.subplots()
    doctor_names = [f"Dr. {doctor.get_full_name()}" for doctor in doctors]
    appointment_counts = [len(doctor.get_monthly_appointment()) for doctor in doctors]
    ax.bar(doctor_names, appointment_counts)
    ax.set_xlabel('Doctors')
    ax.set_ylabel('Number of Appointments')
    ax.set_title('Monthly Appointments per Doctor')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)

def plot_illness_type(frame):
    # Plot illness types and patient count
    patients_per_illness = admin.sort_ilness(patients)
    fig, ax = plt.subplots()
    symptoms = list(patients_per_illness.keys())
    patient_numbers = list(patients_per_illness.values())
    ax.bar(symptoms, patient_numbers)
    ax.set_xlabel('Illness Type')
    ax.set_ylabel('Number of Patients')
    ax.set_title('Illness Type')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)

def doctors_info(frame):
    # Display total number of doctors
    total_doctors_label = Label(frame, text=f"Total No. of Doctors: {len(doctors)}", font=("Arial", 10))
    total_doctors_label.pack(anchor="w")

    # Display list of doctors
    for doctor in doctors:
        doctor_label = Label(frame, text=f"{doctor.get_full_name()} - {doctor.get_speciality()}", font=("Arial", 10), anchor="w")
        doctor_label.pack(anchor="w")

def patients_per_doctor(frame):
    # Display patients per doctor
    for doctor in doctors:
        patients_list = doctor.get_patients()
        label = Label(frame, text=f"Dr. {doctor.get_full_name()}: {len(patients_list)} patients", font=("Arial", 10), anchor="w")
        label.pack(anchor="w")
        if patients_list:
            patients_label = Label(frame, text=", ".join(patient.get_full_name() for patient in patients_list), font=("Arial", 9), anchor="w")
            patients_label.pack(anchor="w", padx=20)

def monthly_appointments(frame):
    # Display monthly appointments per doctor
    for doctor in doctors:
        monthly_appointments = doctor.get_monthly_appointment().items()
        label = Label(frame, text=f"Dr. {doctor.get_full_name()}", font=("Arial", 10), anchor="w")
        label.pack(anchor="w")
        if not monthly_appointments:
            no_appointments_label = Label(frame, text="No appointments for any month", font=("Arial", 9), anchor="w", padx=20)
            no_appointments_label.pack(anchor="w")
        else:
            for month, appointments in monthly_appointments:
                appointments_label = Label(frame, text=f"{month}: {len(appointments)} appointments", font=("Arial", 9), anchor="w", padx=20)
                appointments_label.pack(anchor="w")


def illness_type(frame):
    # Display illness types and patient count
    patients_per_illness = admin.sort_ilness(patients)
    for symptom, patient_no in patients_per_illness.items():
        label = Label(frame, text=f"{symptom}: {patient_no} patients", font=("Arial", 10), anchor="w")
        label.pack(anchor="w")



# Call the management report function



# Example usage:
# management_report(doctors, patients)


# Example usage:
# management_report(doctors, patients)


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
