
print("enter a number of rows : ")
var1 = int(input())
b=int(input("enter 0 for ascending pattern and 1 for descending pattern\n"))

if(b == 0):
  for row in range(var1):
         # row = var1 - row
         row = row + 1
         print(row*"*")



if(b == 1):
  for row in range(var1):
         row = var1 - row
         print(row * "*")
