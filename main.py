from linked_list import SingleLinkedList

name = "  Rishabh Rawat"  # Sttring type
age = 22  # Int type
percentage = 71.2  # Float type
graduated = True  # Boolean type

print(type(name))  # print the type

# int(x)
# float(x)
# bool(x)
# str(x)
# chr(x) gives the char from the int

# cast to int from string
print(f"Convert from string to int {int('10')}")
# cast to int from float
print(f"Convert from float to int {int(583.236)}")
# cast to float from string
# print(f"Convert from string to float {float("50.26")}")
# cast to float from int
print(f"Convert from int to float {float(45)}")
# cast to string from float
print("Convert from float to string "+str('10.326'))

print(name.upper())  # RISHABH RAWAT
print(name.lower())  # rishabh rawat
print(name.strip())  # Rishabh Rawat
print(name.split(' '))  # '','','Rishabh','Rawat'
print(name.title())     # Rishabh Rawat
print(name.find("awa"))  # 11
print(name.replace("R", "Z"))  # Zishabh Zawat
print(name[2])
print(name[4:10])


print(10+10)  # 20
print(10-10)  # 0
print(10*10)  # 100
print(10/3)  # 3.33333333333335
print(10//3)  # 3
print(3**3)  # 27


# ternary operator
message = "Eligible" if(age > 18) else "Not eligible"
print(message)

# logical operator
# and
# or
# not

yourage = int(input("Enter your age: "))
if yourage > 18 or yourage <= 30:
    print("You are Younger")
elif yourage > 1 or yourage <= 18:
    print("You are Babay")
elif yourage < 0:
    print("Correct the input")
else:
    print("You are older")


# chaining comparsion operator
if(18 <= yourage <= 30):
    print('you are younger')

if 10 == int('10'):  # not equal if we remove int() cast because type also be same
    print("EQUAL")
elif 'apple' > 'rishabh' or 'rishabh' < 'zenth':
    print("Rishabh EQUAL")
else:
    print("Not equal")

# for loop
for num in range(0, 10, 2):  # first 0 is initialize value
    # Second 10 is last iteration condition  third 1 is the steps or increment
    print(f'Num {num}', end='')


for ch in "Rishabh":
    print(ch)


# print even number and iterartion
loop = 1
inc = 0
while loop < 10:
    if(loop % 2 == 0):
        print(f"Even {loop}")
        inc += 1
    loop = loop+1

print(f"Total even is {inc}")

########################################################
# for defing the function


def save_user(**name):
    print(name)


# pass like a json
save_user(name='Rishabh', age=22, char="MALE")
##########################################################


def print_num(*num):
    print(num)


print_num(5, 4, 5, 1, 2, 8, 9, 5, 10)
########################################################


def adding(num1, num2):
    return num1+num2


print(adding(10, 20))
##########################################################


def check_mail(mail, ischeck=False):  # default value ischeck
    if(not ischeck):
        print("mail not check by user")
    else:
        print("Mail is check by user")


check_mail("GMail", True)
check_mail("Yahoo")
###########################################################
# List in the python
mylist = ["Rishabh", "Rawat"]
mylist.append("Hello")
mylist.append("ABP")
mylist.append("Nail")
mylist.insert(0, "Google")
del mylist[3]  # for removing the item
# for removing the item from position and it return the removed item
mylist.pop(3)
mylist.remove("Rishabh")  # remove item from the object
print(mylist[:])
mylist.sort()
mylist.sort(reverse=True)
mylist.reverse()  # for reversing the list
print(mylist)
print(len(mylist))
# for printing the whole list from the loop
for name in mylist:
    print(name.lower())
# nested list
neslist1 = [1, 2, 3]
neslist2 = [4, 5, 6]
neslist3 = [7, 8, 9]
finallist = [neslist1, neslist2, neslist3]
print(finallist)


################################################################################
# working with tuples
mytuple = ("Rishabh", "Rawat")
print(mytuple)


# main function in python
if __name__ == "__main__":
    mysingle = SingleLinkedList()
    mysingle.insertTop(20)
    mysingle.insertTop(30)
    mysingle.insertTop(40)
    mysingle.printlist()
