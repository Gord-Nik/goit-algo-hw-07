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

def sum_of_values(node):
    """ Рекурсивно обчислює суму всіх значень у BST """
    if node is None:
        return 0
    return node.val + sum_of_values(node.left) + sum_of_values(node.right)

# Створення дерева
root = TreeNode(50)
insert(root, 30)
insert(root, 20)
insert(root, 40)
insert(root, 70)
insert(root, 60)
insert(root, 80)

# Обчислення суми всіх значень
total_sum = sum_of_values(root)
print("Сума всіх значень у BST:", total_sum)