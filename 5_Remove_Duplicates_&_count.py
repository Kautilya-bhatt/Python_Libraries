'''#####5. Remove Duplicates & Count Frequency Use the following list and write a program that creates a list of unique values and calculates the frequency of each value. 
numbers = [10, 20, 10, 30, 20, 40, 10, 50, 30] 
Expected concepts: Lists, sets/dictionaries, loops, and counting logic.#####'''


numbers = [10, 20, 10, 30, 20, 40, 10, 50, 30] 
unique_value=list(set(numbers))
for num in unique_value:
    freq=numbers.count(num)
    print("frequency of a ",num, "is " ,freq)
print("unique values = ",unique_value)

   




   