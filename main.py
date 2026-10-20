import random
caratteri = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
numero = input('quanti cratteri devo inserire?')
password = ''
for i in(int(numero)):
    carattere = random.choice(caratteri)
    password += carattere
print(password)


    

