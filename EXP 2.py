attendance = int(input("Enter attendance: "))

if attendance <75:
    print("ELIGIBLE")
else:
    print("NOT ELIGIBLE: ATTENDANCE IS LESS THAN 75%")

marks = int(input("Enter marks: "))

if marks >= 80:
    print("GRADE A")
    print("Performance: Excellent")
elif marks >= 70:
    print("GRADE B")
    print("Performance: Great")
elif marks >= 60:
    print("GRADE C")
    print("Performance: Very Good")
elif marks >= 50:
    print("GRADE D")
    print("Performance: Good")
else:
    print("GRADE F")
    print("Performance: Fail")
