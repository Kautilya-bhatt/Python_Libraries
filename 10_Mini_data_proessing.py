'''####Use try and except appropriately.10. Mini Data Processing Program Use the following data: students = [ {'name': 'Amit', 'marks': 78}, 
              {'name': 'Riya', 'marks': 92},
                {'name': 'Rahul', 'marks': 65},
                  {'name': 'Neha', 'marks': 88},
                    {'name': 'Karan', 'marks': 55} ] 
                    Write a program to:
                      1. Print all student names.
                      2. Calculate the average marks.
                        3. Find the highest-scoring student.
                          4. Find the lowest-scoring student.
                            5. Create a list of students scoring above 75.
                              6. Count the number of passing students.
                                7. Process the data through a function.#####'''

students = [ {'name': 'Amit', 'marks': 78}, 
              {'name': 'Riya', 'marks': 92},
                {'name': 'Rahul', 'marks': 65},
                  {'name': 'Neha', 'marks': 38},
                    {'name': 'Karan', 'marks': 55} ] 
def process_data(std_list):
    sum=0

    name=[]
    mark=[]
    count=0
    passing_marks=40
    highest_score=students[0]
    lowest_score=students[0]

    for student in students:
      name.append(student['name'])
      sum=sum+student['marks']

      if student['marks']>highest_score['marks']:
        highest_score=student

      if student['marks']<lowest_score['marks']:
        lowest_score=student

      if student['marks'] > 75:
        mark.append(student['name'])

      if student['marks'] > passing_marks:
        count+=1      

    Average=sum/len(students)
    print("List of All students ",name)
    print("Average marks of students is ",Average)
    print("highest scores student is ",highest_score['name'], "scores" ,highest_score['marks'])
    print("lowest scores student is ",lowest_score['name'], "scores" ,lowest_score['marks'])
    print("List of Students who scores above 75 is ", mark)
    print("The number of passing students is ", count)


process_data(students)


    

