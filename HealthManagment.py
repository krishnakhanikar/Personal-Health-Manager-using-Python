import datetime
def gettime():
    return datetime.datetime.now()

def take(a):
    if a ==1:
        c = int(input("enter 1 for exercise and 2 for food"))
        if c==1:
            value = input("type here\n")
            with open("harry-ex.txt", "a") as kk :
                kk.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")

        elif c==2:
            value = input("type here\n")
            with open("harry-food.txt","a") as kk:
                kk.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")

    elif a == 2:
        c = int(input("enter 1 for exercise and 2 for food"))
        if c == 1:
            value = input("type here\n")
            with open("rohan-ex.txt", "a") as kk:
                kk.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")

        elif c == 2:
            value = input("type here\n")
            with open("rohan-food.txt", "a") as kk:
                kk.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")


    elif a == 3:
        c = int(input("enter 1 for exercise and 2 for food"))
        if c == 1:
            value = input("type here\n")
            with open("hammad-ex.txt", "a") as kk:
                kk.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")

        elif c == 3:
            value = input("type here\n")
            with open("hammad-food.txt", "a") as kk:
                kk.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")

def give(a):
    if a ==1 :
        c = int(input("enter 1 for excersise and 2 for food"))
        if c == 1:
            with open("harry-ex.txt") as kk:
                for i in kk:
                    print(i, end="")
        elif c==2:
            with open("harry-food.txt") as kk:
                for i in kk:
                    print(i, end="")

    elif a ==2 :
        c = int(input("enter 1 for excersise and 2 for food"))
        if c == 1:
            with open("rohan-ex.txt") as kk:
                for i in kk:
                    print(i, end="")
        elif c==2:
            with open("rohan-food.txt") as kk:
                for i in kk:
                    print(i, end="")

    if a ==3 :
        c = int(input("enter 1 for excersise and 2 for food"))
        if c == 1:
            with open("hammod-ex.txt") as kk:
                for i in kk:
                    print(i, end="")
        elif c==2:
            with open("hammod-food.txt") as kk:
                for i in kk:
                    print(i, end="")



print("Welcome to your personal Health Manager")
d = int(input("Type 1 for log the value and 2 for retrieve : "))
if d ==1:
    a = int(input("Type 1 for harry 2 for rohan 3 for hammad : "))
    take(a)
else:
    a = int(input("Type 1 for harry 2 for rohan 3 for hammad : "))
    give(a)