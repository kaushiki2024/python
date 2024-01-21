info={'name':'kaushiki','age':21,'Fav_sports':'cricket'}
print(info.keys())
print(info.values())
print(info.items())
print(info['name'])# throw error when key not exist
print(info.get('name'))#ddo not throw error when key not exist
#1method
for i in info.keys():
   print(f"The value corresponding to the key {i} is {info[i]}")
#2method
for key, value in info.items():
  print(f"The value corresponding to the key {key} is {value}") 