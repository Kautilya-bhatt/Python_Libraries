'''#####8. List Comprehension Using the list below, create new lists using list comprehension for:
 • Even numbers 
 • Squares of the numbers 
 • Numbers greater than 50 numbers 
 list  = [10, 25, 40, 55, 70, 85]#####'''

# list=[10,25,40,55,70,85]
# empty_List=[]
# for num in list:
#     if num % 2==0:
#         empty_List.append(num)
# print(empty_List)   
# empty_List.clear()  

# for num in list:
#     empty_List.append(num*num)
# print(empty_List)    
# empty_List.clear()

# for  num in list:
#     if num > 50:
#         empty_List.append(num)
# print(empty_List)     

'''###########################OR####################################'''

list=[10,25,40,55,70,85]

even_number=[num for num in list if num % 2==0]
print(even_number)

square=[num*num for num in list ]
print(square)

greater_fifty=[num for num in list if num > 50]
print(greater_fifty)