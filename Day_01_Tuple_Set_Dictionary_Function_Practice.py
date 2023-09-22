#Tuple

marks = (95, 98, 97, 97)
#marks[0] = 98
print(marks.count(97))
print(marks.index(97))



#Set

marks = {98, 97, 95, 95}
print(marks)
for score in marks:
    print(score)



#Dictionary

marks = {"math" : 99, "chemistry" : 98, "physics" : 97}
print(marks)
print(marks["chemistry"])
marks["english"] = 95
print(marks)
marks["math"] = 96
print(marks)    



#Function

def sum(a, b=4):
    print(a + b)
sum(1, 2)
sum(1)
