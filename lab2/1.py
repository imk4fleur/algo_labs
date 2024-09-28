fout=''

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

def create_bst():
    with open("input.txt") as fin:
        n = int(fin.readline())
        lines = [fin.readline().strip() for _ in range(n)]
        nodes, k, l, r = [], [], [], []

        for i in range(n):
            ki, li, ri = lines[i].split()
            node = Node(int(ki))
            nodes.append(node)
            k.append(int(ki))
            l.append(int(li))
            r.append(int(ri))

        for i in range(n):
            left = l[i]
            right = r[i]
            if left != -1:
                nodes[i].left = nodes[left]
            if right != -1:
                nodes[i].right = nodes[right]

    return nodes[0]

def in_order(tree):
    if tree:
        in_order(tree.left)
        print(tree.key, end=" ", file=fout)
        in_order(tree.right)

def pre_order(tree):
    if tree:
        print(tree.key, end=" ", file=fout)
        pre_order(tree.left)
        pre_order(tree.right)

def post_order(tree):
    if tree:
        post_order(tree.left)
        post_order(tree.right)
        print(tree.key, end=" ", file=fout)

def main():
    with open("output.txt", "w") as f_out:
        global fout
        fout = f_out
        tree = create_bst()
        in_order(tree)
        print(file=fout)
        pre_order(tree)
        print(file=fout)
        post_order(tree)

if __name__ == "__main__":
    main()
