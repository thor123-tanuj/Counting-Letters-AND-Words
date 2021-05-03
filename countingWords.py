intro = input("Enter String : ")
characterCount = 0
wordCount = 1

for i in intro : 
    characterCount = characterCount + 1
    if(i == " ") : 
        wordCount = wordCount + 1

    
print("Number of words in a String : ")
print(wordCount)

print("Number of letters in a String : ")
print(characterCount)

