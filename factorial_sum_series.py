import math
n=int(input("Enter n: "))
total=0
for i in range(1,n+1):
    print(i,"! + ",end="")
    total=total+math.factorial(i)
print("Sum of series is: ",total)    
