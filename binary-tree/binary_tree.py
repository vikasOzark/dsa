from base_tree import BinaryTree, TreeNode
from collections import deque
from typing import TypeVar

T = TypeVar("T")


class SolutionIterative[T](BinaryTree[T]):
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

    def pre_order_recursive(self) -> list[T]:
        if not self.root:
            return []

        def pre_order(root: TreeNode):
            if not root:
                return []

            left = pre_order(root.left)
            right = pre_order(root.right)

            return [root.data] + left + right

        return pre_order(self.root)

    def post_order_iterative(self) -> list[T]:
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

    def post_order_recursive(self) -> list[T]:
        if not self.root:
            return []

        def post_order(root: TreeNode):
            if not root:
                return []

            left = post_order(root.left)
            right = post_order(root.right)

            return [] + left + right + [root.data]

        return post_order(self.root)

    def in_order_iterative(self) -> list[T]:
        """In order traversal is type of traversal which is `left` -> `root` -> `right` where:
        - Traverse `left subtree` first.
        - Then traverse `root of the subtree`.
        - Finally, Traverse `right subtree`. 
        """

        if not self.root:
            return []

        stack = list()
        result: list[T] = []
        current: TreeNode[T] | None = self.root

        while stack or current:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            result.append(current.data)
            current = current.right

        return result

    def in_order_recursive(self) -> list[T]:
        if not self.root:
            return []

        def in_order(root: TreeNode[T]) -> list[T]:
            if not root:
                return []

            left = in_order(root.left)
            right = in_order(root.right)
            return [] + left + [root.data] + right

        return in_order(self.root)

    def level_order_iterative(self) -> list[T]:
        """Level order traversal is a type of traversal where on every iteration we go 
        on every level of the tree and get the data."""

        if not self.root:
            return []

        stack = deque([self.root])
        result = []

        while stack:
            current = stack.popleft()
            result.append(current.data)

            if left := current.left:
                stack.append(left)

            if right := current.right:
                stack.append(right)

        return result

    def level_order_recursive(self) -> list[T]:
        if not self.root:
            return []

        def level_order(root: TreeNode[T], level: int, result: list[list]) -> list[T]:
            if not root:
                return

            if len(result) == level:
                result.append([])

            result[level].append(root.data)
            level_order(root.left, level+1, result)
            level_order(root.right, level+1, result)

        result = []
        level_order(self.root, 0, result)
        return result

    def level_order_recursive_v2(self) -> list[T]:
        if not self.root:
            return

        def level_order_v2(root: TreeNode[T], result: list[T]) -> list[T]:
            if not root:
                return
            result.append(root.data)
            level_order_v2(root.left, result)
            level_order_v2(root.right, result)

        result = []
        level_order_v2(self.root, result)
        return result


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
    bft = SolutionIterative(root)
    # print(bft.pre_order_iterative())

    print(bft.level_order_recursive())
    print(bft.level_order_recursive_v2())

    # Visualize the tree structure
    print("\nTree structure:")
    bft.pp_tree()


if __name__ == "__main__":
    main()
