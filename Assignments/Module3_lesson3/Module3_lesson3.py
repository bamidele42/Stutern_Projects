# The students class
print("This program adds student to and removes student from a class")

class Students:
    # This is the parent class
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.email = first + "." + last + "@stutern.com"

    def fullname(self):
        return "{} {}".format(self.first, self.last)


class Group_leader(Students):
    # (1)This is the child's or subclass
    def __init__(self, first, last, student=[]):
        super().__init__(first, last) # Inherit the parent class attributes
        self.student = student

    def add_students(self, student):
        # (2) This method adds students to the list of student
        self.student.append(student)
        print(f"student {student} added to student list{self.student}")

    def remove_students(self, student):
       # (3) This method removes students from the list of students under the group leader
        self.student.remove(student)
        print(f"student {student} has been removed from the list {self.student}")

    def fullname_1(self):
        # (4) This method print the fullname of students in the child's class
        print(f"{self.first} {self.last}")
    



    

# (5) Three instances of the parent class
# student_1 = Students("Temitope", "Bamidele")
# print(student_1.first)
# print(student_1.last)
# print(student_1.email)
# print()
# student_2 = Students("Tawakalitu", "Awonaike")
# print(student_2.first)
# print(student_2.last)
# print(student_2.email)
# print()
# student_3 = Students("Mariam", "Adeoti")
# print(student_3.first)
# print(student_3.last)
# print(student_3.email)

# (6) Two instances of the child's class

stud_1 = Group_leader("Placidus", "Ali")
stud_2 = Group_leader("Praise", "Emmanuel")
# print(stud_1.fullname())
# print(stud_2.fullname())
# print(stud_1.fullname_1())
# print(stud_2.fullname_1())
# print(stud_1.email)
# print(stud_2.email)

#(7) Adding 2 students each to the list of students under the child's class
stud_1.add_students("Placidus")
stud_1.add_students("Ali")
stud_2.add_students("Praise")
stud_2.add_students("Emmanuel")

# (8) Removing 1 student each from the list of students under the child's class

stud_1.remove_students("Placidus")
stud_1.remove_students("Ali")

# (9) Print the full name of the students in the list of students under the instances of your subclass
print(stud_1.fullname())
print(stud_2.fullname())

# (10) Print the email of the instances of your subclass
print(stud_1.email)
print(stud_2.email)



