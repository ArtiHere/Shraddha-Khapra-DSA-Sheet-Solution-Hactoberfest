class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def breadth_first_search(root):
    if root is None:
        return

    queue = [root]

    while queue:
        current_node = queue.pop(0)
        print(current_node.value)

        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)

def main():
    # Create a binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    print("Breadth-First Search:")
    breadth_first_search(root)

if __name__ == "__main__":
    main()
