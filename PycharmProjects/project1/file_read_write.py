

# f = open("harry.txt","r")
#
# var = f.read()
#
# print(var)
#
# f.close()


# f = open("harry2.txt","r+")
#
# var1 = f.write("hum sab jante hai hi nahi to humk kya kare")
# f.close()
#
#
# f = open("harry2.txt","r+")
# print(f.read())
# f.close()


with open("harry.txt") as f:
    a = f.readline()
    print(a)


r = open("harry.txt")
# z= r.readlines()
print(r.read())

r.close()

