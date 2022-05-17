"""
Riase Exception
"""
try:
    n = int(input("Please enter any positive number"))
    if n >=0 :
        print("Number is=", n)
    else:
        raise Exception("Number is not a positive number")    
except Exception as e:
    print("Exception")
    print(e)    