from random import randint as r
x = int(input("How many characters would you like your password to be ? Choose between 8 and 24 "))
while not (8<=x<=24):
  x = int(input("Please choose a length between 8 and 24"))
#Declaring the result variable as a sequence of zeros
pw = ""
for i in range(x):
  pw+="0"
  
s = x // 4 

#Assigning character function
def assign(a,b):
  for i in range (s):
  c = chr(r(a,b))
  k = pw[r(0,x)]
  while k != "0" :
    k = c
  
#Uppercase alphabetic characters
assign(65,90)

#Lowercase alphabetic characters
assign(97,122)

#Numerical characters
assign(48,57)

#Dealing with special characters
#Declaring a list containing the ascii code intervals of symbols then randomly choosing which interval will be given to the assign function 
l = [(32,47),(58,64),(91,96),(123,126)]
assign(r(0,3))

#Displaying result

print ("The generated password for you is : ", pw)
    
