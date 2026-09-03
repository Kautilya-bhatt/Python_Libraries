'''###### 6. Dictionary-Based Student Record Create student records using dictionaries with at least the fields Name, Age, and Marks.
 Your program should:
   • Search for a student 
   • Update marks 
   • Find the student with the highest marks
   • Calculate average marks ######'''

students={'chinki':{'name':'chinki','marks': 88},
          'kautilya':{'name':'kautilya','marks': 90},
          'shaurya':{'name':'shaurya','marks': 42},
          'kartik':{'name':'kartik','marks': 58},
          'ayush':{'name':'ayush','marks': 68}
          }
highest_marks=students['chinki']
total_marks=0
search=input("Enter name of student for search : ").lower()

for index,key in enumerate(students):
    total_marks+=students[key]['marks']
     
    if students[key]['marks'] > highest_marks['marks']:
          highest_marks= students[key]
    if (key == search):
        print(f"Student name is found at Index {index} -->  {key} " )
       
        choice=(input("Do you want to update marks  ,press 1/2 for Yes/No Respectively :  "))
        if choice == "1":

           update=int(input("Enter marks u want to update from marking :"))
           students[key]['marks']=update
           print(f"Marks was updated of student {key} at Index {index} marks changed to {update}")
           
           if students[key]['marks'] > highest_marks['marks']:
               highest_marks= students[key]

        if choice =="2":
            print("No marks  updates: ")
    else:
        print("Student Name not Found ")
Average=total_marks/len(students)
           
print(f"Highest marks of Student is : {highest_marks} ")
print(f"Average Marks of students average : {Average}")





  
    