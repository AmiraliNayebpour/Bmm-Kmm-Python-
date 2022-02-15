num = input()
number = num.split(" ")


a = int(number[0])
b = int(number[1])
BMM = 1
if a > b :
    for i in range(1 , a) :
        if a % i == 0 and b % i == 0 :
            BMM = i
elif a < b :
    for i in range(1 , b) :
        if b % i == 0 and a % i == 0 :
            BMM = i
KMM = (a * b) // BMM
print(BMM , KMM)




