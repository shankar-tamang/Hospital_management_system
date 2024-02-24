from tkinter import messagebox, Tk, Frame, Button, Label, Entry, Toplevel
import os

class Main:
    def __init__(self):
        self.root = Tk()
        self.root.title("Login form")
        self.root.geometry("340x440")
        self.root.configure(bg="black")

        self.frame = Frame(self.root, bg="black")

        # Getting the root directory
        self.root_dir = os.path.dirname(__file__)

        with open(os.path.join(self.root_dir, 'admin.txt'), 'r') as file:
            line = file.readline()
            line_list = line.split(',')
            self.admin_username = line_list[0]
            self.admin_password = line_list[1]
            self.admin_address = line_list[2]

        self.admin = Admin(self.admin_username, self.admin_password, self.admin_address)

        # Define username_entry and password_entry as instance variables
        self.username_entry = None
        self.password_entry = None

        self.start()

    def start(self):
        login_label = Label(self.frame, text="Admin  Login", bg="black", fg="#FF3399", font=("Arial", 30))
        username_label = Label(self.frame, text="Username", bg="black", fg="white", font=("Arial", 16))
        self.username_entry = Entry(self.frame)
        password_label = Label(self.frame, text="Password", bg="black", fg="white", font=("Arial", 16))
        self.password_entry = Entry(self.frame, show="*")
        login_button = Button(self.frame, text="Login", bg="#FF3399", fg="white", font=("Arial", 16), command=self.login)

        login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
        username_label.grid(row=1, column=0)
        self.username_entry.grid(row=1, column=1, pady=20)
        password_label.grid(row=2, column=0)
        self.password_entry.grid(row=2, column=1, pady=20)
        login_button.grid(row=3, column=0, columnspan=2, pady=30)

        self.frame.pack()

    def login(self):
        username = self.admin.get_username()
        password = self.admin.get_password()
        if self.username_entry.get() == username and self.password_entry.get() == password:
            messagebox.showinfo(title="Login Success", message="You are successfully logged in.")
            self.root.withdraw()
            self.main_operation()
        else:
            messagebox.showinfo(title="Error", message="Invalid login.")

    def main_operation(self):
        main_window = Toplevel(self.root)
        main_window.title("Main Operations")
        menu_frame = Frame(main_window)
        menu_frame.pack(expand=True)

        operations = [
            ("Register/view/update/delete doctor", self.doctor_management),
            ("Book appointments/View appointments", self.appointments_management),
            ("View/add patient/patient's family", self.patient_management),
            ("Discharge patients", self.discharge),
            ("View discharged patient", self.view_discharge),
            ("Assign doctor to a patient", self.assign_doctor_to_patient),
            ("Update admin details", self.update_details),
            ("Store patient details", self.add_patient_data),
            ("Relocate the patient", self.relocate_doctors),
            ("Show management report", self.management_report),
        ]

        num_rows = (len(operations) + 1) // 2
        num_columns = 2

        for i, (text, command) in enumerate(operations):
            button = Button(
                menu_frame, text=text, font=("Arial", 12), command=command,
                bg="#2E8BC0", fg="white", bd=0, padx=10, pady=5,
                relief="ridge", borderwidth=3, width=30
            )

            row = i // num_columns
            column = i % num_columns
            button.grid(row=row, column=column, padx=5, pady=5)

        quit_button = Button(
                menu_frame, text="Quit", font=("Arial", 12),
                command=self.root.destroy, bg="#2E8BC0", fg="white",
                bd=0, padx=10, pady=5, relief="ridge", borderwidth=3, width=60
            )
        quit_button.grid(row=num_rows, columnspan=num_columns, padx=5, pady=5)

        main_window.mainloop()

    def doctor_management(self):
        pass

    def appointments_management(self):
        pass

    def patient_management(self):
        pass

    def discharge(self):
        pass

    def view_discharge(self):
        pass

    def assign_doctor_to_patient(self):
        pass

    def update_details(self):
        pass

    def add_patient_data(self):
        pass

    def relocate_doctors(self):
        pass

    def management_report(self):
        pass

class Admin:
    def __init__(self, username, password, address):
        self.username = username
        self.password = password
        self.address = address

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

if __name__ == "__main__":
    app = Main()
