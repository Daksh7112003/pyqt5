class student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age 
        self.grade = grade

    def get_grade(self):
        return self.grade


class course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def get_students(self):
        return self.students

    def get_average_grade(self):
        value = 0
        for student in self.students:
            value+=student.get_grade()

        return value/len(self.students)


s1 = student("Daksh", 19, 97)


s2=student("Nitin" , 20 , 87)
course1 = course("Science", 2)

course2= course("Maths", 3)

course1.add_student(s1)


course2.add_student(s2)


course2.add_student(s1)


course1.add_student(s2)






print(course1.students[0].name, course1.students[0].grade)

print(course2.students[1].name)
                   

print(course1.students[9].name)


print(course1.get_average_grade())
         


        



