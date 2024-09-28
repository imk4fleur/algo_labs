class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

def check(root):
    if root is None:
        return None

    queue = [(root, -10**9, 10**9)]

    while len(queue) > 0:
        node, min_val, max_val = queue.pop(0)

        if node.left is not None:
            if node.left.key >= node.key or node.left.key >= max_val or node.left.key <= min_val:
                return False
            queue.append((node.left, min_val, node.key))

        if node.right is not None:
            if node.right.key <= node.key or node.right.key >= max_val or node.right.key <= min_val:
                return False
            queue.append((node.right, node.key, max_val))

    return True

def main():
    with open("input.txt") as fin:
        n = int(fin.readline())
        lines = [fin.readline().strip() for _ in range(n)]

        nodes, k, l, r = [], [], [], []
        for line in lines:
            ki, li, ri = map(int, line.split())
            nodes.append(Node(ki))
            k.append(ki)
            l.append(li)
            r.append(ri)

        for i in range(n):
            left = l[i]
            right = r[i]
            if left != -1:
                nodes[i].left = nodes[left]
            if right != -1:
                nodes[i].right = nodes[right]

    with open("output.txt", "w") as fout:
        if nodes:
            result = check(nodes[0])
        else:
            result = True

        if result:
            fout.write("CORRECT")
        else:
            fout.write("INCORRECT")

if __name__ == "__main__":
    main()