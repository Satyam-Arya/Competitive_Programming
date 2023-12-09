class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def postorderTraversal(root):
    if not root:
        return []

    result = []
    stack = [root]

    while stack:
        current = stack.pop()
        result.insert(0, current.value)  # Insert at the beginning for reverse order

        # Push left and right children to the stack
        if current.left:
            stack.append(current.left)
        if current.right:
            stack.append(current.right)

    return result

# Example usage:
# Construct a sample binary tree
#       1
#      / \
#     2   3
#    / \
#   4   5
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

result = postorderTraversal(root)
print("PostOrder Traversal:", result)
