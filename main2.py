num = input()
number = num.split(" ")


a = int(number[0])
b = int(number[1])
mainA = a
mainB = b
BMM = 1
c = 0
while True :
    c = a % b
    if c == 0 :
        BMM = b
        break
    a = b
    b = c





KMM = (mainA *mainB) // BMM
print(BMM , KMM)

