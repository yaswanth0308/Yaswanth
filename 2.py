#Create an empty dictionary called dog#
#Add name, color, breed, legs, age to the dog dictionary#

dog = {
'name' : 'peter',
'color' : 'black',
'breed' : 'Bernedoddle',
'legs' : 'four',
'age' : '17 weeks'
}#adding name, color, breed, legs, age keys to empty dictionary dog#
dog
#Create a student dictionary and add first_name, last_name, gender, age, marital status,skills, 
#country, city and address as keys for the dictionary#
student = {
'first_name' : 'Yaswanth',
'last_name' : 'Inuganti',
'gender' : 'Male',
'age' : 23,
'marital_status' : 'single',
'skills' : ['Positive attitude'],
'city' : 'Kansas',
'address' : 'Floyd Dr'
} #adding first_name, last_name, gender, age, marital status,skills, country, city and address as keys for student dictionary#
Student
#Get the length of the student dictionary#

len(student)#Using len fuction to find length of dictionary#
#Get the value of skills and check the data type, it should be a list#

print(student['skills'])#printing the value of skills key from dictionary student# 
print(type(student['skills']))#printing the type of skills key from dictionary student#
#Modify the skills values by adding one or two skills#

student['skills'].append('multi-tasking')#Using append function to add one more value to key skills# 
student
#Get the dictionary keys as a list#

student.keys()#Get the keys as list using .keys#
#Get the dictionary values as a list#

student.values()#Get the values as list using .values#
