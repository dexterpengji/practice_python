import time

timeStart = time.time()
 
def primes(n):
    P = []
    f = []
    for i in range(n+1):
        if i > 2 and i%2 == 0:
            f.append(1)
        else:
            f.append(0)
    i = 3
    while i*i <= n:
        if f[i] == 0:
            j = i*i
            while j <= n:
                f[j] = 1
                j += i+i
        i += 2
 
    P.append(2)
    for x in range(3,n+1,2):
        if f[x] == 0:
            P.append(x)
            print(x)
 
    return P
 
n = int(input("Type in the max number for prime number looking:"))
P = primes(n)

print("Finished")
print("Prime Numbers: \n",P)
print("Number of Prime Numbers: %d" % len(P))
print("Time elapsed: %d seconds" % (time.time() - timeStart))
