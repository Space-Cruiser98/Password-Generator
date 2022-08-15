from random import randint as r
x = int(input("How many characters would you like your password to be ? Choose between 8 and 24 : "))
while not (8<=x<=24):
  x = int(input("Please choose a length between 8 and 24"))
pw =""

s= x//4 

def func1(a,b):
  f=""
  for i in range(s):
    f = f + chr(r(a,b))
  return f 



def func2():
  l1 = [32,58,91,123]
  l2 = [47,64,96,126]
  x= r(0,3)
  y = x 
  return func1(l1[x],l2[y])

pw = func1(65, 90) + func1(97, 122) + func1(48, 57) + func2()

if len(pw) < x :
  k= x - len(pw)
  for i in range (k):
    pw = pw + chr(r(65, 90))

print ("The generated password for you is : ", pw)
