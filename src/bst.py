class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


class BST:
    def __init__(self, root):
        self.root = root
        self.left = None
        self.right = None

    def insert(self, val):
        node = self.root
        while True:
            if val < node.val:
                if node.left:
                    node = node.left
                else:
                    node.left = Node(val)
                    break
            else:
                if node.right:
                    node = node.right
                else:
                    node.right = Node(val)
                    break

    def traverse(self):
        def helper(node):
            if not node:
                return

            print(node.val, end=" ")
            helper(node.left)
            helper(node.right)


        root = self.root
        helper(root)
def main():
    bst = BST(Node(4))
    bst.insert(1)
    bst.insert(0)
    bst.insert(3)
    bst.insert(5)
    bst.insert(6)


    bst.traverse()
main()
