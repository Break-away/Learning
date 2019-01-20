def gen(n):
    a = ''
    for i in range(0, n):
        yield i, a
        a = 'i'

a = gen(1)
print(next(a))
