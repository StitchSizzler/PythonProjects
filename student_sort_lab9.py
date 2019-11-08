"""
This program sorts students according to the key.
Keys can be: ID, name, mark
"""

def main():
    # open file with student's data
    students_file = open("students_lab9.txt", "r")
    students = []
    key = input("Enter key to sort (id, name, mark): ")
    for line in students_file:  # read line by line
        student_id, name, mark = line.split(", ")   # get info from each line
        student = Student(student_id, name, mark, key)   # create student object from info
        students.append(student)    # add each student to list of students
    students_file.close()
        
    students.sort()
    for student in students:
        print(student)
        
  

class Student:
    
    def __init__(self, student_id, name, mark, key):
        self.student_id = student_id
        self.name = name
        self.mark = mark
        if key == "id":
            self.key = self.student_id
        elif key == "name":
            self.key = self.name
        else:   # any invalid keys would be sorted by mark
            self.key = self.mark
    
    def __repr__(self):
        return str(self.student_id+" "+self.name+" "+" "+self.mark)

    
    def __eq__(self,other):
        return self.key == other.key
    
    def __lt__(self,other):
         return self.key < other.key
main()