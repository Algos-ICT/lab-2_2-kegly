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
        l = L[i]
        r = R[i]
        if l != -1:
            nodes[i].left = nodes[l]
        if r != -1:
            nodes[i].right = nodes[r]
    fin.close()
    return nodes


class BSTNode:
    def __init__(self, key=None, parent=None):
        self.parent: BSTNode = parent
        self.left: BSTNode = None
        self.right: BSTNode = None
        self.key = key




def file_output(result):
    fout = open('output.txt', 'w')
    if result:
        fout.write("CORRECT")
    else:
        fout.write("INCORRECT")
    fout.close()


def check(root: BSTNode):
    if (root == None):
        return None
    que = []
    que.append((root, -1000000000, 10000000000))
    while len(que) > 0:
        line = que.pop(0)
        node = line[0]
        if node.left != None:
            if node.left.key >= node.key or node.left.key >= line[2] or node.left.key <= line[1]:
                return False
            que.append((node.left, line[1], node.key))
        if node.right != None:
            if node.right.key < node.key or node.right.key > line[2] or node.right.key <= line[1]:
                return False
            que.append((node.right, node.key, line[2]))
    return True


def main():
    nodes = file_input()
    if nodes:
        result = check(nodes[0])
    else:
        result = True
    file_output(result)


main()
