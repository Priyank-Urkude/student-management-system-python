import pandas as pd
import matplotlib.pyplot as plt

student_data = pd.read_csv("student_data.csv")

#columns are name,english,maths,science,sst,computer,average,grade

class Student:
    def __init__(self,name,english,maths,science,sst,computer):
        self.name = name
        self.english = english
        self.maths = maths
        self.science = science
        self.sst = sst
        self.computer = computer

    def average(self):
        return (self.english + self.maths + self.science +
                self.sst + self.computer) / 5

    def grade(self):
        avg = self.average()

        if avg >= 90:
            return "A+"
        elif avg >= 80:
            return "A"
        elif avg >= 70:
            return "B"
        elif avg >= 60:
            return "C"
        elif avg >= 50:
            return "D"
        else:
            return "F"

    def show_graph(self):
        subjects = ["English", "Maths", "Science", "SST", "Computer"]

        marks = [
            self.english,
            self.maths,
            self.science,
            self.sst,
            self.computer
        ]

        plt.bar(subjects, marks, color="red")
        plt.title(f"{self.name}'s Marks")
        plt.xlabel("Subjects")
        plt.ylabel("Marks")
        plt.ylim(0, 100)
        plt.show()

#Creating Student objects from rows in existing csv files

students = []

for _, row in student_data.iterrows():
    student = Student(
        row["name"],
        row["english"],
        row["maths"],
        row["science"],
        row["sst"],
        row["computer"]
    )

    students.append(student)

# Main menu
while True:

    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student Data")
    print("2. View Student Data")
    print("3. View Student Graph")
    print("4. Update Student Data")
    print("5. Delete Student Data")
    print("6. Exit")

    choice = input("Enter your choice: ")

    #Option 1: Add Student
    if choice == '1':
        new_row = []
        for column in student_data.columns[:-2]:
            value = input(f"enter {column}: " )

            if column == "name":
                new_row.append(value)
            else:
                try:
                    mark = float(value)
                    if 0 <= mark <= 100:
                        new_row.append(mark)
                    else:
                        print("Marks must be between 0 and 100")
                        valid = False
                        break
                except ValueError:
                    print("Please enter a valid number")
                    valid = False
                    break
    
        student = Student(*new_row)

        students.append(student)

        student_data.loc[len(student_data)] = new_row + [student.average(), student.grade()]

    #Option 2: View Student Data
    elif choice == '2':

        print("\n----- STUDENT DATA -----")
        print(student_data)

    #Option 3: View Student Graph
    elif choice == '3':

        print("\n----- STUDENT GRAPH -----")
        number = int(input("Enter Student Number (refer to Student data index)"))
        if number in student_data.index.tolist():
            students[number].show_graph()
        else:
            raise ValueError("Invalid index")

    #Option 4: Updating Student Data
    elif choice == "4":
        
        index = int(input("Enter student number (refer to Student data index): "))
        if index not in student_data.index:
            print("Student index does not exist")
            continue
        column = input("Enter subject: ").lower()
        if column in student_data.columns.tolist()[1:-2]:
            value = float(input("Enter new value: "))
            student_data.loc[index, column] = value
            setattr(students[index], column, value)
            student_data.loc[index, "average"] = students[index].average()
            student_data.loc[index, "grade"] = students[index].grade()
        else:
            raise ValueError("subject does not exist")

    #Option 5: Deleting student Data
    elif choice == "5":
        del_student = int(input("Enter student number (refer to Student data index): "))
        if del_student in student_data.index.tolist():
            student_data.drop(del_student, inplace=True)
            students.pop(del_student)

            student_data.reset_index(drop=True, inplace=True)
            print("Student's data is deleted")
        else:
            raise ValueError("index does not exist")
    
    #Option 6: Exit
    elif choice == "6":
        student_data.to_csv("student_data.csv", index=False)
        print("Exited the program")
        break

    else:
    print("Invalid choice. Please enter a number from 1 to 6.")

        

    






    

   
        
        
    
        
   




