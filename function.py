import numpy as np
from numpy import nan
from pandas import Series
import os


start=0
flag=float('inf')

while(True):
    inputs=input('Please input path and number or press Esc to quit:\n').split()
    if (len(inputs)<2):
        if inputs[0].lower()=='esc':
            break
        else:
            print('please input correct path and number:')
    else:
       
        txt,n=inputs
        n=int(n)+1

        #Read and Count the total lines of file
        df=open(txt,'rb')
        count=0
        while True:
            buffer=df.read(1024*8192)
            if not buffer:
                break
            count+=buffer.count(('\n').encode())
        count+=1
        df.close()

        df=open(txt)

        flag=float('inf')
        start=0


    
        if n<0:
            print("please input a positive number!")
        if n==1:
    
            old=df.readline()
            old=old.split()
            if str(old[0])=='plane1':
                if np.count_nonzero([int(i) for i in old[1:]])<3:
                    print("Erro:%d",n)
        #else:
            #print(old[0],n,old[1:])
    
        if n>count:
            print("Can not find :",n-1)                 
        elif(n>=flag):
            print("Error1:%d",n-1)
        else:
            for i in range(start,n):
                #print("i:",i)
                new=df.readline()
                #print("new line:",new)
                if start==0:
                    #print(start)
                    if str(old[0])=='plane1' and np.count_nonzero([int(i) for i in new.split()[1:]])<3:
                        print("Erro:%d",n)
                        flag=0
                        break
                    else:
                        old=[int(i) for i in new.split()[1:4]]
                        old=[old]
                        #print("old:",old)
                        start=1
                        continue
        
                if str(new.split()[0])=='plane1' and np.count_nonzero([int(i) for i in new.split()[1:]])==6:
                    new1=np.array([[int(i) for i in new.split()[1:4]],[int(i) for i in new.split()[4:]]])
                    if list(np.array(np.sum(old,axis=0)))==list(new1[0]):
                        old=[list(np.sum(new1,axis=0))]
                        start+=1
                        #print("old:",old)
                        continue
                    else:
                        flag=n
                else:
                    print("Erro:",n-1)
                    flag=n
                    break
    
            if(flag<=n):
                pass
            else:
                print(new.split()[0],n-1,old[0][0],old[0][1],old[0][2])
    