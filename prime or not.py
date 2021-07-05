 # assignment 4 
# to check prime or not
a=input("enter number")
a=int(a)
def test_prime(n):
    if (n==1):
        return ("not prime")
    elif (n==2):
        return ("prime")
    else:
        for x in range(2,n):
            if(n % x==0):
                return ("not prime")
        return ("prime")             
print(test_prime(a))