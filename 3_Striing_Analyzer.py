''' ##### 3. String Analyzer Take a sentence as input and calculate:
• Total characters
• Total words 
• Number of vowels 
• Number of consonants 
• Number of digits 
• Number of spaces ##### '''

text = input("Enter any Sentence : ") 
vowel=0
consonant=0
spaces=0
digit=0
total_chars=len(text)
total_words=len(text.split())
vowels="AEIOUaeiou"
consonants="BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz"
digits="0123456789"
for char in text:
    if char in vowels:
        vowel+=1
    if char in consonants:
        consonant+=1
    if char in " ":
        spaces+=1
    if char in digits:
            digit+=1
print("• Total characters --> " ,total_chars)
print("• Total words --> " ,total_words)
print("• Number of vowels --> " ,vowel)
print("• Number of consonants --> " ,consonant)
print("• Number of spaces --> " ,spaces)
print("• Number of digits --> " ,digit)