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
        node = BSTNode(Ki)
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


def file_output(inorder, preorder, postorder):
    fout = open('output.txt', 'w')
    for num in inorder:
        fout.write(num + ' ')
    fout.write('\n')
    for num in preorder:
        fout.write(num + ' ')
    fout.write('\n')
    for num in postorder:
        fout.write(num + ' ')
    fout.close()


class BSTNode:
    def __init__(self, key=None, parent=None):
        self.parent: BSTNode = parent
        self.left: BSTNode = None
        self.right: BSTNode = None
        self.key = key

    def preorder(self, vals):
        if self.key is not None:
            vals.append(self.key)
        if self.left is not None:
            self.left.preorder(vals)
        if self.right is not None:
            self.right.preorder(vals)
        return vals

    def inorder(self, vals):
        if self.left is not None:
            self.left.inorder(vals)
        if self.key is not None:
            vals.append(self.key)
        if self.right is not None:
            self.right.inorder(vals)
        return vals

    def postorder(self, vals):
        if self.left is not None:
            self.left.postorder(vals)
        if self.right is not None:
            self.right.postorder(vals)
        if self.key is not None:
            vals.append(self.key)
        return vals


def main():
    nodes = file_input()
    preorder = nodes[0].preorder([])
    inorder = nodes[0].inorder([])
    postorder = nodes[0].postorder([])

    file_output(inorder, preorder, postorder)


main()
