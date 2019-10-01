#Task 20 - Consolidation II - Files
#Objective: Read in lines from a file which will include a function to be performed and then the numbers to perform it on, and then execute these commands

import numpy as np
from statistics import mean

#read in the lines of the file into 'fileReader'
fileReader = open('input_Extended.txt','r', encoding='utf-8-sig') #Had to specify the encoding in order to be viewed properly
fileReader.read()
fileReader.seek(0)   #Necessary in order to start reading from line 1 when we iterate through

for i in fileReader:     #Will iterate through the lines of data in 'f' from the text file 
    functionName = str(i[0:3]) #reads in the function name
    
    numString = str(i[4:len(i)+1])  #reads in the numbers which need to be evaluated
    numString = numString.strip()   #Strip all empty spaces or newline/(\n) characters
    numsList = list(numString.split(","))   #Split out numbers into a list
    numsList = [int(x) for x in numsList]   #Cast all numbers to int
    
    if functionName[0] == "p":  #Lines requiring percentile calculations start with a p
        percentileValue = int(functionName[1:3])
        newNumsList = np.array(numsList)
        percentileNum = np.percentile(newNumsList,percentileValue)
        print("The ",str(percentileValue),"th percentile of ",str(numsList)," is: ", str(percentileNum)) 
    else:
        if functionName == "avg":
            functionName = "mean"  #To find an average I will use the mean function so need to change this function name
        exec(str("outputCalc = "+functionName+"("+str(numsList)+")"))       # This will take the values of functionName and numsList and execute them as functions
        print("The ", functionName," of ", str(numsList)," is: ", str(outputCalc))

fileReader.close()