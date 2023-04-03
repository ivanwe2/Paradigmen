#4 sporta ako e v spisyka da se dobavi i da se sortira
sports=['basket','football','tennis']

while True:
    
    s=input("Enter favourite sport: \nexit to exit\n")
    if s == "exit":
       print("Goodbye!")
       break
    elif s in sports:
      print("Exists! Have a nice day!")
    else:
       sports.append(s)
       print("New sport detected! Added to list!")

sorted=sorted(sports)
print("All sports sorted:\n")
for i in range(0,len(sorted)):
   print(f"{i+1}: {sorted[i]}")

a="A"
b="B"
c= a or b
print(c)
c = "d"
c == "A" or "C"
print(c)

#second task
#123479
#fdiba
#dostyp do fdiba takovata


subjects=['math','programming','el','sports','paradigmen','music']

print("All subjects:\n")
for i in range(0,len(subjects)):
   print(f"{i+1}: {subjects[i]}")

while True:
    print("All subjects:\n")
    for i in range(0,len(subjects)):
       print(f"{i+1}: {subjects[i]}")
    
    

    s=input("Enter least favourite subject: \nexit to exit\n")
    if s == "exit":
       print("Goodbye!")
       break
    elif s in subjects:
      subjects.remove(s)

      print(f"Removed: {s}. ")
    else:
       subjects.append(s)
       print("Invalid subject detected! Added to list!")