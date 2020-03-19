a=raw_input()
l=[]
N=int(a.split()[0])
M=int(a.split()[1])
def func(M,N,l):
  i=0
  k=0
  sayi=0
  while(i<N):
     xyz=raw_input()
     x=int(xyz.split()[0])
     y=int(xyz.split()[1])
     z=int(xyz.split()[2])

     uzaklik=(x*x+y*y+z*z)**0.5
     l.append(uzaklik)
     i+=1
  l.sort()
  print l
  while(k<len(l)):
     if (M-l[k]>=0):
          sayi+=1
     else:
         break
     
     
     k+=1
  print sayi
  return 0
func(M,N,l)
