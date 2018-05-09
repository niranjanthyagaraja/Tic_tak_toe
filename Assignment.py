#variables

#variablesend

#CODE
print("WELCOME TO TIC_TAC_TOE")
while True:
    name1 = input("Enter Player1 name:")
    if name1.isalpha():
        break
    else:
        print("Enter only alphabets")
while True:
    name2 = input("Enter Player2 name:")
    if name2.isalpha():
        break
    else:
        print("Enter only alphabets")
while True:
    bsize = int(input("Please enter the size of the board"))
    n = bsize % 2
    if n == 0:
        print("Please enter an odd number ")
    else:
        break

for i in range(bsize):
    print("|_|" * bsize)

print ("Let's start the Game!")
