from Admin import Admin
from Doctor import Doctor
from Patient import Patient

def main():
    """
    the main function to be ran when the program runs
    """

    admin = Admin('admin','123','B1 1AB') # username is 'admin', password is '123'
    doctors = [Doctor('John','Smith','Internal Med.'), Doctor('Jone','Smith','Pediatrics'), Doctor('Jone','Carlos','Cardiology')]
    patients = [Patient('Sara','Smith', 20, '07012345678','B1 234', 'Fever'), Patient('Mike','Jones', 37,'07555551234','L2 2AB', 'Headache'), Patient('David','Smith', 15, '07123456789','C1 ABC', 'Cough')]
    discharged_patients = []

    # keep trying to login tell the login details are correct
    while True:
        if admin.login():
            running = True 
            break
        else:
            print('Incorrect username or password.')

    while running:
        
        print('Choose the operation:')
        print(' 1- Register/view/update/delete doctor')
        print(' 2- Discharge patients')
        print(' 3- View discharged patient')
        print(' 4- Assign doctor to a patient')
        print(' 5- Update admin details')
        print(' 6- Quit')

        
        op = input('Option: ')

        if op == '1':
            # 1- Register/view/update/delete doctor
            #ToDo1
            admin.doctor_management(doctors)

        elif op == '2':
            # 2- View or discharge patients
            #ToDo2
            admin.view_patient(patients)

            while True:
                op = input('Do you want to discharge a patient(Y/N):').lower()

                if op == 'yes' or op == 'y':
                    #ToDo3
                    admin.discharge(patients, discharged_patients)

                elif op == 'no' or op == 'n':
                    break

                # unexpected entry
                else:
                    print('Please answer by yes or no.')
        
        elif op == '3':
            # 3 - view discharged patients
            #ToDo4
            admin.view_discharge(discharged_patients)

        elif op == '4':
            # 4- Assign doctor to a patient
            admin.assign_doctor_to_patient(patients, doctors)

        elif op == '5':
            # 5- Update admin details
            admin.update_details()

        elif op == '6':
            # 6 - Quit
            #ToDo5
            print('System exited.')
            break

        else:
            # the user did not enter an option that exists in the menu
            print('Invalid option. Try again')

if __name__ == '__main__':
    main()

