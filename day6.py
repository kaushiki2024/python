#anything which is enclosed within double quotes or single quotes is known as string

name="kaushiki"
age="20"
friend="myself"
print("topper=>"+name)


#if we have to print double quotes in some lines

#apple=" he said ,"I want to eat an apple"  

apple= 'he said,"I want to eat an apple'
print(apple)

'''unknown='hey harry,
how are you?,
i hope you are good.'''

st="""
hey harry,
how are you?,
i hope you are good.
actually i am feeling tensed these days"""
 
print(st)   #assign string to any word then the whole string can be printed 


#A string is like an array of characters and index always starts with zero

print(name[0])
print(name[1])
print(name[2])
print(name[3])

#for looping through string
loop="""
hey harry,
how are you?,
i hope you are good.
actually i am feeling tensed these days"""
for character in loop:
    print(character)
