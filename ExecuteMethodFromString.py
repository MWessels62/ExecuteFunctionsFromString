#Task 20 - Consolidation II - Files
#Objective: read in lines from a file which will include a function to be performed and then the numbers to perform it on, and then execute these commands

import numpy as np 

#read in the lines of the file into 'f'
f = open('input_Extended.txt','r', encoding='utf-8-sig') #Had to specific the encoding otherwise it printed with strange charactes at the start
f.read()
f.seek(0)   #Necessary in order to start reading from line 1 when we iterate through

#Since an "avg" function doesnt exist we needed to define what this should do
def avg(lst): # Python program to get average of a list 
    return sum([int(x) for x in lst]) / len(lst)    #sums the list items and divides by the length of the list

outputCalc = 0
for i in f:     #Will iterate through the lines of data in 'f' from the text file 
    func = str(i[0:3]) #reads in the function name
    numsList = list(i[4:len(i)+1])  #reads in the numbers which need to be evaluated

    numsList[:] = (value for value in numsList if value != ",") # the above commands read in the commas between numbers as individual items so these needed to be removed 
    numsList[:] = (value for value in numsList if value != "\n")
    
    if func[0] == "p":
        percentileValue = int(func[1:3])
        newNumsList = np.array(numsList)
        #print("percentileValue",str(percentileValue))
        #print("newNumsList",str(newNumsList))
        percentileNum = str(np.percentile(newNumsList,percentileValue))
        #print("percentileNum",str(percentileNum))
        print("The ",str(percentileValue),"th percentile of ",str(numsList)," is: ", percentileNum) 
    else:
        exec(str("outputCalc = "+func+"("+str(numsList)+")"))       # This will take the values of func and numsList and execute them as functions
        print("The ", func," of ", str(numsList)," is: ", str(outputCalc))

f.close()