from base_tree import BinaryTree, TreeNode
from collections import deque
from typing import Self


class Solution(BinaryTree):
    def __init__(self, root: TreeNode):
        super().__init__(root)

    def pre_order_iterative(self) -> Self:
        """Pre order traversal defined as a type of `tree traversal` that 
        follows the `root` -> `left-tree` -> `right-tree` policy where:
        
        - The `root` node of left `subtree` is visited first.
        - Then the left `subtree` is traversed.
        - At last, the right `subtree` is traversed.
        """

        if not self.root:
            return None

        queue = [self.root]
        while queue:
            current = queue.pop()
            print("data : ", current.data)

            if right := current.right:
                queue.append(right)

            if left := current.left:
                queue.append(left)
        return self

    def post_order_iterative(self): ...

    def in_order_iterative(self): ...

    def level_order_iterative(self): ...


def main():
    # Create a binary tree:
    #       5
    #      / \
    #     3   7
    #    / \  / \
    #   2  4 6   8

    root = TreeNode(5)

    # Level 1
    root.left = TreeNode(3)
    root.right = TreeNode(7)

    # Level 2
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(8)

    # Create tree and run traversal
    bft = Solution(root)

    print("Pre-order traversal:")
    bft.pre_order_iterative()

    # Visualize the tree structure
    print("\nTree structure:")
    bft.pp_tree()

if __name__ == "__main__":
    main()
