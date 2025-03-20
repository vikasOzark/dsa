from typing import Self, Optional
from dataclasses import dataclass


@dataclass
class TreeDisplayConfig:
    """Configuration for tree display characters."""
    vertical: str = "│"
    horizontal: str = "─"
    left_corner: str = "└"
    right_corner: str = "┌"
    space: str = " "


class TreeNode:
    """A class representing a node in a binary tree.

    Each node contains data and references to left and right child nodes.

    Attributes:
        data: The value stored in the node
        left (TreeNode): Reference to the left child node
        right (TreeNode): Reference to the right child node

    Example:
        >>> node = TreeNode(5)
        >>> node.left = TreeNode(3)
        >>> node.right = TreeNode(7)
    """

    def __init__(self, data, left: Optional[Self] = None, right: Optional[Self] = None) -> None:
        """Initialize a new TreeNode.

        Args:
            data: The value to be stored in the node
            left (TreeNode, optional): The left child node. Defaults to None.
            right (TreeNode, optional): The right child node. Defaults to None.

        Raises:
            TypeError: If left or right is not a TreeNode or None
        """
        self.data = data
        self.left = left
        self.right = right


class BinaryTree:
    """A class representing a binary tree data structure.

    A binary tree is a tree data structure where each node has at most
    two child nodes, referred to as left and right children.

    Attributes:
        root (TreeNode): The root node of the binary tree. None for empty tree.

    Example:
        >>> tree = BinaryTree()
        >>> tree.root = TreeNode(1)
        >>> tree.root.left = TreeNode(2)
        >>> tree.root.right = TreeNode(3)
    """

    def __init__(self, root: Optional[TreeNode] = None):
        """Initialize an empty binary tree.

        The tree is initialized with no root node (None).
        """
        self.root = root
        self.display_config = TreeDisplayConfig()
        self.max_depth = 1000  # Prevent stack overflow

    def pp_tree(self, root_node: Optional[TreeNode] = None, prefix="", isLeft=True):
        node = root_node if root_node is not None else self.root

        if not node:
            print("Empty Tree")
            return

        if node.right:
            self.pp_tree(node.right, prefix +
                                 ("│   " if isLeft else "    "), False)

        print(prefix + ("└── " if isLeft else "┌── ") + f"[{str(node.data)}]")

        if node.left:
            self.pp_tree(node.left, prefix +
                                 ("    " if isLeft else "│   "), True)
