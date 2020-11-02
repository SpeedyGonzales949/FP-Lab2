def remove_repetitions(v):
    for i in range(0, len(v) - 2):
        if v.count(v[i]) >= 2:
            v.pop(i)
    print("ex1. removed all repetitive numbers: ", v)


def create_symetrical(x):
    y = 0
    if x < 10:
        return x * 10
    else:
        while x > 0:
            y = y * 10 + x % 10
            x = x // 10
        return y


def find_symetrical(v):
    print("ex2.")
    ct = 0
    for i in range(0, len(v) - 1):
        y = create_symetrical(v[i])
        if v[i + 1:].count(y) > 0:
            ct += 1
            print("{}.pair is {}-{}".format(ct, v[i], y))


def big_num(v):
    v.sort(reverse=True)
    bigNum = 0
    for i in v:
        bigNum = bigNum * 100 + i
    print("ex3. the biggest number:", bigNum)


def crypt(v):
    l=[]
    for i in range(0, len(v)):
      l.append(v[i]^(v[0] * 2 + 50))
    print("ex4. encrypted list:", l)


def check_exp(v, exp):
    num=[]
    l=list(exp)
    index=l.index("=")
    if l.count("!")<=0 and l.count("=")<2:
        l=l[:index]+["="]+l[index:]
    newExp = "".join(l)
    for i in v:
        y = i % 10
        x = i // 10
        if eval(newExp, {"x": x, "y": y}):
            num.append(i)
    print("ex.5 Numbers who fullfill the expression:", num)


def check_Domino(v):
    ct = 1
    ctmax = 1
    imax = 0
    for i in range(0, len(v) - 2):
        if v[i] % 10 == v[i + 1] // 10:
            ct += 1
        else:
            ct = 1

        if ctmax < ct:
            ctmax = ct
            imax = i
    print("ex6. Longest Domino:", v[imax - ctmax + 2:imax + 2])


def smallest_multiple(x, y):
    z = 1
    i = 2
    while x > 1 or y > 1:
        p1 = 1
        p2 = 1
        while x % i == 0:
            p1 *= i
            x = x // i

        while y % i == 0:
            p2 *= i
            y = y // i

        i+=1
        if p1>p2:
            z *= p1
        else:
            z *= p2
    return z

def find_KGV(v,i,j):
    x=1
    for k in range(i,j+1):
        x=smallest_multiple(x,v[k])

    print("ex7. ",x)

