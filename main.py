def askQ(key1,key2,a,b,z):
  sentence = a[key1] + " is to " + b[key1] + ", as " + a[key2] + " is to ... "
  answer = (input(sentence))
  if answer == b[key2]:
    if z < 1:
      print("Well done! You've completed all of the questions!")
    else:
      print("Correct, well done! You have",  z, "questions left")
  else:
    print("Not quite, try again...")
    askQ(key1,key2, a, b, z)
    
usedNums = []

a = ["hot", "summer", "hard", "dry", "simple","light", "weak", "male", "sad", "win", "small","ignore", "buy", "succeed", "reject","prevent", "exclude"]
b = ["cold", "winter", "soft", "wet", "complex","darkness", "strong", "female", "happy","lose", "big", "pay attention", "sell", "fail","accept", "allow", "include"]
from random import randint
for i in range(10):
  key1, key2 = randint(0,len(a)-1), randint(0,len(a)-1)
  if key2 == key1:
    key2 += 1
    if key2 > len(a)-1:
      key2 = 0
  while key1 in usedNums:
    key1 += 1
    if key1 > len(a)-1:
      key1 = 0
  while key2 in usedNums or key2 == key1:
    key2 += 1
    if key2 > len(a)-1:
      key2 = 0
  askQ(key1, key2, a, b, 10 - (i+1))
  usedNums.append(key1)
  usedNums.append(key2)