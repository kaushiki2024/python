a = "hello"
b = "hello"

print(a == b)  # True
print(a is b)  # True

a = 5
b = 5

print(a == b)  # True
print(a is b)  # True

a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)  # True
print(a is b)  # false

a=(1,2)        #tuple is immutable object.Both are given same location 
b=(1,2)
print(a == b)  # True
print(a is b)  # True