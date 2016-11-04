class Student(object):
    studentInformation = Student()
    studentInformation.studentID = "2344241"
    studentInformation.firstName = "Ben"
    studentInformation.lastName = "Humphris"
    studentInformation.email = "bhumphris@comcast.net"

    def create_student():
        s = Student()
        s.studentID = raw_input("\nEnter the ID number")
        s.studentFirstName = raw_input("\nEnter student first name")
        s.lastName = raw_input("\nEnter student last name")
        s.Email = raw_input("\nEnter student email address")
        return s
        student1 = create_student()
        student2 = create_student()
        print ("\n\n" + studentInformation.studentID + ' ' + studentInformation.firstName + ' ' + studentInformation.lastName + ' ' + studentInformation.email + "\n\n")
        print ("\n" + student1.studentID + ' ' + student1.FirstName + ' ' + student1.LastName + ' ' + student1.email + "\n\n")
        print ("\n" + student2.studentID + ' ' + student2.FirstName + ' ' + student2.LastName + ' ' + student2.email + "\n\n")



