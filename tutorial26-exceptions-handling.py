"""
Exceptions Handling
try
except
else	
finally
Type Of Exception:
ZeroDivisionError
NameError
"""
try:
    x = int(input("Please enter x"))
    y = int(input("Please enter y"))
    print("Call")
    s = x / y
    print("div=", s)
except ZeroDivisionError as e:
    print("ZeroDivisionError:", e)
except NameError as e:
    print("NameError:", e)
except Exception as e:
    print("Exception:", e)
else:
    print("This is Else")
finally:
    print("This is Finally Block")

print("After Try")        
