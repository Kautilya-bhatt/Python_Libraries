''' ##### 2. Number Classification ######
 Write a Python program to examine the numbers from 1 to 100 and identify/count: 
 • Even numbers 
 • Odd numbers 
 • Multiples of 3 
 • Prime numbers
'''
even=0
odd=0
multiple=0
prime=0
for num in range(1,101):
    if num % 2==0:
        even+=1
    if num % 2 !=0:
        odd+=1
    if num % 3 ==0:
        multiple+=1
    if num >1:
        is_Prime=True
        for i in range(2,num):
            if num % i == 0:
                is_Prime=False
                break
        if is_Prime == True:
             prime+=1

print(" •  NO.of Even numbers--> ", even) 
print(" •  NO.of odd numbers--> ", odd)      
print(" •  NO.of Multiple of  3 --> ", multiple)      
print(" •  NO.of prime numbers--> ", prime)                    
         

        
             

    
