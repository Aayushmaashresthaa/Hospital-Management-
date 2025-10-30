import tkinter as tk
from tkinter import messagebox
from Admin import Admin
from Doctor import Doctor
from Patient import Patient

class HospitalManagementGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("400x300")
        self.admin = Admin("admin", "123", "B1 1AB")
        self.doctors = [
            Doctor("John", "Smith", "Internal Med."),
            Doctor("Jone", "Smith", "Pediatrics"),
            Doctor("Jone", "Carlos", "Cardiology")
        ]
        self.patients = [
            Patient("Sara", "Smith", 20, "07012345678", "B1 234", "Fever"),
            Patient("Mike", "Jones", 37, "07555551234", "L2 2AB", "Headache"),
            Patient("David", "Smith", 15, "07123456789", "C1 ABC", "Cough")
        ]
        self.discharged_patients = []
        self.login_screen()
    
    def login_screen(self):
        self.clear_screen()
        tk.Label(self.root, text="Login", font=("Arial", 16)).pack(pady=10)
        tk.Label(self.root, text="Username:").pack()
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack(pady=5)
        tk.Label(self.root, text="Password:").pack()
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack(pady=5)
        tk.Button(self.root, text="Login", command=self.check_credentials).pack(pady=10)
    
    def check_credentials(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if username == "admin" and password == "123":
            messagebox.showinfo("Login Successful", "Welcome to the Hospital Management System.")
            self.main_menu()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")
    
    def main_menu(self):
        self.clear_screen()
        tk.Label(self.root, text="Main Menu", font=("Arial", 16)).pack(pady=10)
        tk.Button(self.root, text="Manage Doctors", command=self.manage_doctors).pack(pady=5)
        tk.Button(self.root, text="View Patients", command=self.view_patients).pack(pady=5)
        tk.Button(self.root, text="Assign Doctor to Patient", command=self.assign_doctor).pack(pady=5)
        tk.Button(self.root, text="Discharge Patient", command=self.discharge_patient).pack(pady=5)
        tk.Button(self.root, text="View Discharged Patients", command=self.view_discharged_patients).pack(pady=5)  # NEW FEATURE
        tk.Button(self.root, text="Logout", command=self.login_screen).pack(pady=10)
    
    def manage_doctors(self):
        self.clear_screen()
        tk.Label(self.root, text="Doctors", font=("Arial", 14)).pack(pady=10)
        for doctor in self.doctors:
            tk.Label(self.root, text=str(doctor)).pack()
        tk.Button(self.root, text="Register Doctor", command=self.register_doctor).pack(pady=5)
        tk.Button(self.root, text="Delete Doctor", command=self.delete_doctor).pack(pady=5)
        tk.Button(self.root, text="Update Doctor", command=self.update_doctor).pack(pady=5)
        tk.Button(self.root, text="Back", command=self.main_menu).pack(pady=10)
    
    def register_doctor(self):
        self.clear_screen()
        tk.Label(self.root, text="Register Doctor", font=("Arial", 14)).pack(pady=10)
        tk.Label(self.root, text="First Name:").pack()
        self.first_name_entry = tk.Entry(self.root)
        self.first_name_entry.pack(pady=5)
        tk.Label(self.root, text="Surname:").pack()
        self.surname_entry = tk.Entry(self.root)
        self.surname_entry.pack(pady=5)
        tk.Label(self.root, text="Specialization:").pack()
        self.specialization_entry = tk.Entry(self.root)
        self.specialization_entry.pack(pady=5)
        tk.Button(self.root, text="Register", command=self.process_doctor_registration).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.manage_doctors).pack(pady=5)
    
    def process_doctor_registration(self):
        first_name = self.first_name_entry.get()
        surname = self.surname_entry.get()
        specialization = self.specialization_entry.get()
        if first_name and surname and specialization:
            new_doctor = Doctor(first_name, surname, specialization)
            self.doctors.append(new_doctor)
            messagebox.showinfo("Success", f"Doctor {first_name} {surname} registered successfully!")
            self.manage_doctors()
        else:
            messagebox.showerror("Error", "All fields are required!")

    def delete_doctor(self):
        self.clear_screen()
        tk.Label(self.root, text="Delete Doctor", font=("Arial", 14)).pack(pady=10)
        if not self.doctors:
            tk.Label(self.root, text="No doctors available.").pack()
        else:
            self.selected_doctor = tk.StringVar()
            tk.Label(self.root, text="Select Doctor: ").pack()
            self.doctor_dropdown = tk.OptionMenu(self.root, self.selected_doctor, *[d.full_name() for d in self.doctors])
            self.doctor_dropdown.pack()
            tk.Button(self.root, text="Delete", command=self.process_delete_doctor).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.manage_doctors).pack(pady=10)
    
    def process_delete_doctor(self):
        doctor_name = self.selected_doctor.get()
        if doctor_name:
            for doctor in self.doctors:
                if doctor.full_name() == doctor_name:
                    self.doctors.remove(doctor)
                    messagebox.showinfo("Success", f"Doctor {doctor_name} deleted successfully!")
                    self.manage_doctors()
                    return
        messagebox.showerror("Error", "You haven't chose any doctor to delete.")

    def update_doctor(self):
        self.clear_screen()
        tk.Label(self.root, text="Update Doctor", font=("Arial", 14)).pack(pady=10)
        if not self.doctors:
            tk.Label(self.root, text="No doctors available.").pack()
        else:
            self.selected_doctor = tk.StringVar()
            tk.Label(self.root, text="Select Doctor:").pack()
            self.doctor_dropdown = tk.OptionMenu(self.root, self.selected_doctor, *[d.full_name() for d in self.doctors])
            self.doctor_dropdown.pack()
            
            self.update_choice = tk.StringVar()
            tk.Label(self.root, text="Select Detail to Update:").pack()
            options = ["First Name", "Last Name", "Specialization"]
            self.update_dropdown = tk.OptionMenu(self.root, self.update_choice, *options)
            self.update_dropdown.pack()
            
            tk.Label(self.root, text="New Value:").pack()
            self.new_value_entry = tk.Entry(self.root)
            self.new_value_entry.pack(pady=5)
            
            tk.Button(self.root, text="Update", command=self.process_doctor_update).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.manage_doctors).pack(pady=10)

    def process_doctor_update(self):
        doctor_name = self.selected_doctor.get()
        update_choice = self.update_choice.get()
        new_value = self.new_value_entry.get()
        
        if doctor_name and update_choice and new_value:
            for doctor in self.doctors:
                if doctor.full_name() == doctor_name:
                    if update_choice == "First Name":
                        doctor.first_name = new_value
                    elif update_choice == "Last Name":
                        doctor.surname = new_value
                    elif update_choice == "Specialization":
                        doctor.specialization = new_value
                    
                    messagebox.showinfo("Success", f"Doctor {doctor_name} updated successfully!")
                    self.manage_doctors()
                    return
        messagebox.showerror("Error", "Doctor update failed.")



    def view_patients(self):
        self.clear_screen()
        tk.Label(self.root, text="Patients", font=("Arial", 14)).pack(pady=10)
        for patient in self.patients:
            tk.Label(self.root, text=str(patient)).pack()
        tk.Button(self.root, text="Back", command=self.main_menu).pack(pady=10)
    
    def assign_doctor(self):
        self.clear_screen()
        tk.Label(self.root, text="Assign Doctor", font=("Arial", 14)).pack(pady=10)
        if not self.patients or not self.doctors:
            tk.Label(self.root, text="No available patients or doctors.").pack()
        else:
            self.selected_patient = tk.StringVar()
            self.selected_doctor = tk.StringVar()
            tk.Label(self.root, text="Select Patient:").pack()
            self.patient_dropdown = tk.OptionMenu(self.root, self.selected_patient, *[p.full_name() for p in self.patients])
            self.patient_dropdown.pack()
            tk.Label(self.root, text="Select Doctor:").pack()
            self.doctor_dropdown = tk.OptionMenu(self.root, self.selected_doctor, *[d.full_name() for d in self.doctors])
            self.doctor_dropdown.pack()
            tk.Button(self.root, text="Assign", command=self.process_assignment).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.main_menu).pack(pady=10)
    
    def process_assignment(self):
        patient_name = self.selected_patient.get()
        doctor_name = self.selected_doctor.get()
        if patient_name and doctor_name:
            for patient in self.patients:
                if patient.full_name() == patient_name:
                    patient.link(doctor_name)
                    messagebox.showinfo("Success", f"{patient_name} is assigned to {doctor_name}.")
                    self.main_menu()
                    return
        messagebox.showerror("Error", "Assignment failed.")
    
    def discharge_patient(self):
        self.clear_screen()
        tk.Label(self.root, text="Discharge Patient", font=("Arial", 14)).pack(pady=10)
        if not self.patients:
            tk.Label(self.root, text="No active patients to discharge.").pack()
        else:
            self.selected_discharge = tk.StringVar()
            tk.Label(self.root, text="Select Patient:").pack()
            self.discharge_dropdown = tk.OptionMenu(self.root, self.selected_discharge, *[p.full_name() for p in self.patients])
            self.discharge_dropdown.pack()
            tk.Button(self.root, text="Discharge", command=self.process_discharge).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.main_menu).pack(pady=10)
    
    def process_discharge(self):
        patient_name = self.selected_discharge.get()
        if patient_name:
            for patient in self.patients:
                if patient.full_name() == patient_name:
                    self.patients.remove(patient)
                    self.discharged_patients.append(patient)
                    messagebox.showinfo("Success", f"{patient_name} has been discharged.")
                    self.main_menu()
                    return
        messagebox.showerror("Error", "Discharge failed.")
    
    def view_discharged_patients(self): 
        self.clear_screen()
        tk.Label(self.root, text="Discharged Patients", font=("Arial", 14)).pack(pady=10)
        if not self.discharged_patients:
            tk.Label(self.root, text="No discharged patients.").pack()
        else:
            for patient in self.discharged_patients:
                tk.Label(self.root, text=str(patient)).pack()
        tk.Button(self.root, text="Back", command=self.main_menu).pack(pady=10)

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = HospitalManagementGUI(root)
    root.mainloop()

