class Node:
    def __init__(self):
        self.key = None
        self.left = None
        self.right = None
        self.parent = None
        self.size = None


class binTree:
    def __init__(self):
        self.root = None

    def search(self, data, root):
        if root is None or data == root.key:
            return root
        if data < root.key:
            if root.left is not None:
                return self.search(data, root.left)
            return root
        if root.right is not None:
            return self.search(data, root.right)
        return root

    def insert(self, data):
        if self.root is None:
            self.root = Node()
            self.root.key = data
            self.root.size = 1
        else:
            t = self.search(data, self.root)
            if t.key == data:
                return
            elif data < t.key:
                t.left = Node()
                t.left.key = data
                t.left.parent = t
                t.left.size = 1
            else:
                t.right = Node()
                t.right.key = data
                t.right.parent = t
                t.right.size = 1
            while t is not None:
                t.size += 1
                t = t.parent

    def treeMin(self, root):
        while root.left is not None:
            root = root.left
        return root.key

    def rightAncestor(self, root):
        if root.parent is None:
            return 0
        if root.key < root.parent.key:
            return root.parent.key
        return self.rightAncestor(root.parent)

    def next(self, data):
        if self.root is None:
            return 0
        t = self.search(data, self.root)
        f = False
        if t.key != data:
            self.insert(data)
            f = True
            t = self.search(data, self.root)
        if t.right is not None:
            res = self.treeMin(t.right)
        else:
            res = self.rightAncestor(t)
        if f:
            self.delete(data)
        return res

    def delete(self, data):
        t = self.search(data, self.root)
        if t.right is None:
            par = t.parent
            if t.left is not None:
                t.left.parent = par
            if par is None:
                self.root = t.left
            elif par.left.key == t.key:
                par.left = t.left
            else:
                par.right = t.left
        else:
            x = self.search(self.next(t.key), self.root)
            y = x.right
            par = x.parent
            t.key = x.key
            if x.key != t.right.key:
                x.parent.left = y
                if y is not None:
                    y.parent = x.parent
            else:
                t.right = y
                if y is not None:
                    y.parent = t
        while par is not None:
            par.size -= 1
            par = par.parent

    def kMin(self, root, k):
        if root.right is None:
            s = 0
        else:
            s = root.right.size
        if k == s + 1:
            return root.key
        if k < s + 1:
            return self.kMin(root.right, k)
        return self.kMin(root.left, k - s - 1)


fin = open('input.txt', 'r')
fout = open('output.txt', 'w')
n = int(fin.readline())
T = binTree()
for i in range(n):
    com, key = tuple(map(int, fin.readline().split()))
    if com == 1:
        T.insert(key)
    elif com == -1:
        T.delete(key)
    else:
        fout.write(str(T.kMin(T.root, key)) + '\n')

fin.close()
fout.close()
