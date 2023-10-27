class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def depth_first_search(root):
    if root is None:
        return

    print(root.value)  # Process the current node

    depth_first_search(root.left)  # Recursively visit the left subtree
    depth_first_search(root.right)  # Recursively visit the right subtree

def main():
    # Create a binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    print("Depth-First Search:")
    depth_first_search(root)

if __name__ == "__main__":
    main()
