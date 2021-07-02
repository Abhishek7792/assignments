#assignment4

a=input("enter the altitude at which plan in flying(in feets)")
a=float(a)
if(a<=1000):
    print("safe to land")
else:
    if(a>1000 and a<=5000):
        print("bring down to 1000")
    else:
        if(a>5000):
            
            print("go around and try again")
        
