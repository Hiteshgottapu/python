import random
passlen= int(input("enter t length of the password"))
s="abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*+-"
p="".join(random.sample(s,passlen))
print(p)