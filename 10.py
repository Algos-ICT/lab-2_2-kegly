def file_input():
    fin = open('input.txt', 'r')
    n = int(fin.readline())
    lines = [fin.readline() for i in range(n)]
    nodes = []
    K = []
    L = []
    R = []

    for i in range(n):
        Ki, Li, Ri = lines[i].split()
        node = BSTNode(int(Ki))
        nodes.append(node)
        K.append(int(Ki))
        L.append(int(Li))
        R.append(int(Ri))

    for i in range(n):
        l = L[i] - 1
        r = R[i] - 1
        if l != -1:
            nodes[i].left = nodes[l]
        if r != -1:
            nodes[i].right = nodes[r]
    fin.close()
    return nodes


def file_output(result):
    fout = open('output.txt', 'w')
    if result:
        fout.write("YES")
    else:
        fout.write("NO")
    fout.close()


class BSTNode:
    def __init__(self, key=None, parent=None):
        self.parent: BSTNode = parent
        self.left: BSTNode = None
        self.right: BSTNode = None
        self.key = key

    def get_min(self):
        current = self
        while current.left is not None:
            current = current.left
        return current.key

    def get_max(self):
        current = self
        while current.right is not None:
            current = current.right
        return current.key





def check(node, lo, hi, smallest, largest):
    '''if lo > hi:
        return False'''

    if node is None:
        return True
    if node.key <= lo and node.key != smallest or node.key >= hi and node.key != largest:
        return False

    return check(node.left, lo, node.key, smallest, largest) and check(node.right, node.key, hi, smallest, largest)


def main():
    nodes = file_input()

    if nodes:
        smalllest = nodes[0].get_min()
        largest = nodes[0].get_max()
        result = check(nodes[0], smalllest, largest, smalllest, largest)
    else:
        result = True

    file_output(result)


main()