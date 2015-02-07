import os
import sys
import math


#to change current working directory
print os.getcwd()
os.chdir(os.path.dirname(sys.argv[0]))
#os.chdir('D:\Information Retrival\Assign-2')
print os.getcwd()
print os.listdir('D:\Information Retrival\Assign-2')

#creating a dictionary for words in txt
wordDictionary = dict()

totalWordCount = 0;
totalUniqueCount = 0;
#file I/O
fobject = open('output.txt','r',1)
for line in fobject:
   # print line;
    totalWordCount = totalWordCount+1;
    line = line.replace('\n', '')
    if wordDictionary.has_key(line):
        wordCount = wordDictionary[line];
        wordCount = wordCount+1;
        wordDictionary[line] = wordCount;       
    else:
        wordDictionary[line] = 1;
        totalUniqueCount = totalUniqueCount+1;

items = [(v,k) for k,v in wordDictionary.items()]
items.sort()
items.reverse()
items = [(k,v) for v,k in items]

rank = 1;
numWords = 1;
for key,value in items:
    if rank <= 25:
        numWords += 1;
        Probability = (float(value)*100/float(totalWordCount));
        rPr = rank * Probability;
        print rank ," ",key," ",value," rank =",rank," Probability P of Occurence in % =","%.3f" % (float(value)*100/float(totalWordCount))," rP = ", float(rank)*(float(value)*100/float(totalWordCount));
    elif key[0].lower() == 'f':
        if numWords > 50:
           break;
        else:
            numWords += 1;
            print rank ," ",key," ",value," rank =",rank," Probability P of Occurence in % =","%.3f" % (float(value)*100/float(totalWordCount))," rP = ", float(rank)*(float(value)*100/float(totalWordCount));
    rank+=1;
    
print "Total Number of Words :",totalWordCount;
print "Total Number of Unique Words :",totalUniqueCount;