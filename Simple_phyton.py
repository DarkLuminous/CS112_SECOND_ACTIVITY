stud_NAME = str(input("Your name:"))
stud_ID = int(input("ID:"))
stud_course = str(input("Course:"))
stud_section = str(input("Section:"))
stud_grade1 = int(input("1st Grade:"))
stud_grade2 = int(input("2nd Grade:"))
stud_grade3 = int(input("3rd Grade:"))
stud_grade4 = int(input("4th Grade:"))

totalGrade = (stud_grade1 + stud_grade2 + stud_grade3 + stud_grade4)

Average = totalGrade / 4

print("Name:", stud_NAME)
print("ID:", stud_ID)
print("Course:", stud_course)
print("Section:", stud_section)
print("GPA:", Average)