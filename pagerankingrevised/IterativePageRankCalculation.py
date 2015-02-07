'''
Created on Oct 21, 2013

@author: Ankita Muley

This project require Python 2.7 version to run.
To run the program, please pass inlink file path as command line argument.This program requires both the script and input file in the same directory.

Program Iterative version of page rank.output is the Page Rank of siz nodes after 1st, 10th, 100th iteration
'''

import math
import sys
import os

print os.getcwd()
print os.chdir(os.path.dirname(sys.argv[0]))

# Method for Retriving Command line Argument
def getCommandLineArg(): 
    cmdargs = str(sys.argv)
    print "Script Name:",sys.argv[0],len(cmdargs)
    for x in sys.argv:
         print "Argument: ", x
    return str(sys.argv[1])

#pages,Dictionary For total Pages
pages = dict()

#PageSetInlink,Dictionary to Reference page Inlinks, with key=page and value=list of inlink pages
PageSetInlink = dict()

#PageSetOutLink,Dictionary to reference page outlinks count, with key=page and value = count of outlinks from key page
PageSetOutLink = dict()

#PageWithNoInlink,List containing pages which has no inlinks
PageWithNoInlink = list()

#SinkSet, List of pages with no outlinks
SinkSet = list()

#PR, dictionary stores page rank of each page, key= page, value = page rank
PR = dict();

#newPR, dictionary which temprorily stores page rank for each while calculating actual page rank 
newPR = dict()

#perplexities, list containing Perplexities values
perplexities = list();


def DefineSet(filename):
    global  PageSetOutLink
    global pages
    #print "In Define Set"
    fobject = open(filename)
    #For each line in file, do something
    for line in fobject:
        #strip \n from the line
        line = line.rstrip()
        #split line with spaces                
        pageList = line.split();
        #return and remove first page from the list
        givenPage = pageList.pop(0);        
        pages[givenPage] = 0;
        #if page has inlinks,i.e list length is greater than zero than add those pages list in PageSetInlink
        #else add page in PageSetWithNoInlink
        if len(pageList) > 0:
            PageSetInlink[givenPage] =  pageList;
            for eachpage in pageList:
                if eachpage in PageSetOutLink:
                    PageSetOutLink[eachpage] = 1 + PageSetOutLink[eachpage];
                else:
                    PageSetOutLink[eachpage] = 1;
        else:
            PageWithNoInlink.append(givenPage);

    

def CalculatePageRank():
    global PR
    global pages

    #N, gives Total Number of Pages
    N =  float(len(pages));
    #d, damping factor is The probability, at any step, that the person will continue to jump on some page.
    d = 0.85;
    #Initially Page rank of pages is not set, We start by considering each page as equally likely
    if not PR:
        for key,value in pages.iteritems():
            PR[key] = float(1/N)
    #index
    index = 1;
    while index <= 100:
        sinkPR = 0
        for page in SinkSet:                                       # calculate total sink PR */
            sinkPR += PR[page];
        for page in pages:
            newPR[page] = (1.0-d)/N                                # calculate teleportation factor for each page 
            newPR[page] += (d*sinkPR)/N                            # spread remaining sink PR evenly */
           
            #add share of PageRank from in-links 
            if page in PageSetInlink and isinstance(PageSetInlink[page],list):
                inlist = PageSetInlink[page];           
                for inPage in inlist:      
                    newPR[page] += d*PR[inPage]/PageSetOutLink[inPage];   
        
        #Set page rank of each page as calculated above       
        for pge in pages:
            PR[pge] = newPR[pge];
        
        if index==1 or index==10 or index == 100:
            print "For Page WT01-B01-14 after ",index," iteration , Page Rank : ",float(PR['WT01-B01-14']) 
            print "For Page WT01-B01-17 after ",index," iteration , Page Rank : ",float(PR['WT01-B01-17'])
            print "For Page WT01-B01-18 after ",index," iteration , Page Rank : ",float(PR['WT01-B01-18'])
            print "For Page WT01-B01-19 after ",index," iteration , Page Rank : ",float(PR['WT01-B01-19'])
            print "For Page WT01-B01-20 after ",index," iteration , Page Rank : ",float(PR['WT01-B01-20'])
            print "For Page WT01-B01-21 after ",index," iteration , Page Rank : ",float(PR['WT01-B01-21'])
            print "------------------------------------------------------------------------------"
        
        index = index+1
        

def display():
    print "Total pages,P: ",len(pages);
    print "Length of Sink Set,SinkSet:",len(SinkSet);
    print "Length of Set of pages with inlink,M:",len(PageSetInlink);
    print "Length of Set of pages with outlink,L:",len(PageSetOutLink);
    print "------------------------------------------------------------------------------"
    print "Following are Page Rank values after 1st, 10th, 100th iteration:"


fileinput = getCommandLineArg()

#Define all sets except Sink Set
#input: file to read
#output: All the Sets
DefineSet(fileinput)

#Calculate Sink Set
SinkSet = set(pages.keys()) - set(PageSetOutLink.keys())

#Method to display output
display()

#Function Calculate Page Rank
#Uses globalally defined sets 
#output: Values of Perplexities, untill page rank converges
CalculatePageRank();
