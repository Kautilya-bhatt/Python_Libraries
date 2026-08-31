''' #### 1. Student Marks Analyzer #####

Given a list of student marks, write a Python program to calculate and display: 

• Total marks 
• Average marks
• Highest marks 
• Lowest marks
• Number of students who passed 
• Number of students who failed '''

student_marks = [85, 92, 28, 65, 90, 55, 30, 88, 95, 60]
total_marks=0
passs=0
fail=0


highest_marks=student_marks[0]
lowest_marks=student_marks[0]
print(highest_marks)
for marks in student_marks:
    passing_marks=40
    total_marks+=marks   
    if marks  > highest_marks:
        highest_marks=marks
    if marks  < lowest_marks:
        lowest_marks=marks    
    if marks >= passing_marks:
        passs+=1
    else:
        fail+=1

average_marks=total_marks/len(student_marks) 
  
print("• Total marks out off 1000  -->",total_marks)   
print("• Highest marks -->",highest_marks)
print("• Lowest marks -->", lowest_marks)
print("• Number of students who passed -->",passs)
print("• Number of students who failed -->",fail) 
print("• Average marks -->",average_marks)







