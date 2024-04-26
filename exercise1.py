class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    """ Рекурсивно вставляє ключ у дерево BST """
    if root is None:
        return TreeNode(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

def find_max(node):
    """ Знаходить найбільше значення в BST """
    current = node
    while current.right is not None:
        current = current.right
    return current.val

# Створення дерева
root = TreeNode(50)
insert(root, 30)
insert(root, 20)
insert(root, 40)
insert(root, 70)
insert(root, 60)
insert(root, 80)

# Знаходження найбільшого значення
print("Найбільше значення в BST:", find_max(root))