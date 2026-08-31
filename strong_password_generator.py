import random
lower ="abcdefghjklmnopqrstuvwxyz"
upper ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number ="1234567890"
symbols ="@#$&"
all =lower+upper+number+symbols

length = 12

password=" ".join(random.sample(all,length))
print(password)