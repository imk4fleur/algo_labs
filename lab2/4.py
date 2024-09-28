def binary_search(a, left, right, x):
    while left <= right:
        mid = left + (right - left) // 2
        if a[mid] == x:
            return None
        if a[mid] < x:
            right = mid - 1
        else:
            left = mid + 1
    return right

class BST:
    def __init__(self):
        self.a = []

    def insert(self, val):
        index = binary_search(self.a, 0, len(self.a) - 1, val)
        if index is not None:
            self.a = self.a[: index + 1] + [val] + self.a[index + 1:]

def main():
    bst = BST()
    result = ""
    with open("input.txt") as fin:
        for i in fin.readlines():
            cmd = i.split()
            v, cmd = cmd[1], cmd[0]
            if cmd == "+" and int(v):
                bst.insert(int(v))
            if cmd == "?":
                result += str(bst.a[-int(v)]) + "\n"
    with open("output.txt", "w") as fout:
        print(result, file=fout)

if __name__ == "__main__":
    main()