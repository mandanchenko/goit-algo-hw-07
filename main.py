class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root


def search(root, key):
    if root is None or root.val == key:
        return root
    if key < root.val:
        return search(root.left, key)
    return search(root.right, key)


# Завдання 1 - знаходження мінімального значення в двійковому дереві пошуку
def min_value_node(node):
    current = node
    while current.left:
        current = current.left
    return current


# Завдання 2 - знаходження максимального значення в двійковому дереві пошуку
def max_value_node(node):
    current = node
    while current.right:
        current = current.right
    return current


# Завдання 3 - знаходження суми всіх значень в двійковому дереві пошуку
def sum_value_node(root):
    if root is None:
        return 0
    return root.val + sum_value_node(root.left) + sum_value_node(root.right)


def preorder_traversal(root):
    if root:
        print(root.val)
        preorder_traversal(root.left)
        preorder_traversal(root.right)


def delete(root, key):
    if not root:
        return root

    if key < root.val:
        root.left = delete(root.left, key)
    elif key > root.val:
        root.right = delete(root.right, key)
    else:
        if not root.left:
            temp = root.right
            root = None
            return temp
        elif not root.right:
            temp = root.left
            root = None
            return temp
        root.val = min_value_node(root.right).val
        root.right = delete(root.right, root.val)
    return root


if __name__ == "__main__":
    root = Node(7)
    root = insert(root, 3)
    root = insert(root, 2)
    root = insert(root, 4)
    root = insert(root, 9)
    root = insert(root, 6)
    root = insert(root, 8)

    print("Мінімальне зачення в ДДП: ", min_value_node(root).val)
    print("Максимальне зачення в ДДП: ", max_value_node(root).val)
    print("Сума всіх значень в ДДП: ", sum_value_node(root))
