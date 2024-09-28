class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        parent = None
        node = self.root

        while node is not None:
            parent = node
            if key < node.key:
                node = node.left
            elif key > node.key:
                node = node.right
            else:
                return

        new = Node(key)

        if parent is None:
            self.root = new
        elif key < parent.key:
            parent.left = new
        elif key > parent.key:
            parent.right = new

    def find_min(self, x):
        if self.root is None:
            return 0

        path = []
        node = self.root

        while True:
            path.append(node)
            if x > node.key:
                if node.right is None:
                    break
                node = node.right
            elif x < node.key:
                if node.left is None:
                    break
                node = node.left
            else:
                if node.right is None:
                    break
                node = node.right

                while node.left is not None:
                    node = node.left

                return node.key

        for i in range(len(path) - 1, -1, -1):
            if path[i].key > x:
                return path[i].key

        return 0

def main():
    tree = Tree()
    with open("input.txt") as fin:
        line = fin.readline()
        with open("output.txt", "w") as fout:
            while line:
                items = line.split()
                if items[0] == "+":
                    tree.insert(int(items[1]))
                else:
                    print(tree.find_min(int(items[1])), file=fout)
                line = fin.readline()

if __name__ == "__main__":
    main()