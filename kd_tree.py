import numpy as np
import time 

#10**6 points with 100 dimensions

l=[]
for i in range(10**6):
  l.append(np.random.uniform(-100,100,100))
original=l

#Generating a random query point
query_point=np.random.uniform(-100,100,100)

starttime=time.time()
points=len(l)
dimensions=0
while points>50:
    while dimensions<=100 and points>50:
        temp=[]
        for i in range(points):
            temp.append(l[i][dimensions])
        md=np.median(temp)
        j=[]
        if(query_point[dimensions]<=md):
            for i in range(points):
                if(l[i][dimensions]<=md):
                    j.append(l[i])
        else:
            for i in range(points):
                if(l[i][dimensions]>md):
                    if(l[i][dimensions]>md):
                        j.append(l[i])
        l=j
        points=len(l)
        dimensions=dimensions+1
        
#computing distance among those 50 points
dis=[]
dict={}
for i in range(len(l)):
    s=0
    for j in range(100):
        s=s+(query_point[j]-l[i][j])**2
    s=s**(1/2)
    dict[s]=l[i]
    dis.append(s)
dis.sort()
for i in range(10):
    print(dis[i])
endtime=time.time()
print(endtime-starttime)


#brute force
bu=[]
for i in range(len(original)):
    s=0
    for j in range(100):
        s=s+(query_point[j]-original[i][j])**2
    s=s**(1/2)
    bu.append(s)
bu.sort()
print(bu)
