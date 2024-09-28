class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def __repr__(self):
        return self.key


class KMaxStructure:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self.insert_recursive(self.root, key)

    def insert_recursive(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = Node(key)
            else:
                self.insert_recursive(node.left, key)
        elif key > node.key:
            if node.right is None:
                node.right = Node(key)
            else:
                self.insert_recursive(node.right, key)

    def delete(self, key):
        self.root = self.delete_recursive(self.root, key)

    def delete_recursive(self, node, key):
        if node is None:
            return None
        if key < node.key:
            node.left = self.delete_recursive(node.left, key)
        elif key > node.key:
            node.right = self.delete_recursive(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                successor = self.min(node.right)
                node.key = successor.key
                node.right = self.delete_recursive(node.right, successor.key)
        return node

    def min(self, node):
        curr = node
        while curr.left is not None:
            curr = curr.left
        return curr

    def find_k_max(self, k):
        curr = self.root
        k_largest = None
        count = 0  # счетчик посещенных узлов
        while curr is not None:
            if curr.right is None:
                count += 1
                if count == k:
                    k_largest = curr
                curr = curr.left
            else:
                succ = curr.right
                while succ.left is not None and succ.left != curr:
                    succ = succ.left
                if succ.left is None:
                    succ.left = curr
                    curr = curr.right
                else:
                    succ.left = None
                    count += 1
                    if count == k:
                        k_largest = curr
                    curr = curr.left
        return k_largest.__repr__()


def main():
    with open("input.txt", "r") as file:
        n = int(file.readline().strip())
        operations = [list(map(int, file.readline().strip().split())) for _ in range(n)]

    kmax = KMaxStructure()
    result = []

    for op in operations:
        if op[0] == 1:
            kmax.insert(op[1])
        elif op[0] == 0:
            result.append(str(kmax.find_k_max(op[1])))
        elif op[0] == -1:
            kmax.delete(op[1])

    with open("output.txt", "w") as file:
        file.write("\n".join(result))

if __name__ == "__main__":
    main()