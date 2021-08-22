import random
import string
id=''
li=list(string.ascii_letters+string.digits)
for i in range(6):
    id+=random.choice(li)
print("The OTP is",id)
