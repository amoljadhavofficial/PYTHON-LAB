marks = []
total = 0

print("Enter marks for 5 subjects")
print("Enter -1 to stop")

i = 0
while i < 5:
    m = int(input("Enter marks: "))

    if m == -1:
        break

    if i < 2:
        if m < 0 or m > 100:
            print("Invalid marks")
            continue
    else:
        if m < 0 or m > 50:
            print("Invalid marks")
            continue

    marks.append(m)
    i = i + 1

for x in marks:
    total = total + x

if len(marks) > 0:
    average = total / len(marks)
    print("Total Marks:", total)
    print("Average Marks:", average)

    if average >= 75:
        print("Performance: Excellent")
    elif average >= 60:
        print("Performance: Good")
    elif average >= 40:
        print("Performance: Average")
    else:
        print("Performance: Poor")
else:
    print("No student data entered")