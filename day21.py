#how fstring works
#f-strings are a new way to format strings in Python 3.6 and above. They provide an easy, readable way to embed expressions
letter = "Hey my name is {1} and I am from {0}"
country = "India"
name = "Harry"

print(letter.format(country, name)) #it will take the index value old method
print(f"Hey my name is {name} and I am from {country}")
print(f"We use f-strings like this: Hey my name is {{name}} and I am from {{country}}")
price = 49.09999
txt = f"For only {price:.2f} dollars!"
print(txt)
# print(txt.format())
print((f"{2 * 30}"))
print(type(f"(2*30)"))




