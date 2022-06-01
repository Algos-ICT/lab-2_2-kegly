def file_input():
    fin = open('input.txt', 'r')
    n = int(fin.readline())
    lines = [fin.readline() for i in range(n)]
    nodes = []

    for i in range(n):
        Ki, Li, Ri = lines[i].split()
        nodes.append((int(Li), int(Ri)))

    fin.close()
    return nodes


def file_output(result):
    fout = open('output.txt', 'w')
    fout.write(str(result))
    fout.close()


def find_height(nodes):
    deeps = [0] * (len(nodes) + 1)
    for i in range(len(nodes) - 1, -1, -1):
        if (nodes[i][0] == 0) and (nodes[i][1] == 0):
            deeps[i + 1] = 1
        else:
            deeps[i + 1] = max(deeps[nodes[i][0]], deeps[nodes[i][1]]) + 1
    return deeps[1]


def main():
    nodes = file_input()
    if nodes:
        result = find_height(nodes)
        file_output(result)
    else:
        file_output(0)


main()
