import numpy as np
#ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]#
#Sort the list and find the min and max age#

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort() #sorting the ages using sort function#
ages

#Add the min age and the max age again to the list#

ages.append(min(ages)) #Adding min ages to the ages#
ages.append(max(ages)) #Adding man ages to the ages#
ages

#Find the median age (one middle item or two middle items divided by two)#

np.median(ages) #Using median function to find the middle item#

#Find the average age (sum of all items divided by their number)#

np.average(ages) #Using average function to find the average age#

#Find the range of the ages (max minus min)

range_ages = range(min(ages),max(ages)) #range of ages form min to max#
range_ages

