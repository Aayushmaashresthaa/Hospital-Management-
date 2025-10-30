from Doctor import Doctor
from Patient import Patient 

class Admin:
    """A class that deals with the Admin operations"""
    
    def __init__(self, username, password, address=''):
        """
        Args:
            username (string): Username
            password (string): Password
            address (string, optional): Address Defaults to ''
        """
        self.__username = username
        self.__password = password
        self.address = address

    def view(self, a_list):
        """
        Print a list
        Args:
            a_list (list): a list of printables
        """
        for index, item in enumerate(a_list):
            print(f'{index+1:3}|{item}')

    def login(self):
        """
        A method that deals with the login
        Raises:
            Exception: Raised when the username and the password don't match the data registered
        Returns:
            bool: True if login is successful, else False
        """
        print("-----Login-----")
        # details of the admin
        username = input('Enter the username: ')
        password = input('Enter the password: ')

        # username and password match the registered ones
        return True if self.__username == username and self.__password == password else False 

    def find_index(self, index, doctors):
        """
        Check if the doctor index exists
        Args:
            index (int): The index to search for
            doctors (list): The list of doctors
        Returns:
            bool: True if index exists, False otherwise
        """
        if index in range(len(doctors)):
            return True
        return False

    def get_doctor_details(self):
        """
        Get the details needed to add a doctor
        Returns:
            first name, surname, and the speciality of the doctor in that order.
        """
        first_name = input('Enter the first name of the doctor: ')
        last_name = input('Enter the surname of the doctor: ')
        speciality = input("Enter the doctor's speciality: ")
        return first_name, last_name, speciality

    def doctor_management(self, doctors):
        """
        A method that deals with registering, viewing, updating, deleting doctors
        Args:
            doctors (list<Doctor>): the list of all the doctors
        """
        print("-----Doctor Management-----")

        # Menu
        print('Choose the operation:')
        print(' 1 - Register')
        print(' 2 - View')
        print(' 3 - Update')
        print(' 4 - Delete')

        op = input('Enter your choice: ')

        # Register
        if op == '1':
            print("-----Register-----")
            # Get the doctor details
            print('Enter the doctor\'s details:')
            first_name, last_name, speciality = self.get_doctor_details()

            # Check if the name is already registered
            name_exists = False
            for doctor in doctors:
                if first_name == doctor.get_first_name() and last_name == doctor.get_surname():
                    print('Doctor already exists.')
                    name_exists = True
                    break  

            if not name_exists:
                new_doctor = Doctor(first_name, last_name, speciality)
                doctors.append(new_doctor)
                print('Doctor registered successfully.')

        # View
        elif op == '2':
            print("-----List of Doctors-----")
            
            for doctor in doctors:
                print(doctor)
                # 

        # Update
        elif op == '3':
            while True:
                print("-----Update Doctor's Details-----")
                print('ID |  Full Name  | Speciality')
                self.view(doctors)
                try:
                    index = int(input('Enter the ID of the doctor: ')) - 1
                    doctor_index = self.find_index(index, doctors)
                    if doctor_index:
                        break
                    else:
                        print("Doctor not found")
                except ValueError:
                    print('The ID entered is incorrect')

            # Menu to update 
            print('Choose the field to be updated:')
            print(' 1 First name')
            print(' 2 Surname')
            print(' 3 Speciality')
            op = int(input('Input: '))

            if op == 1:
                new_first_name = input('Enter new first name: ')
                doctors[index].set_first_name(new_first_name)
            elif op == 2:
                new_last_name = input('Enter the new last name: ')
                doctors[index].set_last_name(new_last_name)
            elif op == 3:
                new_speciality = input('Enter the new speciality: ')
                doctors[index].set_speciality(new_speciality)

        # Delete
        elif op == '4':
            print("-----Delete Doctor-----")
            print('ID |  Full Name  | Speciality')
            self.view(doctors)

            try:
                doctor_index = int(input('Enter the ID of the doctor to be deleted: ')) - 1
                if self.find_index(doctor_index, doctors):
                    doctors.pop(doctor_index)
                    print('Doctor deleted successfully.')
                else:
                    print('Doctor not found.')
            except ValueError:
                print('The ID entered is incorrect')

        else:
            print('Invalid operation chosen. Check your spelling!')

    def view_patient(self, patients):
        """
        Print a list of patients
        Args:
            patients (list<Patients>): list of all the active patients
        """
        print("-----View Patients-----")
        print('ID | Full Name | Doctor | Age |     Mobile    | Postcode ')
        self.view(patients)

    def assign_doctor_to_patient(self, patients, doctors):
        """
        Allow the admin to assign a doctor to a patient
    
        """
        print("-----Assign-----")
        print("-----Patients-----")
        print('ID | Full Name | Doctor | Age |     Mobile    | Postcode ')
        self.view(patients)

        try:
            patient_index = int(input('Please enter the patient ID: ')) - 1
            if patient_index not in range(len(patients)):
                print('The ID entered was not found.')
                return

            print("-----Doctors Select-----")
            print('Select the doctor that fits these symptoms:')
            patients[patient_index].print_symptoms()
            print('ID |  Full Name  | Speciality')
            self.view(doctors)

            doctor_index = int(input('Please enter the doctor ID: ')) - 1
            if self.find_index(doctor_index, doctors):
                # Link patient to doctor and vice versa
                patients[patient_index].link(doctors[doctor_index].full_name())
                # doctors[doctor_index].add_patient(patients[patient_index], patients[patient_index].full_name())
                doctors[doctor_index].add_patient(patients[patient_index])
                print('The patient is now assigned to the doctor.')
            else:
                print('The ID entered was not found.')
        except ValueError:
            print('The ID entered is incorrect')

    def discharge(self, patients, discharge_patients):
        """
        Allow the admin to discharge a patient when treatment is done
       
           
        """
        print("-----Discharge Patient-----")
        try:
            patient_index = int(input('Please enter the patient ID: ')) - 1
            if patient_index in range(len(patients)):
                discharge_patients.append(patients.pop(patient_index))
                print('The patient was discharged successfully.')
            else:
                print('The ID entered was not found.')
        except ValueError:
            print('The ID entered is incorrect')

    def view_discharge(self, discharged_patients):
        """
        Prints the list of all discharged patients
     
        """
        print("-----Discharged Patients-----")
        print('ID | Full Name | Doctor | Age |     Mobile    | Postcode ')
        self.view(discharged_patients)

    def update_details(self):
        """
        Allows the user to update and change username, password, and address
        """
        print('Choose the field to be updated:')
        print(' 1 Username')
        print(' 2 Password')
        print(' 3 Address')
        op = int(input('Input: '))

        if op == 1:
            new_username = input('Enter your new username: ')
            self.__username = new_username
            print(f'Your username has been updated to: {self.__username}')
        elif op == 2:
            password = input('Enter the new password: ')
            if password == input('Enter the new password again: '):
                self.__password = password
                print('Your password has been updated successfully.')
        elif op == 3:
            new_address = input('Enter your new address: ')
            self.address = new_address
            print(f'Your address has been updated to: {self.address}')
        else:
            print('Invalid option. Please choose 1, 2, or 3.')
            