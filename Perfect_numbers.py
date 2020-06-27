# Python program to print perfect number

# function definition for perfect

def perfect(n):
    
    s=0
    
    for i in range(1,n+1 // 2): # n+1 is to count the last number.
        
        if n % i ==0:
            
            s = s + i
    return(s)

# function definition to print perfect number
    
def perfect_numbers():
    
    r = int(input("Enter the maximum range to get perfect number : "))
    
    for x in range(1,r+1):
        
        if x == perfect(x):
            print("\n",x,"is a perfect number.")
        

# function call
perfect_numbers()
