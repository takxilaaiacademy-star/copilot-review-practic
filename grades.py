def average(marks):
    total = 0
    for m in marks:
        total = total + m
    return total / len(marks)

def grade(score):
    if score > 90:
        return "A"
    elif score > 75:
        return "B"
    elif score > 50:
        return "C"

students = {"Asha": [88, 92, 79], "Ravi": []}
for name in students:
    print(name, grade(average(students[name])))
###
