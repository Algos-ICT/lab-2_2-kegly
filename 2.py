error = 0.1 ** 10


def file_input():
    fin = open('input.txt', 'r')
    n, A = fin.readline().split()
    fin.close()
    return int(n), float(A)


def file_output(result):
    fout = open('output.txt', 'w')
    fout.write("%.6f" % result)
    fout.close()


def equal(a, b):
    return (abs(a - b) <= error)


def less(a, b):
    return (a < b) and (not equal(a, b))


def more(a, b):
    return (a > b) and (not equal(a, b))


def search_height(left, right, n):
    dots = [0] * n
    dots[0] = right
    result = 1000000000
    while less(left, right):
        dots[1] = (left + right) / 2
        dots[-1] = 0
        is_up = False
        for i in range(2, n):
            dots[i] = 2 * dots[i - 1] - dots[i - 2] + 2
            if (not more(dots[i], 0)):
                is_up = True
                break
        if more(dots[-1], 0):
            result = min(result, dots[-1])
        if is_up:
            left = dots[1]
        else:
            right = dots[1]
    return result


def main():
    n, H = file_input()
    result = search_height(0, H, n)
    file_output(result)


main()
