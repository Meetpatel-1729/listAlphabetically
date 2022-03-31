# listAlphabetically is a python program uses list
# You can enter as many words you want
# If you wnat to quit, you can just enter "Quit" and then it will print all the words you have entered  # in alphabetical order


#Append word into list
def appendWord( word ):
    while word.capitalize() != "Quit":
        wordList.append(word.title())

        word = input("Please enter any word: ")
    return wordList  

    
word = input("Please enter any word: ")
wordList = []

wordList = appendWord(word)

wordList.sort()

print( "\nHere is the list of word that you entered in the alphabetical order:" )
for i in wordList:
    print( "Word " + str(wordList.index(i)+1) + ": " + i )

print( "\n" )
