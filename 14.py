def file_input():
    fin = open('input.txt', 'r')
    n = int(fin.readline())
    a = []
    for i in range(n + 1):
        a.append(Node(0, 1, 1, 0))
    for i in range(1, n + 1):
        k, l, r = map(int, fin.readline().split())
        a[i].k = k
        a[i].l = l
        a[i].r = r
        if l > 0:
            a[l].p = i
        if r > 0:
            a[r].p = i
    height(a, n)
    f = 1
    x = int(fin.readline())
    fin.close()
    return a, x, f, n


def file_output(a, n, f):
    fout = open('output.txt', 'w')
    fout.write(str(n + 1) + '\n')
    a = red(a, f)
    for i in range(1, n + 2):
        fout.write(str(a[i].k) + ' ' + str(a[i].l) + ' ' + str(a[i].r) + '\n')
    fout.close()


class Node():
    def __init__(self, key, left, right, parent):
        self.k = key
        self.l = left
        self.r = right
        self.p = parent
        self.h = -1


def height(a, n):
    for i in range(n, 0, -1):
        a[i].h = max(a[a[i].l].h, a[a[i].r].h) + 1


def newHeight(a, i):
    l = a[i].l
    r = a[i].r
    if l != 0:
        a[l].h = max(a[a[l].l].h, a[a[l].r].h) + 1
    if r != 0:
        a[r].h = max(a[a[r].l].h, a[a[r].r].h) + 1
    a[i].h = max(a[l].h, a[r].h) + 1


def lt(a, i):
    j = a[i].r
    p = a[i].p
    if i == a[p].l:
        a[p].l = j
    else:
        a[p].r = j
    a[i].r = a[j].l
    a[a[i].r].p = i
    a[i].p = j
    a[j].l = i
    a[j].p = p
    newHeight(a, i)
    newHeight(a, j)
    return j


def rt(a, i):
    j = a[i].l
    p = a[i].p
    if i == a[p].l:
        a[p].l = j
    else:
        a[p].r = j
    a[i].l = a[j].r
    a[a[i].l].p = i
    a[i].p = j
    a[j].r = i
    a[j].p = p

    newHeight(a, i)
    newHeight(a, j)
    return j


def red(a, s):
    k = 2
    rzv = [s, ]
    rez = [0, ]
    while len(rzv) > 0:
        zam = rzv
        rzv = []
        for i in range(len(zam)):
            if a[zam[i]].l > 0:
                rzv.append(a[zam[i]].l)
                l = k
                k += 1
            else:
                l = 0
            if a[zam[i]].r > 0:
                rzv.append(a[zam[i]].r)
                r = k
                k += 1
            else:
                r = 0
            rez.append(Node(a[zam[i]].k, l, r, 0))
    return rez


def pbal(a, i):
    return a[a[i].l].h - a[a[i].r].h


def balance(a, m):
    i = m
    while i != 0:
        newHeight(a, i)
        if pbal(a, i) == 2:
            if pbal(a, a[i].l) < 0:
                lt(a, a[i].l)
            i = rt(a, i)
        elif pbal(a, i) == -2:
            if pbal(a, a[i].r) > 0:
                rt(a, a[i].r)
            i = lt(a, i)
        k = i
        i = a[i].p
    return k


def add(a, n, m):
    if len(a) == 1:
        a.append(Node(n, 0, 0, 0))
        i = 1
    else:
        i = m
        while True:
            if a[i].k > n and a[i].l == 0:
                a.append(Node(n, 0, 0, i))
                a[i].l = len(a) - 1
                break
            elif a[i].k < n and a[i].r == 0:
                a.append(Node(n, 0, 0, i))
                a[i].r = len(a) - 1
                break
            elif a[i].k > n:
                i = a[i].l
            else:
                i = a[i].r
    return balance(a, i)


def main():
    a, x, f, n = file_input()
    f = add(a, x, f)
    file_output(a, n, f)


main()
