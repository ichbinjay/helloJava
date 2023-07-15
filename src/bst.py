import collections

def printLeftView(root):
    if not root:
        return
    queue = [(root, 0)]  # Maintain a queue of nodes and their levels
    level_dict = {}  # Keep track of the first node encountered at each level
    while queue:
        node, level = queue.pop(0)
        if level not in level_dict:
            level_dict[level] = node.data
        if node.left:
            queue.append((node.left, level + 1))
        if node.right:
            queue.append((node.right, level + 1))
    left_view = [level_dict[level] for level in sorted(level_dict.keys())]
    print(' '.join(str(node) for node in left_view))


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
    

    def kthSmallest(self, root, k):
        res = []
        def inorder(root):
            if root:
                nonlocal res
                inorder(root.left)
                res.append(root.val)
                inorder(root.right)

        inorder(root)  
        return res[k-1]
    

    def rightSideView(self, root):
        res = []
        q = collections.deque([root])

        while q:
            rightSide = None
            qLen = len(q)

            for i in range(qLen):
                node = q.popleft()
                if node:
                    rightSide = node
                    q.append(node.left)
                    q.append(node.right)
            if rightSide:
                res.append(rightSide.val)
        return res
    
    def heightOfTree(self, root):
        if root is None:
            return 0
        else:
            height = 0

            def dfs(root, level):
                nonlocal height
                if root:
                    height = max(height, level)
                    dfs(root.left, level+1)
                    dfs(root.right, level+1)

            dfs(root, 0)
            return height


def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        bst = BST(Node(arr[0]))
        for j in range(1, n):
            bst.insert(arr[j])
        print(bst.heightOfTree(bst.root))


main()
