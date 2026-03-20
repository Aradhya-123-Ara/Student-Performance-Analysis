marks_list = [85, 90, 78, 92, 88]

print(marks_list)

print("Student Performance Analysis \n")
for marks in marks_list:
 if(marks >= 85):
  print("Marks: " ,marks, " - Excellent")
  
 elif(marks >= 70):
  print("Marks: " ,marks, " - Good")
  
 elif(marks >= 60):
     print("Marks: " ,marks, " - Average")
 else:
     print("need Improvement")
     
if(marks >= 33):
    print("Status: Pass")
else:
    print("Status: Fail")
    
average = sum(marks_list) / len(marks_list)
print("Average marks:" ,average)

highest = max(marks_list)
print("Highest marks:", highest)
    
    
    
     
