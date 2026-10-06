from array import *
Roll_Number=array("i",[])
Marks=array("i",[])

students=int(input("Enter Number of Students: "))

for result in range(students):
    Hall_Ticket=input("Enter Student Roll Number: ")
    if len(Hall_Ticket)==10:
        Roll_Number.append(int(Hall_Ticket))
    else:
        print("Invalid Number")

    
    Marks.append(int(input("Enter Student Marks: ")))
    continue

print("____________________STUDENT RESULTS_____________________")

print("")

for result in range(students):
    if Marks[result]>=90:
        print("Grade-O+")
        print("Roll Number:",Roll_Number[result],"->","Marks=",Marks[result])
print("")


for result in range(students):
    if Marks[result]>=80 and Marks[result]<90:
        print("Grade-O")
        print("Roll Number:",Roll_Number[result],"->","Marks=",Marks[result])

print("")

for result in range(students):
    if Marks[result]>=75 and Marks[result]<80:
        print("Grade-A+")
        print("Roll Number:",Roll_Number[result],"->","Marks=",Marks[result])

print("")

for result in range(students):
    if Marks[result]>=70 and Marks[result]<75:
        print("Grade-A")
        print("Roll Number:",Roll_Number[result],"->","Marks=",Marks[result])

print("")


for result in range(students):
    if Marks[result]>=65 and Marks[result]<70:
        print("Grade-B+")
        print("Roll Number:",Roll_Number[result],"->","Marks=",Marks[result])

print("")

for result in range(students):
    if Marks[result]>=60 and Marks[result]<65:
        print("Grade-B")
        print("Roll Number:",Roll_Number[result],"->","Marks=",Marks[result])


print("")

for result in range(students):
    if Marks[result]>=55 and Marks[result]<60:
        print("Grade-C+")
        print("Roll Number:",Roll_Number[result],"->","Marks=",Marks[result])

print("")

for result in range(students):
    if Marks[result]>=50 and Marks[result]<55:
        print("Grade-C")
        print("Roll Number:",Roll_Number[result],"->","Marks=",Marks[result])

print("")

for result in range(students):
    if Marks[result]>=35 and Marks[result]<50:
        print("PASS")
        print("Roll Number:",Roll_Number[result],"->","Marks=",Marks[result])

print("")

for result in range(students):
    if Marks[result]<35:
        print("FAIL")
        print("Roll Number:",Roll_Number[result],"->","Marks=",Marks[result])