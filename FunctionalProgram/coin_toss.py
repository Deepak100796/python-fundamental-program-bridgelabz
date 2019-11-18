import numpy as np


flips=int (input (" enter the number : "))

head=0
tail=0
for i in range(flips):
    toss=np.random.randint(0,2)
    if toss==0:
        head+=1
    else:
        tail+=1

print(head,tail)


