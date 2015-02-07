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
words_processed = 0;
#file I/O
fobject = open('output.txt','r',1)
for line in fobject:
   # print line;
    words_processed += 1;
    totalWordCount = totalWordCount+1;
    line = line.replace('\n', '')
    if wordDictionary.has_key(line):
        wordCount = wordDictionary[line];
        wordCount = wordCount+1;
        wordDictionary[line] = wordCount;
        print words_processed , "  ", totalUniqueCount
    else:
        wordDictionary[line] = 1;
        totalUniqueCount = totalUniqueCount+1;
        print words_processed , "  ", totalUniqueCount;




items = [(v,k) for k,v in wordDictionary.items()]
items.sort()
items.reverse()
items = [(k,v) for v,k in items]

#print items;

# dictionary ends here !!
rank = 1;
numWords = 1;
for key,value in items:
        #print "%.3f" % (value*100/totalCount);
        print rank ," ",key," = ",value;
        rank+=1;
    
print "Total Number of Words :",totalWordCount;
print "Total Number of Unique Words :",totalUniqueCount;