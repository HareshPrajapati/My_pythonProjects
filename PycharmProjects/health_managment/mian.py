# Health Management System
# 3 clients - HARRY, AJAY and VIRAL
def getdate():
    import datetime
    return datetime.datetime.now()


task = input('WAHT DO YOU WANT TO DO READ OR ADD: ')
if task == 'Add' or task == "add" or task == "ADD":
    patient = input('WRITE \n 1 for HARRY\n 2 for AJAY \n3 for VIRAL \n')
    if patient == "1":
        k = input("Write \n 1 for Exercise and 2 for Food ")
        if k == "1":
            h = open("HARRY1.txt", "a")
            exercise = input("WRITE YOUR EXERCISE ")
            h.write(f"[{str(getdate())}]")
            h.write(f" {exercise}\n")
        elif k == "2":
            h = open("HARRY2.txt", "a")
            Food = input("WRITE YOUR FOOD ")
            h.write(f"[{str(getdate())}]")
            h.write(f" {Food}\n")
    elif patient == "2":
        k = input("Write \n 1 for Exercise and 2 for Food ")
        if k == "1":
            h = open("AJAY1.txt", "a")
            exercise = input("WRITE YOUR EXERCISE ")
            h.write(f"[{str(getdate())}]")
            h.write(f" {exercise}\n")
        elif k == "2":
            h = open("AJAY2.txt", "a")
            Food = input("WRITE YOUR FOOD ")
            h.write(f"[{str(getdate())}]")
            h.write(f" {Food}\n")
    elif patient == "3":
        k = input("Write \n 1 for Exercise and 2 for Food ")
        if k == "1":
            h = open("VIRAL1.txt", "a")
            exercise = input("WRITE YOUR EXERCISE ")
            h.write(f"[{str(getdate())}]")
            h.write(f" {exercise}\n")
        elif k == "2":
            h = open("VIRAL2.txt", "a")
            Food = input("WRITE YOUR FOOD ")
            h.write(f"[{str(getdate())}]")
            h.write(f" {Food}\n")
    else:
        print("you pressed wrong key")
elif task == 'read' or task == 'READ' or task == 'Read':
    thing = input("Press 1 for exercise 2 for food")

    if thing == "1":
        person = input("PRESS 1 FOR HARRY 2 FOR AJAY AND 3 FOR VIRAL")
        if person == '1':

            q = open("HARRY1.txt")
            text = q.read()
            print(text)
        elif person == '1':
            q = open("AJAY1.txt")
            text = q.read()
            print(text)
        elif person == '3':
            q = open("VIRAL1.txt")
            text = q.read()
            print(text)

    elif thing == "2":
        person = input("PRESS 1 FOR HARRY 2 FOR AJAY AND 3 FOR VIRAL")
        if person == '1':

            q = open("HARRY2.txt")
            text = q.read()
            print(text)
        elif person == '1':
            q = open("AJAY2.txt")
            text = q.read()
            print(text)
        elif person == '3':
            q = open("VIRAL2.txt")
            text = q.read()
            print(text)

