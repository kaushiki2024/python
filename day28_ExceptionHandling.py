try:
    num=int(input("enter integer number:"))
    a=[7,8]
    print(a[num])
except ValueError:
    print(" entered value is not an integer")
except IndexError:
    print("not a valid index")    
    
