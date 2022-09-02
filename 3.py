#Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)#

S1 = ('john','johnson','trump','biedon')#tuple s1 containings names of siblings#
S1
#Join brothers and sisters tuples and assign it to siblings#

brothers = ('john','johnson')#tuple brothers containing john and johnson#
sisters = ('trump','biedon') #tuple sisters containing trump and biedon#
siblings = sisters + brothers#joining the two tuples(sisters and brothers) into new tuple(siblings)# 
siblings
#How many siblings do you have?#

len(siblings)#Using len function to find length of tuple siblings#
#Modify the siblings tuple and add the name of your father and mother and assign it to family_members#
    
father = 'modi'
mother = 'indira gandi'
family_members = siblings + (father,mother)#adding the parents names and siblings to family_members #
family_members
