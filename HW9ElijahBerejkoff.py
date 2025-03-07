# Define the Student class
class Student:
    def __init__(self, name, age, grade):
        # Initialize attributes
        self.name = name
        self.age = age
        self.grade = grade

# Define the Staff class
class Staff:
    def __init__(self, name, department, role, salary):
        # Initialize attributes
        self.name = name
        self.department = department
        self.role = role
        self.salary = salary

# Define the Teacher class that inherits from Staff
class Teacher(Staff):
    def __init__(self, name, department, role, salary, age):
        # Call the parent class (Staff) __init__ method to initialize inherited attributes
        super().__init__(name, department, role, salary)  # Using super() as suggested by google because I could not figure it out otherwise
        self.age = age

# Define the Square class
class Square:
    def __init__(self, side_length):
        # Initialize the side length attribute
        self.side_length = side_length

    def area(self):
        # Calculate and return the area of the square
        return self.side_length ** 2

    def perimeter(self):
        # Calculate and return the perimeter of the square
        return 4 * self.side_length

# Instances of Student
student_1 = Student("Elijah", 18, 12)
student_2 = Student("Anakin Skywalker", 28, 66)
# Print student attributes
print(student_1.grade, student_1.name)
print(student_2.age, student_2.name)

# Instances of Teacher
teacher_1 = Teacher("Bob", "Language Arts", "Teacher", 68000, 35)
teacher_2 = Teacher("Bog", "Science", "Teacher", 64000, 40)
# Print teacher attributes
print(teacher_1.name, teacher_1.department, teacher_1.role, teacher_1.salary, teacher_1.age)
print(teacher_2.name, teacher_2.department, teacher_2.role, teacher_2.salary, teacher_2.age)

# Example of Square
square_1 = Square(1324567864532)
# Print square area and perimeter
print("Area:", square_1.area())
print("Perimeter:", square_1.perimeter())
