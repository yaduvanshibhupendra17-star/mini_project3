#Student Records and Marks Analyzer

subjects=("python","maths","DBMS")
students=[]
print("students are:",students)
num=int(input("Enter number of students:"))
for i in range(num):
    print()
    student_id=input("Enter student id:")
    student_name=input("Enter student name:")
    marks=[]
    for subject in subjects:
        mark=int(input(f"Enter marks for {subject}:"))
        marks.append(mark)
    student={"id": student_id, "name": student_name, "marks": marks}
    students.append(student)

    print("\n======STUDENT REPORT======")
    unique_subjects=set(subjects)
    for student in students:
        student_id=student["id"]
        student_name=student["name"]
        marks=student["marks"]

        total=sum(marks)
        average=total/len(subjects)
        if average>=75:
            result="Distinction"
        elif average>=40:
            result="Pass"
        else:
            result="Fail"
#displaying the student report
        print(f"\nStudent ID: {student_id}|student Name: {student_name}")
        print(f"python:{marks[0]}|maths:{marks[1]}|DBMS:{marks[2]}")
        print(f"Total Marks:{total}|Average Marks:{average:.2f}|Result:{result}")
print("\nunique subjects are:",unique_subjects)                
print("\nstudents recorded:",len(students))
