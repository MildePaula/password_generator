import random

print(" Nice to see you! \n Need help to generate a strong password? \n Welcome!!\n ")

chars = ("abcdefghijklmnopqrtuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#%&0123456789")

number = int(input("Number of passwords you need: "))
length = int(input("Length of the password(s): "))

print("\nPassword(s) below:")

for n in range(number):
    passwords = ''
    for l in range(length):
        passwords += random.choice(chars)
print(passwords)
