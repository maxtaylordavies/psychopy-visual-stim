import numpy as np

#this function deletes parasize from the str sent
#it returns a list consisting of one number
#ex. if "parasize800.00" is sent, this function will return [800.]
def deleteParasize(str):
    
    #this function replaced the parasize with an empty string
    str = str.replace("parasize", "")
    
    str = str.split(" ")
    
    str = np.asfarray(str, int)
    
    return(int(str[0]))


#this fucntion converts a string into numbers
#ex. if str = [ "1", "2"], this function will return [1., 2.]
def convStr2Dig(str):
    
    #this function splits the str into an array based on where the " " are in the string
    str = str.split(" ")
    
    #this function converts the str data types in the array to floats
    str = np.asfarray(str, float)

    return(str)