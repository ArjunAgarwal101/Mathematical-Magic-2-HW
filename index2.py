def primeSeive(n):
    prime=[True for i in range(n+1)]
    print(prime)
    currentNumber=2
    while (currentNumber*currentNumber <= n):
        if(prime[currentNumber]==True):
            for i in range(currentNumber**2,n+1,currentNumber):
                prime[i]=False
        currentNumber+=1
    prime[0]=False
    prime[1]=False
    for p in range (n+1):
     if prime[p]:
        print(p)
    print(prime)
n=100
primeSeive(n)
print("following are the prime number smaller than or equal to")