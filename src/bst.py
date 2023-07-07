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
            elif val > node.val:
                if node.right:
                    node = node.right
                else:
                    node.right = Node(val)
                    break

    def preorder(self, node):
        if node:
            print(node.val, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.val, end=" ")
            self.inorder(node.right)

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.val, end=" ")


    def isFBT(self, root):
        if root is None:
            return True
        if root.left is None and root.right is None:
            return True
        if root.left is None or root.right is None:
            return False
        return self.isFBT(root.left) and self.isFBT(root.right)

    def isCBT(self, root):
        q = [root]
        flag = False
        while q:
            node = q.pop(0)
            if node.left:
                if flag:
                    return False
                q.append(node.left)
            else:
                flag = True
            if node.right:
                if flag:
                    return False
                q.append(node.right)
            else:
                flag = True
        return True




def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        bst = BST(Node(arr[0]))
        for j in range(1, n):
            bst.insert(arr[j])

        print(str(bst.isCBT(bst.root)).lower())


main()
