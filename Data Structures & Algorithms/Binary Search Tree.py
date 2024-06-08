class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = TreeNode(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = TreeNode(key)
            else:
                self._insert(node.left, key)
        else:
            if node.right is None:
                node.right = TreeNode(key)
            else:
                self._insert(node.right, key)

    def find(self, key):
        return self._find(self.root, key)

    def _find(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._find(node.left, key)
        else:
            return self._find(node.right, key)

    def delete(self, key):
        self.root, _ = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return node, None
        if key < node.key:
            node.left, deleted_node = self._delete(node.left, key)
        elif key > node.key:
            node.right, deleted_node = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right, node
            elif node.right is None:
                return node.left, node
            min_larger_node = self._find_min(node.right)
            node.key = min_larger_node.key
            node.right, _ = self._delete(node.right, min_larger_node.key)
            return node, node
        return node, None

    def _find_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def height(self):
        return self._height(self.root)

    def _height(self, node):
        if node is None:
            return -1
        left_height = self._height(node.left)
        right_height = self._height(node.right)
        return 1 + max(left_height, right_height)
        
        
bst = BST()
bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(3)
bst.insert(7)

print("Find 7:", bst.find(7))  # Output: TreeNode with key 7
print("Height of tree:", bst.height())  # Output: 2

bst.delete(5)
print("Find 5 after deletion:", bst.find(5))  # Output: None
print("Height of tree after deletion:", bst.height())  # Output: 2