import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
from Admin import Admin

class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("800x400")  # Setting window dimensions
        self.create_widgets()

    def create_widgets(self):
        # Left side - Logo and headline
        left_frame = tk.Frame(self.root, bg="#cfe2f3", width=300)  # Adjusted width
        left_frame.pack(side="left", fill="both", expand=True)

        # Hospital Management System logo
        logo_img = ImageTk.PhotoImage(Image.open("hospital_logo.jpg"))  # Path to your logo image
        logo_label = tk.Label(left_frame, image=logo_img, bg="#cfe2f3")
        logo_label.image = logo_img  # Keep a reference to the image to prevent garbage collection
        logo_label.pack(pady=20)

        # Headline
        headline_label = tk.Label(left_frame, text="Hospital Management System", font=("Arial", 20), bg="#cfe2f3")
        headline_label.pack(pady=20)

        # Right side - Login window
        right_frame = tk.Frame(self.root)
        right_frame.pack(side="right", fill="both", expand=True)

        # Welcome message
        welcome_label = tk.Label(right_frame, text="Welcome to Admin", font=("Arial", 16))
        welcome_label.pack(pady=20)

        # Username label and entry
        username_frame = tk.Frame(right_frame)
        username_frame.pack(pady=10)
        username_label = tk.Label(username_frame, text="Username:", font=("Arial", 12))
        username_label.pack(side="left", padx=5)
        self.entry_username = tk.Entry(username_frame, font=("Arial", 12))
        self.entry_username.pack(side="right", padx=5)

        # Password label and entry
        password_frame = tk.Frame(right_frame)
        password_frame.pack(pady=10)
        password_label = tk.Label(password_frame, text="Password:", font=("Arial", 12))
        password_label.pack(side="left", padx=5)
        self.entry_password = tk.Entry(password_frame, show="*", font=("Arial", 12))
        self.entry_password.pack(side="right", padx=5)

        # Login button
        login_button = tk.Button(right_frame, text="Login", font=("Arial", 12), command=self.login)
        login_button.pack(pady=10)

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        # Attempt login
        if username == "admin" and password == "123":
            self.root.destroy()  # Close the login window
            main_window = tk.Tk()
            main_window.title("Hospital Management System")
            app = HospitalManagementApp(main_window)
            main_window.mainloop()
        else:
            messagebox.showerror("Login Failed", "Incorrect username or password")

class HospitalManagementApp:
    def __init__(self, root):
        self.root = root
        self.admin = Admin('admin', '123', 'B1 1AB')
        self.root.geometry("800x400")  # Setting window dimensions
        self.create_widgets()

    def create_widgets(self):
        # Create a frame for the menu buttons
        menu_frame = tk.Frame(self.root)
        menu_frame.pack(expand=True)

        # Create buttons for each operation
        operations = [
            ("Register/view/update/delete doctor", self.admin.doctor_management),
            ("Book appointments/View appointments", self.admin.appointments_management),
            ("View/add patient/patient's family", self.admin.patient_management),
            ("Discharge patients", self.admin.discharge),
            ("View discharged patient", self.admin.view_discharge),
            ("Assign doctor to a patient", self.admin.assign_doctor_to_patient),
            ("Update admin details", self.admin.update_details),
            ("Store patient details", self.admin.add_patient_data),
            ("Relocate the patient", self.admin.relocate_doctors),
            ("Show management report", self.admin.management_report),
        ]

        # Calculate number of rows and columns
        num_rows = (len(operations) + 1) // 2  # Add 1 for the Quit button
        num_columns = 2

        # Create buttons
        for i, (text, command) in enumerate(operations):
            button = tk.Button(menu_frame, text=text, font=("Arial", 12), command=command, bg="#2E8BC0", fg="white", bd=0, padx=10, pady=5, relief=tk.RIDGE, borderwidth=3, width=30)

            row = i // num_columns
            column = i % num_columns
            button.grid(row=row, column=column, padx=5, pady=5)

        # Quit button
        quit_button = tk.Button(menu_frame, text="Quit", font=("Arial", 12), command=self.quit_application, bg="#2E8BC0", fg="white", bd=0, padx=10, pady=5, relief=tk.RIDGE, borderwidth=3, width=60)
        quit_button.grid(row=num_rows, columnspan=num_columns, padx=5, pady=5)

    def quit_application(self):
        self.root.destroy()

def main():
    login_window = tk.Tk()
    app = LoginWindow(login_window)
    login_window.mainloop()

if __name__ == "__main__":
    main()
