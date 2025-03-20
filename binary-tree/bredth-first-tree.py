from base_tree import BinaryTree, TreeNode
from collections import deque
from typing import Self


class Solution[T](BinaryTree[T]):
    def __init__(self, root: TreeNode[T]):
        super().__init__(root)

    def pre_order_iterative(self) -> list[T]:
        """Pre order traversal defined as a type of `tree traversal` that 
        follows the `root` -> `left-tree` -> `right-tree` policy where:
        
        - The `root` node of left `subtree` is visited first.
        - Then the left `subtree` is traversed.
        - At last, the right `subtree` is traversed.
        """

        if not self.root:
            return None

        stack: list[TreeNode[T]] = [self.root]
        result: list[T] = []
        while stack:
            current = stack.pop()
            print("data : ", current.data)

            if right := current.right:
                stack.append(right)

            if left := current.left:
                stack.append(left)
        return result

    def post_order_iterative(self):
        """Post order traversal is defined as a type of `tree traversal` that
        follows the `left` -> `right` -> `root` policy where:
        
        - The `left subtree` is traversed first.
        - Then `right subtree` is traversed.
        - Finally, the `root node of the subtree is traversed.
        """

        if not self.root:
            return None

        stack, stack_2 = [self.root], []
        while stack:
            current = stack.pop()
            stack_2.append(current)

            if left := current.left:
                stack.append(left)

            if right := current.right:
                stack.append(right)

        return [node.data for node in stack_2]

    def post_order_iterative_v2(self) -> list[T]:

        if not self.root:
            return None

        stack: list[TreeNode[T]] = []
        current = self.root

        result: list[T] = []
        last_visited: TreeNode[T] | None = None

        while stack or current:
            if current:
                stack.append(current)
                current = current.left
            else:
                peek = stack[-1]
                if peek.right and last_visited != peek.right:
                    current = peek.right
                else:
                    result.append(peek.data)
                    last_visited = stack.pop()
        return result


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
    # print(bft.pre_order_iterative())

    print(bft.post_order_iterative_v2())

    # Visualize the tree structure
    print("\nTree structure:")
    bft.pp_tree()

if __name__ == "__main__":
    main()
