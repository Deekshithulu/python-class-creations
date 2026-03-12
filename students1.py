class Student:

    total_fee = 50000

    def __init__(self, name, stid, m1, m2, m3, dob, fee_paid):
        self.name = name 
        self.stid = stid
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        self.dob = dob
        self.fee_paid = fee_paid

    def average(self):
        return (self.m1 + self.m2 + self.m3) / 3

    def cgpa(self):
        avg = (self.m1 + self.m2 + self.m3) / 3
        return avg / 10

    def age(self):
        return 2026 - self.dob

    def fee_balance(self):
        return Student.total_fee - self.fee_paid
    def display(self):
        print("\nStudent Name:", self.name)
        print("Student ID:", self.stid)
        print("Marks:", self.m1, self.m2, self.m3)
        print("Average Marks:", self.average())
        print("CGPA:", self.cgpa())
        print("Age:", self.age())
        print("Fee Balance:", self.fee_balance())


class College:

    def __init__(self, code, name, location):
        self.code = code
        self.name = name
        self.location = location
        self.students = []

    def register_student(self, student):
        self.students.append(student)

    def display_details(self):
        print("College Code:", self.code)
        print("College Name:", self.name)
        print("Location:", self.location)

        print("\nStudent Academic Report")

        for s in self.students:
            s.display()


c = College("Anil", "ANITS College", "Visakhapatnam")
s1 = Student(1,"Ravi",85,78,90,2006,40000)
s2 = Student(2,"Ramu",88,92,80,2007,42000)
s3 = Student(3,"Madhu",70,75,68,2005,30000)

c.register_student(s1)
c.register_student(s2)
c.register_student(s3)

c.display_details()
