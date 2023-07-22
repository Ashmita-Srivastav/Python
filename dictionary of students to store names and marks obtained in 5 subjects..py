#Create a dictionary of students to store names and marks obtained in 5 subjects
Students = {'Arun':'English=88''Hindi=95''Maths=62''Science=42''SocialStudies=56',
         'Ankit':'English=56''Hindi=87''Maths=87.5''Science=65''SocialStudies=74',
         'Bhrat':'English=78.5''Hindi=45''Maths=66''Science=88''SocialStudies=83',
         'Rama':'English=45''Hindi=89''Maths=62''Science=49.5''SocialStudies=78',
         'Sunil':'English=98''Hindi=95''Maths=99''Science=99''SocialStudies=98',
         'Seema':'English=54''Hindi=89''Maths=94''Science=85''SocialStudies=78'}
students=dict()
name=input("Enter the name of the student:")

if name in Students.keys():
    print(Students[name])

else:
    print("No student found with this name")
    A= input("Do you want to add student in dictionary(Y/N):")
    if A==("Y"):
       n=int(input("how many students are there: "))
       for i in range(n):
           sname=str(input("Enter the name of the student: "))
           marks=[]
           for j in range(5):
               mark=float(input("Enter the marks: "))
               marks.append(mark)
               students[sname] = marks
       print("Created dictionary of student is:",students)
       name=input("Enter the name of the student:")

       if name in students.keys():
         print(students[name])
    else:
        print=input("press enter to exit")
        quit()
