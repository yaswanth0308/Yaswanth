#How many unique words have been used in the sentence? Use the split methods and set to get the unique words.

s = "I am a teacher and I love to inspire and teach people"
s1 = s.split(' ')#spliting the scentence into words
set_s1=set(s1)
set_s1
len(set_s1) #count of words in scentence
