
def genel():
  a=input()
  l=[]
  for i in range(0,int(a)):
      l.append(input())

  def recursive1(bolumler,string):
 
      if(len(string)<4):
          return 0
    
      elif (bolumler>int(len(string)/4)):
          return  recursive1(1,string[1:])

        
      elif len(string)>=4:
      
        l1=string[:bolumler]
        l2=string[bolumler:2*bolumler]
        l3=string[bolumler*2:bolumler*3]
        l4=string[bolumler*3:bolumler*4]
        if (l1==l3==l2[::-1]==l4[::-1]):
          return [len(l1)*4,l1+l2+l3+l4]
    
      return recursive1(bolumler+1,string)
  for i in l:
   if (len(i)<4):
       continue
   print(recursive1(1,i))
  return 0
genel()
