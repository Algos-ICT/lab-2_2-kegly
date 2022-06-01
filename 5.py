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

    def delete(self, val):
        if self == None:
            return self
        if val < self.key:
            self.left = self.left.delete(val)
            return self
        if val > self.key:
            self.right = self.right.delete(val)
            return self
        if self.right == None:
            return self.left
        if self.left == None:
            return self.right
        min_larger_node = self.right
        while min_larger_node.left:
            min_larger_node = min_larger_node.left
        self.key = min_larger_node.key
        self.right = self.right.delete(min_larger_node.key)
        return self

    def exists(self, val):
        if val == self.key:
            return True

        if val < self.key:
            if self.left == None:
                return False
            return self.left.exists(val)

        if self.right == None:
            return False
        return self.right.exists(val)

    def get_min(self):
        current = self
        while current.left is not None:
            current = current.left
        return current

    def get_max(self):
        current = self
        while current.right is not None:
            current = current.right
        return current

    def next(self, results, num):
        if self.left is not None:
            self.left.next(results, num)
        if self.key is not None:
            if self.key > num:
                results.append(self.key)
        if self.right is not None:
            self.right.next(results, num)
        if results:
            return min(results)
        else:
            return None

    def prev(self, results, num):
        if self.left is not None:
            self.left.prev(results, num)
        if self.key is not None:
            if self.key < num:
                results.append(self.key)
        if self.right is not None:
            self.right.prev(results, num)
        if results:
            return max(results)
        else:
            return None


def main():
    lines = file_input()
    results = []
    bst = BSTNode()
    for line in lines:
        index = line.index(' ')
        num = int(line[index + 1:])
        if line[0] == 'i':
            bst.insert(num)
        elif line[0] == 'd':
            bst.delete(num)
        elif line[0] == 'e':
            value = bst.exists(num)
            if value:
                results.append("true")
            else:
                results.append("false")
        elif line[0] == 'n':
            value = bst.next([], num)
            if value is not None:
                results.append(value)
            else:
                results.append('none')
        elif line[0] == 'p':
            value = bst.prev([], num)
            if value is not None:
                results.append(value)
            else:
                results.append('none')

    file_output(results)


main()
