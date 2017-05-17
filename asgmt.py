import string
import porter
import os
import math
from numpy import number

docID = 0
dictionary = {}
docDictionary = {}
weightDic = {}

stopwords_list = []
p = porter.PorterStemmer()

for line in open('stopword_list.txt'):
    line = line.strip('\n')
    stopwords_list.append(line)
    
for line in open('cranfield_collection.txt'):#read the file line by line
    line = line.strip('\n')
    #.I marks docID for each document
    if line.find('.I') == 0:
        docID = docID + 1
    #split words by space
    for words in line.split(' '):
        #.A .T .W .B and .I are markings, which should not be considered useful
        if words != '.A' and words != '.T' and words != '.W' and words != '.B' and words != '.I':
            #remove punctuation 
            words = ''.join(l for l in words if l not in string.punctuation)
            words = p.stem(words)
            if words not in stopwords_list:
                #if the word has appeared before
                if words in dictionary:
                    #when the same word appears several times in the same document, 
                    #the docID should be only stored once
                    if docID != dictionary[words][-1]:
                        dictionary[words].append(docID)
                #if the word has not been spotted before
                else:
                    dictionary[words] = []
                    dictionary[words] = [docID]



def calcIDF(wordInDic):
    return math.log(docID/len(wordInDic),2)

def createDocIndex():
    docID = 0
    for line in open('stopword_list.txt'):
        line = line.strip('\n')
        stopwords_list.append(line)
    
    for line in open('cranfield_collection.txt'):#read the file line by line
        line = line.strip('\n')
        #.I marks docID for each document
        if line.find('.I') == 0:
            docID = docID + 1
            docDictionary[docID] = {}
            for words in line.split(' '):
                if words != '.A' and words != '.T' and words != '.W' and words != '.B' and words != '.I':
                    words = ''.join(l for l in words if l not in string.punctuation)
                    words = p.stem(words)
                    if words not in docDictionary[docID]:
                        docDictionary[docID] = {}
                        docDictionary[docID][words] = 0
                    else:
                        docDictionary[docID][words] = docDictionary[docID][words] + 1

def calcWeight(word, documentId):
    createDocIndex()
    maxFreq = 0
    print(docDictionary)
    for freq in docDictionary[documentId].values():
        if freq > maxFreq:
            maxFreq = freq
    wordFreq = docDictionary[documentId][word]
    return calcIDF(word) * (wordFreq/maxFreq)

for words in dictionary:
    weightDic[words] = []
    numberOfDoc = 1;
    while(numberOfDoc <= len(dictionary)):
        weightDic[words].append(calcWeight(words,numberOfDoc))
        
        
    
      
                    
                    
            

