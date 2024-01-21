a=int(input("enter any number between 5 and 9"))
if(a>9 or a<5):
  raise ValueError("should be between 5 and 9")