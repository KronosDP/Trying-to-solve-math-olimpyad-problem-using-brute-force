import math

print("the following triples that statisfy sqrt(a)+sqrt(b)=sqrt(n) is...")

for n in range(1, 1000):
    for a in range(1, 1000):
        for b in range(1, 1000):
            if a+b+2 * math.sqrt(a * b) == n:
                print("(a,b,n) = ({},{},{})".format(a, b, n))
