import random

print("Welcome to the PyPassword Generator!")

letval = int(input("\n\n\nHow many letters would you like in your password?\n"))
symval = int(input("\nHow many symbols would you like?\n"))
numval = int(input("\nHow many numbers would you like?\n"))

totalChars = letval + symval + numval
typelist = [1,2,3]
passString = ''
letlist = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
symlist = ['!','#','$','%','&','(',')','*','+']
numlist = ['0','1','2','3','4','5','6','7','8','9']

def modType(typeToCheck):
    global letval
    global symval
    global numval
    global typelist
    if typeToCheck == 1:
        letval -= 1
        if letval == 0:
            typelist.remove(1)
    elif typeToCheck == 2:
        symval -= 1
        if symval == 0:
            typelist.remove(2)
    elif typeToCheck == 3:
        numval -= 1
        if numval == 0:
            typelist.remove(3)

for i in range(0, totalChars):

    ranType = random.choice(typelist)
    modType(ranType)
    if ranType == 1:
        passString += random.choice(letlist)
    elif ranType == 2:
        passString += random.choice(symlist)
    elif ranType == 3:
        passString += random.choice(numlist)

print("Your Generated Password is:\n\n" + passString)
