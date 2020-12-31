class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):

        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def display(self, root):
        res = []
        if root:
            res = self.display(root.left)
            res.append(root.data)
            res = res + self.display(root.right)
        return res

l=int(input("Enter the number of elements"))
n=int(input("Enter the elements"))
root = Node(n)
for i in range((l-1)):
    e=int(input())
    root.insert(e)
print(root.display(root))
