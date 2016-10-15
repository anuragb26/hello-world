def genPrimes():
    start=2
    primeList=[]
    primeList.append(start)
    yield start
    second=3
    n=3
    primeList.append(second)
    yield second
    while(True):
        n=n+2
        isPrime=True
        for prime in primeList:
            if(n%prime==0):
                isPrime=False
                break
        if(isPrime):
            primeList.append(n)
            yield n

x=genPrimes()
for i in range(10):
    print(x.__next__())