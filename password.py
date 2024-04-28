import random
lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
number = '0123456789'

all = lower + upper + number
length = 8
password = "".join(random.sample(all,length))
print("The Generated Password is :",password)
