'''#####4. List Operations Without Built-in Shortcuts Given a list of numbers,
 find the maximum, minimum, sum, average, and second-largest value.
   Condition: Do not use max(), min(), sum(), or sort() for the main logic.######'''

list=[]
sum=0
count=0

list.append(int(input("Enter a num :")))
list.append(int(input("Enter a num :")))
list.append(int(input("Enter a num :")))
list.append(int(input("Enter a num :")))
list.append(int(input("Enter a num :")))
list.append(int(input("Enter a num :")))

largest=list[0]
lowest=list[0]
sec_largest=list[0]
for num in list:
    sum =sum+num
    count+=1
    # if num > largest:
    #    largest=num
       
    if num < lowest:
        lowest=num   

    if num > largest:
        sec_largest = largest
        largest = num
    elif num > sec_largest and num < largest:
        sec_largest = num
    
    
Average=sum/count        
        
print("Sum of list --> ",sum)
print("largest no. --> ",largest)
print("Smallest no. --> ",lowest)
print("Second largest no. --> ",sec_largest)
print("Average of a no. --> ",Average)