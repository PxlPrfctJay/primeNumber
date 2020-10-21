start=input("Enter starting positive number: ")
end=input("Enter ending positive number: ")

try:
    start1=int(start)
    end1=int(end)
    print("Prime numbers are")
    if start1 < 0 or end1 < 0:
        print("Enter Positive number only")
    else:
        for i in range(start1,end1+1):
            if i==1 or i==0:
                continue
            for j in range(2,i):
                if i%j==0:
                    #It is not a prime number
                    break
            else:
                # It is a prime number
                print(i,end=" ")

except:
    print("Enter Numbers only,characters are not allowed")
