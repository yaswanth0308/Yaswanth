it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
#Find the length of the set it_companies#

len(it_companies)#Using len fuction to find length#
#Add 'Twitter' to it_companies#

it_companies.add('Twitter')#adding the value twitter to list#
it_companies
#Insert multiple IT companies at once to the set it_companies#

it_companies.update(['Wipro','Infosis'])#Using update fuction to add multiple values to it_companies#
it_companies
#Remove one of the companies from the set it_companies#

it_companies.remove('Wipro')#Using remove fuction to remove a value from it_companies#
it_companies

#What is the difference between remove and discard#

Using remove will throw exception while discard doesn’t throw exception
#Join A and B

A.union(B)#Union fuction is used to join
#Find A intersection B

A.intersection(B)#intersection fuction is used to find common values
#Is A subset of B

A.issubset(B)#issubset is a boolean function it returns true or false
#Are A and B disjoint sets


A.isdisjoint(B)#isdisjoint is a boolean function it returns true or false
#Join A with B and B with A

A.union(B) and B.union(A)#using operation fuction 'and' and union fuction to join to to functions
#What is the symmetric difference between A and B

A.symmetric_difference(B)#function symmetric_difference is used to get elements that are not in intersection
#Delete the sets completely

del A #function del is used to completly delete the set
del B
#Convert the ages to a set 

set_ages = set(age)#converting list to set
set_ages
#compare the length of the list and the set

len(age),len(set_ages)#comparing length of set and list
