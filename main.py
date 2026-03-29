n = 1
for i in range(1000):
    b = n * n
    a = [int(x) for x in str(b)]
    c = sum(a)
    d =  c - 2
    if d == n:
        print(b)
    n += 1
