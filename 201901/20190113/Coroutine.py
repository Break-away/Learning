def consumer():
    r = 'yes'
    while True:
        print('ok')
        n = yield r
        if n is None:
            return
        print('consuming %s' % n)
        r = '200 0K'

def produce(c):
    a = c.send(None)
    print(a)
    for i in range(1, 5):
        print('producing {0}'.format(i))
        m = c.send(i)
        print('Consumer ruturn %s' % m)
    c.close()
c = consumer()
produce(c)