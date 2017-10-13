def divide(x,y):
    try:
        result = x / y
        print ("result is",result)
    except ZeroDivisionError:
        print ("Division by Zero")
    except TypeError:
        print ("non integer number")
    else:
        print ("result is",result)
    finally:
        print("executing finally clause")

divide(2,1)
divide('a','b')
print ("done")


# in python For,while and try has "Else"
