import random
import operator

https://stackoverflow.com/questions/26260950/how-can-i-randomly-choose-a-maths-operator-and-ask-recurring-maths-questions-wit


e=int(input('enter the number of digits for first value\n'))
b=int(input('enter the number of digits for another value'))
if e==1:
    d=random.randint(1,10)
elif e==2:
    d=random.randint(10,100)
elif e==3:
    d=random.randint(100,1000)
if b==1:
    f=random.randint(1,10)
elif b==2:
    f=random.randint(10,100)
elif b==3:
    f=random.randint(100,1000)
    
ops = {'+':operator.add,
           '-':operator.sub,
           '*':operator.mul,
           '/':operator.truediv}
op = random.choice(list(ops.keys()))
answer=ops.get(op)(d,f)
print('what is {} {} {}?'.format(d,op,f))
guess=float(input('guess the anwer'))
if guess==answer:
    print('correct')
else:
    print('wrong')
