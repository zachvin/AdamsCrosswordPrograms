# Wordlist searcher
# Zach Vincent 2021
# rev. 0.9
# Last updated Thu, April 29

import csv

wordlist = []
wordsToRemove = []

filename = "Documents/PythonCode/AdamsCrosswordPrograms/ActiveWL_4-29-21.csv"
newFilename = "Documents/PythonCode/AdamsCrosswordPrograms/ActiveWL_new.csv"


# Import the file
with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for line in csvfile:
        word, score = line.split(",")
        wordlist.append((word, int(score.rstrip("\n"))))

# Parse file
for pairIndex in range(0, len(wordlist)):

    # Target all words with a score of 20
    if(wordlist[pairIndex][1] == 20):
        targetWord = (wordlist[pairIndex][0] + "s").lower()

        # Check if there is a word with score 50 that is the same as the target word with an "s" at the end
        for crossIndex in range(pairIndex, len(wordlist)):
            currentWord = wordlist[crossIndex][0].lower()
            currentScore = wordlist[crossIndex][1]
            if(targetWord == currentWord and currentScore == 50):
                wordsToRemove.append(wordlist[crossIndex])
                break
            elif(max(targetWord, currentWord) == currentWord):
                break

wordsToWrite = []
nextIndex = 0
for pair in wordlist:
    if(nextIndex < len(wordsToRemove)):
        if(pair[0] != wordsToRemove[nextIndex][0]):
            wordsToWrite.append(pair)
        else:
            nextIndex+=1

with open(newFilename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerows(wordsToWrite)

i = 1
for word in wordsToRemove:
    if(i % 10 == 0):
        print()
    print(word, end="\t")
    i+=1