#Lists

friends = ["amar", "akbar", "anthony"]
print(friends[0])
print(friends[1])
print(friends[-1])
print(friends[-2])
friends[0] = "aman"
print(friends)
print(friends[0:2]) #returns a new list
for friend in friends:
   print(friend)




#List Methods :
marks = ["english", 95, "chemistry", 98]
marks.append("physics")
marks.append(97)
print(marks)
marks.insert(0, "math")
marks.insert(1, 99)
print(marks)
print("math" in marks)
print(len(marks)/2)
marks.clear()
print(marks)
i = 0
while i < len(marks):
   print(marks[i])
print(marks[i+1])
i = i + 2



#Break & Continue

students = ["ram", "shyam", "kishan", "radha", "radhika"]
for student in students:
  if(student == "radha"):
    break
print(student)
for student in students:
  if(student == "kishan"):
    continue
print(student)