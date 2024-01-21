info={'name':'kaushiki','age':21,'fav_sport':'cricket'}
info.update({'name':'rockey'})
print(info.items())
info.clear()
print(info)
print(info.items())
info={'name':'kaushiki','age':21,'fav_sport':'cricket'}
info.pop('name')
print(info)
info.popitem()
print(info)
info={'name':'kaushiki','age':21,'fav_sport':'cricket'}
del info['age']
print(info)