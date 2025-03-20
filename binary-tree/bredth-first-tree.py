from base_tree import BinaryTree, TreeNode
from typing import Self


class BreathFirstTree(BinaryTree):
    def __init__(self, root: TreeNode):
        super().__init__(root)

    def pre_order_iterative(self) -> Self:
        return self

    def post_order_iterative(self): ...

    def in_order_iterative(self): ...

    def level_order_iterative(self): ...


def main():
    root = TreeNode(5)
    bft = BreathFirstTree(root)
    bft.pre_order_traversal().pp_tree()


if __name__ == "__main__":
    main()
