
"""
class Book:
    def __init__(self,title,author,price):
        
        self.title =title
        self.author = author
        self.price = price

    def print_info(self):
        print(f"{self.title} by {self.author} with price of {self.price}")

    
    def discount_price(self,discount_percentage):
        discount_amount = self.price*(discount_percentage/100)
        print(f"{self.title}'s discount price {discount_amount}")

        new_price =self.price - discount_amount

        print(f"{self.title}'s After discount {new_price}")

book1 = Book("Rich Dad Poor Dad", "Robert Kiyosaki", 500)
book1.discount_price(20)

"""

class Student:

    college_name="ABC university "

    def __init__(self,student_name,marks_scored):
        self.student_name=student_name
        self.marks_scored =marks_scored
    
    def print_student_info(self):
        return f"{self.student_name} scored {self.marks_scored} marks from {self.college_name}."
    
s1 = Student("Mounika",100)
s2 = Student("Manohar",98.8)

print(s1.print_student_info())
print(s2.print_student_info())

Student.college_name = "XYZ Institute"

print(s1.print_student_info())
print(s2.print_student_info())