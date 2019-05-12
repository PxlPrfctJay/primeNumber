#Program that checks if a number is prime

def isPrime(num):
    #Set up counter to increment by 1 if 
    #any number in a range of 2-num leaves a remainder of 0 after division
    counter = 0
    #loop through range of nums from 2 to provided number 
    for i in range(2,num):
        #if num divided by the current number in the range is 0, add one to counter
        if(num%i==0):
            counter += 1 
    
    if(counter>0):
        #more than 0 number can divide equally into num, return false. not a prime number
        return False
    else:
        #no numbers equally divisible into num, num is prime
        return True

#loop thru range of numbers starting at 1 and not including 30
for i in range(1, 30):
    #use i+1 as argument, if num is prime print to console
	if isPrime(i + 1):
		print(i + 1, end=" ")
