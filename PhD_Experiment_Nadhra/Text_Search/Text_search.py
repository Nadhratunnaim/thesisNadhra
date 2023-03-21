import os #Enable underlying OS capabilities
import time

#Path to directory to scan for files
directory = '/Users/nadhra/desktop/PhD_python_coding_experiment/3-Text_Search/textfiles'

#List all files in directory
allFiles = os.listdir('textfiles/')

#Prompt for keywords
keywords = input('Enter words to search for: ').lower().split()

#start
start = time.time()

#Number of keywords is equivalent to the length of the user input list
nrOfKeywords = len(keywords)

#List for storing keywords found in text
keywordsInText = []

#Dictionary for pairing textfiles with number of keyword matches
results = {} 

#Iterate through all textfiles in directory and search for keyword matches
for file in allFiles:
    path = (directory + '/' + file)
    if file.endswith('.txt'):
        with open(path, 'rt') as openFile: #Open and automatically close file
            text = openFile.read().lower().split() #Read text and split into single words
            uniqueWords = list(dict.fromkeys(text)) #Remove duplicate words
            for word in keywords: #For each keyword, do the following:
                if word in uniqueWords: #Check if keyword matches any word in text
                    keywordsInText.append(word)
                    results[file] = len(keywordsInText) #Add number of matches to corresponding file in dictionary
            keywordsInText = [] #Flush keywords

#Check if dictionary is empty
if not results:
    print('No matches found.')

#Insert match percentage as value for corresponding keyword matches
for key, value in results.items():
    results[key] = float(value)/float(nrOfKeywords) * 100

#Transform results into a sorted list, and then back into a dictionary
sortedResults = dict(sorted(results.items(), key=lambda x: x[1], reverse=True)) 

#Show matched files and corresponding match ratio
counter = 0
for key, value in sortedResults.items():
    counter += 1
    print(int(value),'% match in ',key)
    if counter >= 10: #Limit output to ten rows.
        break


print ("Done in :%ss" % (time.time() - start))
