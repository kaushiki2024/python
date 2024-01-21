fruits=['apple','mango','banana']
for index,fruit in enumerate(fruits):
    print(f'{index+1}:{fruit}')
fruits=['apple','mango','banana']
for index,fruit in enumerate(fruits):
    print(index,fruit)
for index,fruit in enumerate(fruits,start=2):
    print(index,fruit)
    # Loop over a string and print the index and value of each character
s = 'hello'
for index, c in enumerate(s):
    print(index, c)