T=int(raw_input())
l1=[]

def func(T):
 i=0
 temp=1
 while (i<T):
    row=int(raw_input())
    row=(row+1)/2
    l=range(2*row*row-5,2*row*row+1,2)
    
    print l[-1]+l[-2]+l[-3]
    
    
    i+=1
 
 return 0
func(T)
        
