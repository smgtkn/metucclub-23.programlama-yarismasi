a=raw_input()
N=int(a.split()[0])
K=int(a.split()[1])
from math import factorial
def func(N,K):
    if N*9<K:
        print 0
        return 0
    sonuc=factorial(N+K-1)/(factorial(K)*factorial(N-1))
    if K>9:
        i=0
        while K>9:

            sonuc+=((-1)**(i+1))*(factorial(N)/(factorial(i+1)*factorial(N-(i+1))))*(factorial(N+(K-10)-1)/(factorial(K-10)*factorial(N-1)))
            K=K-10
            i+=1
    





    print sonuc%(10**9+7)
    
    return 0
func(N,K)

