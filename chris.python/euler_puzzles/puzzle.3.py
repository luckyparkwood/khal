num = 600851475143

for x in range(num+1):
    if x > 1:
        for i in range(2, x):
            if (x % i) == 0:
                break
        else:
            if num % x == 0:
                print(x)

print("done")

