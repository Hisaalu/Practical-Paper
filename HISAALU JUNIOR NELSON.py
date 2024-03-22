class Student:
    University = "Makerere"
    def __init__(self,full_name,registration_number,student_number):
        self.full_name = full_name
        self.registration_number = registration_number
        self.student_number = student_number
    def generate_IDNo(self,IDNo):
        self.generate_IDNo = IDNo
    def generate_total(self,total):
        self.generate_total = total
    def editRegNo(self):
        a=input("\nwould you like to change your registration number?\n Enter 'a' to change\n Enter 'b' to retain\n")
        if a == "a":
            NewRegNo=input("What is your new registration number?\n")
            self.registration_number=NewRegNo
            print(self.full_name,"changed the registration number to",self.registration_number)
        elif a == "b":
            print("No change made")
        else:
            print("invalid input")
    def print_statement(self):
        print("\nName:",self.full_name,"\nUniversity:",self.University,"\nCollege:","\nReg No:",self.registration_number,"\nStudent No:",self.student_number,"\nID No:",self.generate_IDNo,"\nTotal Students",self.generate_total)

class CEDAT_Student(Student):
    college = "CEDAT"
    def __init__(self,full_name,registration_number,student_number):
        Student.full_name = full_name
        Student.registration_number = registration_number
        Student.student_number = student_number
    def generate_IDNo(self,IDNo):
        Student.generate_IDNo = IDNo
    def generate_total(self,total):
        Student.generate_total = total
    def editRegNo(self):
        a = input("\nwould you like to change your registration number?\n Enter 'a' to change\n Enter 'b' to retain\n")
        if a == "a":
            NewRegNo = input("What is your new registration number?\n")
            self.registration_number = NewRegNo
            print(self.full_name, "changed the registration number to", self.registration_number)
        elif a == "b":
            print("No change made")
        else:
            print("invalid input")
    def print_statement(self):
        print("\nName:",self.full_name,"\nUniversity:",self.University,"\nCollege:","\nReg No:",self.registration_number,"\nStudent No:",self.student_number,"\nID No:",self.generate_IDNo,"\nTotal Students",self.generate_total)

class CoCIS_Student(Student):
    college = "CoCIS"
    def __init__(self,full_name,registration_number,student_number):
        Student.full_name = full_name
        Student.registration_number = registration_number
        Student.student_number = student_number
    def generate_IDNo(self,IDNo):
        Student.generate_IDNo = IDNo
    def generate_total(self,total):
        Student.generate_total = total
    def editRegNo(self):
        a = input("\nwould you like to change your registration number?\n Enter 'a' to change\n Enter 'b' to retain\n")
        if a == "a":
            NewRegNo = input("What is your new registration number?\n")
            self.registration_number = NewRegNo
            print(self.full_name, "changed the registration number to", self.registration_number)
        elif a == "b":
            print("No change made")
        else:
            print("invalid input")
    def print_statement(self):
        print("\nName:",self.full_name,"\nUniversity:",self.University,"\nCollege:","\nReg No:",self.registration_number,"\nStudent No:",self.student_number,"\nID No:",self.generate_IDNo,"\nTotal Students",self.generate_total)

class EDUC(Student):
    college = "Education"
    def __init__(self,full_name,registration_number,student_number):
        Student.full_name = full_name
        Student.registration_number = registration_number
        Student.student_number = student_number
    def generate_IDNo(self,IDNo):
        Student.generate_IDNo = IDNo
    def generate_total(self,total):
        Student.generate_total = total
    def editRegNo(self):
        a = input("\nwould you like to change your registration number?\n Enter 'a' to change\n Enter 'b' to retain\n")
        if a == "a":
            NewRegNo = input("What is your new registration number?\n")
            self.registration_number = NewRegNo
            print(self.full_name, "changed the registration number to", self.registration_number)
        elif a == "b":
            print("No change made")
        else:
            print("invalid input")
    def print_statement(self):
        print("\nName:",self.full_name,"\nUniversity:",self.University,"\nCollege:","\nReg No:",self.registration_number,"\nStudent No:",self.student_number,"\nID No:",self.generate_IDNo,"\nTotal Students",self.generate_total)

class EASLIS_Student(CoCIS_Student):
    school = "EASLIS"
    def __init__(self,full_name,registration_number,student_number):
        Student.full_name = full_name
        Student.registration_number = registration_number
        Student.student_number = student_number
    def generate_IDNo(self,IDNo):
        Student.generate_IDNo = IDNo
    def generate_total(self,total):
        Student.generate_total = total
    def editRegNo(self):
        a = input("\nwould you like to change your registration number?\n Enter 'a' to change\n Enter 'b' to retain\n")
        if a == "a":
            NewRegNo = input("What is your new registration number?\n")
            self.registration_number = NewRegNo
            print(self.full_name, "changed the registration number to", self.registration_number)
        elif a == "b":
            print("No change made")
        else:
            print("invalid input")
    def print_statement(self):
        print("\nName:",self.full_name,"\nUniversity:",self.University,"\nCollege:","\nReg No:",self.registration_number,"\nStudent No:",self.student_number,"\nID No:",self.generate_IDNo,"\nTotal Students",self.generate_total)

class SCIT_Student(CoCIS_Student):
    school = "SCIT"
    def __init__(self,full_name,registration_number,student_number):
        Student.full_name = full_name
        Student.registration_number = registration_number
        Student.student_number = student_number
    def generate_IDNo(self,IDNo):
        Student.generate_IDNo = IDNo
    def generate_total(self,total):
        Student.generate_total = total
    def editRegNo(self):
        a = input("\nwould you like to change your registration number?\n Enter 'a' to change\n Enter 'b' to retain\n")
        if a == "a":
            NewRegNo = input("What is your new registration number?\n")
            self.registration_number = NewRegNo
            print(self.full_name, "changed the registration number to", self.registration_number)
        elif a == "b":
            print("No change made")
        else:
            print("invalid input")
    def print_statement(self):
        print("\nName:",self.full_name,"\nUniversity:",self.University,"\nCollege:",CoCIS_Student.college,"\nReg No:",self.registration_number,"\nStudent No:",self.student_number,"\nID No:",self.generate_IDNo,"\nTotal Students",self.generate_total)

class CS_Student(CoCIS_Student):
    department = "Computer Science"
    def __init__(self,full_name,registration_number,student_number):
        Student.full_name = full_name
        Student.registration_number = registration_number
        Student.student_number = student_number
    def generate_IDNo(self,IDNo):
        Student.generate_IDNo = IDNo
    def generate_total(self,total):
        Student.generate_total = total
    def editRegNo(self):
        a = input("\nwould you like to change your registration number?\n Enter 'a' to change\n Enter 'b' to retain\n")
        if a == "a":
            NewRegNo = input("What is your new registration number?\n")
            self.registration_number = NewRegNo
            print(self.full_name, "changed the registration number to", self.registration_number)
        elif a == "b":
            print("No change made")
        else:
            print("invalid input")
    def print_statement(self):
        print("\nName:",self.full_name,"\nUniversity:",self.University,"\nCollege:",CoCIS_Student.college,"\nReg No:",self.registration_number,"\nStudent No:",self.student_number,"\nDepartment:",self.department,"\nID No:",self.generate_IDNo,"\nTotal Students",self.generate_total)

class SE_Student(CoCIS_Student):
    department = "Networks"
    def __init__(self,full_name,registration_number,student_number):
        Student.full_name = full_name
        Student.registration_number = registration_number
        Student.student_number = student_number
    def generate_IDNo(self,IDNo):
        Student.generate_IDNo = IDNo
    def generate_total(self,total):
        Student.generate_total = total
    def editRegNo(self):
        a = input("\nwould you like to change your registration number?\n Enter 'a' to change\n Enter 'b' to retain\n")
        if a == "a":
            NewRegNo = input("\nWhat is your new registration number?\n")
            self.registration_number = NewRegNo
            print(self.full_name, "changed the registration number to", self.registration_number)
        elif a == "b":
            print("No change made")
        else:
            print("invalid input")
    def print_statement(self):
        print("\nName:",self.full_name,"\nUniversity:",self.University,"\nCollege:",CoCIS_Student.college,"\nReg No:",self.registration_number,"\nStudent No:",self.student_number,"\nDepartment:",self.department,"\nID No:",self.generate_IDNo,"\nTotal Students",self.generate_total)

count = 0
id = 100
student1 = Student("Kayiwa John","2020/U/172","2020172")
count += 1
id = id+1
print("\n\nSTUDENT 1")
student1.generate_IDNo(id)
student1.generate_total(count)
student1.print_statement()
student1.editRegNo()

student2 = SE_Student("Lumu Musa","2020/U/18283/EVE","202018283")
count += 1
id = id+1
print("\n\nSTUDENT 2")
student2.generate_IDNo(id)
student2.generate_total(count)
student2.print_statement()
student2.editRegNo()

student3 = CS_Student("Adongo Diana","2020/U/1725","20201725")
count += 1
id = id+1
print("\n\nSTUDENT 3")
student3.generate_IDNo(id)
student3.generate_total(count)
student3.print_statement()
student3.editRegNo()



