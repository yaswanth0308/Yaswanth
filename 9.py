lst = []
weight = []
no_of_students = int(input("Enter no of students: "))
print('\nEnter student weights in lbs:')
for i in range(0, no_of_students):
    lst.append(int(input()))

for i in range(0, no_of_students):
    weight.append(round(0.453592 * lst[i], 2))

print(weight)

