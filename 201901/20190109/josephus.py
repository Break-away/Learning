def josephus(m, k , n):
    print("""total:{0}
begin:{1}
find:{2}""".format(m, k, n))
    T = []
    for i in range(1, m+1):
        T.append(i)
    while sum(T) > 0:
        i = 0
        j = 0
        c = 0
        num = 0
        while num <= len(T)-1:
            if T[num] > 0:
                i = i + 1
            else:
                num = num + 1
                if num == len(T):
                    num = 0
                continue
            if i == k:
                j = num
                print('begin:', j+1)
                break
            num = num + 1
        if j+1 == len(T):
            j = -1
        while j+1 <= len(T)-1:
            if T[j+1] > 0:
                c = c + 1
            if c == n:
                T[j+1] = 0
                print('out:', j+1)
                print(T)
                r = j
                break
            if j+1 == len(T) - 1:
                j = -1
                continue
            j = j + 1



josephus(10, 8, 3)