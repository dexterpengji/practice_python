import time

timeStart = time.time()

primeNumbers = [2]
for x in range(2, int(input("Type in the max number for prime number looking:"))):
	for de in primeNumbers:
		if x%de == 0:
			print("%d is not a prime number... = %d x %d" % (x,de,x/de))
			break
	else:
		print("%d is a prime number!" % x)
		primeNumbers.append(x)
print("Finished")
print("Prime Numbers: \n",primeNumbers)
print("Number of Prime Numbers: %d" % len(primeNumbers))
print("Time elapsed: %d seconds" % (time.time() - timeStart))
