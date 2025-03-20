from base_tree import BinaryTree, TreeNode
from typing import Self


class BredthFirstTree(BinaryTree):
    def __init__(self, root: TreeNode):
        super().__init__(root)

    def pre_order_traversal(self) -> Self:
        return self
        ...


def main():
    root = TreeNode(5)
    bft = BredthFirstTree(root)
    bft.pre_order_traversal().pp_tree()


if __name__ == "__main__":
    main()
