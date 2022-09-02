#• Calculate the area of a circle and assign the value to a variable name of _area_of_circle_

radius = 30
_area_of_circle_ = 3.14*radius**2     #area=pi*r^2
_area_of_circle_
#Calculate the circumference of a circle and assign the value to a variable name of _circum_of_circle_


_circum_of_circle_ = 2*3.14*radius   #circumference=2*pi*r
_circum_of_circle_
#Take radius as user input and calculate the area

r = float(input("Enter the radius of circle = ")) #radius as input
area = 3.14*r**2
print('area of circle is : {}'.format(area))
