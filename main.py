import random 
pasword = ("+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")
password = ("abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXY")
pasrd = ("1234567890")
who = input("Какой тип пароля тебе нужен ? ")
long = int(input("Какая длинна пороля нужна ? "))
code = ""

if who == "Буквенный":
    for i in range(long):
        code = random.choice(password) + code
    print(code)
elif who == "Цифорный":
    for i in range(long):
        code = random.choice(pasrd) + code
    print(code)
