import random
def coin_flip():
    if random.randint(0,1)==0:
        return 'heads'
    else:
        return "tails"
h=0
t=0
for i in range(500000):
    if coin_flip()=='heads':
        h=h+1
    else:
        t=t+1
ratio=h/t
print(ratio)
