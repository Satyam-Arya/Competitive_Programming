class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def sumOfLongRootToLeafPath(root):
    def dfs(node, current_path, current_sum):
        nonlocal max_sum, max_path

        if node is None:
            return

        current_path.append(node.value)
        current_sum += node.value

        if node.left is None and node.right is None:
            # If it's a leaf node, check if this path is longer and has a greater sum
            if len(current_path) > len(max_path) or (
                len(current_path) == len(max_path) and current_sum > max_sum):
                max_path = current_path[:]
                max_sum = current_sum

        dfs(node.left, current_path, current_sum)
        dfs(node.right, current_path, current_sum)

        current_path.pop()  # Backtrack: remove the current node from the path

    if root is None:
        return 0

    max_sum = float('-inf')  # Initialize the maximum sum
    max_path = []  # Initialize the maximum path

    dfs(root, [], 0)

    return sum(max_path)

if __name__ == "__main__":
    # Construct a sample binary tree
    root = TreeNode(10)
    root.left = TreeNode(2)
    root.right = TreeNode(10)
    root.left.left = TreeNode(20)
    root.left.right = TreeNode(1)
    root.right.right = TreeNode(-2)
    root.right.right.left = TreeNode(3)
    root.right.right.right = TreeNode(4)

    result = sumOfLongRootToLeafPath(root)
    print("Sum of nodes on the longest path:", result)
