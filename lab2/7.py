class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def check(self, root):
        if not root:
            return True
        level = [[root, -float("inf"), float("inf")]]
        while level:
            next_level = []
            for element in level:
                node, min_val, max_val = element
                if min_val <= node.val < max_val:
                    if node.left:
                        next_level.append([node.left, min_val, node.val])
                    if node.right:
                        next_level.append([node.right, node.val, max_val])
                else:
                    return False
            level = next_level
        return True

def main():
    with open("input.txt") as f:
        n = int(f.readline())
        a = []
        mr = -999999999999
        ml = 99999999999
        for i in range(n):
            q = list(map(int, f.readline().split()))
            if q[0] > mr:
                mr = q[0]
            if q[0] < ml:
                ml = q[0]
            a.append(q)

        for i in range(n):
            a[i][0] = TreeNode(a[i][0])

        for i in range(n):
            if a[i][1] != -1:
                a[i][0].left = a[a[i][1]][0]
            if a[i][2] != -1:
                a[i][0].right = a[a[i][2]][0]

        er = True
        if n > 0:
            er = a[0][0].check(a[0][0])

    with open("output.txt", "w") as fout:
        if er:
            fout.write("CORRECT")
        else:
            fout.write("INCORRECT")

if __name__ == "__main__":
    main()