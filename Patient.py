class Patient:
    """Patient class"""

    def __init__(self, first_name, surname, age, mobile, postcode, symptom):
        """
        Args:
            first_name (string): First name
            surname (string): Surname
            age (int): Age
            mobile (string): the mobile number
            postcode (string): Postcode
            symptom (string): Patient's symptom
        """
        self.first_name = first_name
        self.surname = surname
        self.age = age
        self.mobile = mobile
        self.postcode = postcode 
        self.symptom = symptom  
        self.__doctor = 'None'

    def full_name(self):
        """Returns the full name of the patient"""
        return f'{self.first_name} {self.surname}'

    def get_doctor(self):
        """Returns the assigned doctor"""
        return self.__doctor

    def link(self, doctor):
    # def link(self):
        """Assign a doctor to the patient"""
        self.__doctor = doctor
        # return self.__doctor
        

    def print_symptoms(self):
        """Prints the symptom of the patient"""
        print(self.symptom)  


    def __str__(self):
        return f'{self.full_name():^11}|{self.__doctor:^8}|{self.age:^5}|{self.mobile:^14}|{self.postcode:^10}'

