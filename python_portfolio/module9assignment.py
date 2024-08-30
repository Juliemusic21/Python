#Julie Sakai
#Module 9.2 Assignment

class Student:

    #The __init__ method initializes the 
    #first_name and last_name. It is assigned to the
    #attributes of the Student as self.   
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.courses = []

    #Input information for the credits and grade and append it to courses.
    def add_course(self, credits, grade):
        self.courses.append((credits, grade))

    #The calculation of a student's GPA.
    def calculate_gpa(self):
        total_credits = 0
        total_points = 0
        grade_points = {'A': 4.0,'B+': 3.5, 'B': 3.0,'C+': 2.5, 'C': 2.0, 
                        'D': 1.0, 'F': 0.0}
        
        #The loop to add the credits of the course to the total credits.
        #Calculate the total grade pointsa for the current course. 
        #Adding the calculated grade points for current courses to total_points. 
        for credits, grade in self.courses:
            total_credits += credits
            total_points += credits * grade_points[grade]

        #Calculates the GPA correctly to prvent a division by zero error. 
        if total_credits == 0:
            return 0.0
        else:
            return total_points / total_credits
        #calculate the student's GPA and display the cumulative GPA. 
    def display_gpa(self):
        gpa = self.calculate_gpa()
        print(f"Cumulative GPA for {self.first_name} {self.last_name}: {gpa:.2f}")

#The main function. 
def main():
    #Ask user to enter the first and last name of the student.
    first_name = input("Enter student's first name: ")
    last_name = input("Enter student's last name: ")
    student = Student(first_name, last_name)

    while True:
        #Ask user to enter the credits and grade for each source the student has taken.
        credits = float(input("Enter credits (or 0 to finish): "))
        if credits == 0:
            break
        grade = input("Enter grade: ").upper()
        student.add_course(credits, grade)

    #Display the student's cumulative GPA.
    student.display_gpa()

#Call the main function.
if __name__ == "__main__":
    main()