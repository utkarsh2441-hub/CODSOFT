import random
import string

def generate_passward(length):
    chr=string.digits + string.ascii_letters + string.punctuation
    password=""

    for i in range(length):
        password = password + random.choice(chr)

    return password

print("!!PASSWORD GENERATOR!!")

length=int(input("Enter password length: "))
password=generate_passward(length)
print("\nGenerated Password : ")
print(password)