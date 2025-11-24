import random

def l20(k):
    x=[]
    for _ in range(20):
        x.append(random.randint(0, 1))

    if 1 not in x:
        x[random.randint(0, 20)]=1
    


    for t in range(20, k+20):
        
        x.append(x[t-3]^x[t-5]^x[t-9]^x[t-20])


    return x

#c=int("".join(str(x) for x in l20()), 2)
#print(l20(1000000)) #Ну дуже багато циферок виходить, прям рілі багато
