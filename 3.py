def file_input():
    fin = open('input.txt', 'r')
    lines = []

    while True:
        line = fin.readline()
        if line:
            lines.append(line.replace('\n', ''))
        else:
            break
    fin.close()

    return lines


def file_output(results):
    fout = open('output.txt', 'w')
    for num in results:
        fout.write(str(num) + '\n')
    fout.close()


class BSTNode:

    def __init__(self, key=None, parent=None):
        self.parent: BSTNode = parent
        self.left: BSTNode = None
        self.right: BSTNode = None
        self.key = key

    def insert(self, key: int):
        if not self.key:
            self.key = key
            return
        if self.key == key:
            return

        if key < self.key:
            if self.left:
                self.left.insert(key)
            self.left = BSTNode(key, self)

        if self.right:
            self.right.insert(key)
            return
        self.right = BSTNode(key, self)

    def inorder(self, results, num):
        if self.left is not None:
            self.left.inorder(results, num)
        if self.key is not None:
            if self.key > num:
                results.append(self.key)
        if self.right is not None:
            self.right.inorder(results, num)
        if results:
            return min(results)
        else:
            return 0


def main():
    lines = file_input()
    results = []
    bst = BSTNode()
    for line in lines:
        num = int(line[2:])
        if line[0] == '+':
            bst.insert(num)
        elif line[0] == '>':
            value = bst.inorder([], num)
            results.append(value)

    file_output(results)


main()
