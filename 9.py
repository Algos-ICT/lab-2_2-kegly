def file_input():
    fin = open('input.txt', 'r')
    n = int(fin.readline())
    lines = [fin.readline() for i in range(n)]
    nodes = []
    K = []
    for i in range(n):
        Ki, Li, Ri = lines[i].split()
        K.append(int(Ki))
        nodes.append((int(Li), int(Ri)))

    n = int(fin.readline())
    deletes = fin.readline().split()
    deletes = [int(num) for num in deletes]
    fin.close()
    return K, nodes, deletes


def file_output(results):
    fout = open('output.txt', 'w')
    for num in results:
        fout.write(str(num) + '\n')
    fout.close()


def delete(keys, nodes, index):
    if keys[index] is not None:
        keys[index] = None

        if (nodes[index][0] == 0) and (nodes[index][1] == 0):
            return -1
        elif (nodes[index][0] != 0) and (nodes[index][1] == 0):

            if keys[nodes[index][0] - 1] is not None:
                return delete(keys, nodes, nodes[index][0] - 1) - 1
            else:
                return -1

        elif (nodes[index][1] != 0) and (nodes[index][0] == 0):

            if keys[nodes[index][1] - 1] is not None:
                return delete(keys, nodes, nodes[index][1] - 1) - 1
            else:
                return -1

        else:

            if keys[nodes[index][1] - 1] is not None or keys[nodes[index][0] - 1] is not None:
                return delete(keys, nodes, nodes[index][0] - 1) + delete(keys, nodes, nodes[index][1] - 1) - 1
            else:
                return -1

    else:
        return 0


'''def delete_all(keys, nodes, deletes):
    quantity = len(nodes)
    results = []

    for num in deletes:
        k = 0
        try:
            index = keys.index(num)
            if keys[index] is not None:
                keys[index] = None
                k -= 1
                left = nodes[index][0] - 1
                right = nodes[index][1] - 1

                while left != -1 and right != -1:

                    left1 = nodes[left][0] - 1
                    right1 = nodes[right][1] - 1
                    while left1 != -1 and keys[left1] is not None:
                        keys[left1] = None
                        left1 = nodes[left1][0] - 1
                        k -= 1

                    while right1 != -1 and keys[right1] is not None:
                        keys[right1] = None
                        right1 = nodes[right1][1] - 1
                        k -= 1
                    left = nodes[left][0] - 1
                    right = nodes[right][1] - 1

        except ValueError:
            k = 0

        quantity += k

        results.append(quantity)

    return results'''


def main():
    keys, nodes, deletes = file_input()
    results = []
    quantity = len(keys)
    for num in deletes:
        try:
            index = keys.index(num)
            quantity += delete(keys, nodes, index)
            results.append(quantity)
        except ValueError:
            quantity += 0
            results.append(quantity)
    file_output(results)

    file_output(results)


main()
