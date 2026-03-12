class PersonalInfo:

    def __init__(self,name,dob,phone,email):
        self.name = name
        self.dob = dob
        self.phone = phone
        self.email = email

    def display_personal(self):
        print("\nName:",self.name)
        print("Date of Birth:",self.dob)
        print("Phone:",self.phone)
        print("Email:",self.email)


class Education(PersonalInfo):

    def __init__(self,name,dob,phone,email,degree,university,year,cgpa):
        PersonalInfo.__init__(self,name,dob,phone,email)
        self.degree = degree
        self.university = university
        self.year = year
        self.cgpa = cgpa

    def display_education(self):
        print("\nDegree:",self.degree)
        print("University:",self.university)
        print("Year:",self.year)
        print("CGPA:",self.cgpa)


class Experience(Education):

    def __init__(self,name,dob,phone,email,degree,university,year,cgpa,company,role,exp,skills):
        Education.__init__(self,name,dob,phone,email,degree,university,year,cgpa)
        self.company = company
        self.role = role
        self.exp = exp
        self.skills = skills

    def display_experience(self):
        print("\nCompany:",self.company)
        print("Role:",self.role)
        print("Experience:",self.exp,"years")
        print("Skills:",self.skills)


class CandidateProfile(Experience):

    def display_profile(self):
        self.display_personal()
        self.display_education()
        self.display_experience()

    def check_role(self):
        if self.exp > 5:
            print("Eligible for Senior Role")
        else:
            print("Eligible for Junior Role")


c1 = CandidateProfile(
"Hari","5-4-2000","9865089598","Hari@gmail.com",
"B.Tech","ANITS",2018,8.2,
"Infosys","Data Engineer",6,"Python"
)

c2 = CandidateProfile(
"Krishna","29-08-1998","9876767801","krishna@gmail.com",
"B.Tech","IIT Delhi",2021,7.5,
"TCS","Developer",2,"Python, Java"
)

c1.display_profile()
c1.check_role()

c2.display_profile()
c2.check_role()
