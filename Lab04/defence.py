def cube(n):
    for num in range (1,n+1):
        yield num**3
n = int(input())
generator=cube(n)
for i in generator:
    print(i)