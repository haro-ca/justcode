from typing import List


class Node:
    def __init__(self, keys: List = None, children: List = None, is_leaf: bool = True):
        self.keys = keys if keys is not None else []
        self.children = children if children is not None else []
        self.is_leaf = is_leaf


class BPlusTree:
    def __init__(self, order: int):
        self.order = order
        self.node = Node()

    def insert(self, key: List):
        print(f'inserting key {key}')
        leaf = self._find_leaf(self.node, key)
        leaf.keys.append(key)
        leaf.keys.sort()

        if len(leaf.keys) > self.order:
            parent = self._find_parent(self.node, leaf)
            self.split_node(leaf, parent)

    def _find_leaf(self, node: Node, key: List) -> Node:
        # Base case: if a node is a leaf, return it
        if node.is_leaf:
            return node

        # Compare keys to find the correct child
        for i, nodekey in enumerate(node.keys):
            if key < nodekey:
                return self._find_leaf(node.children[i], key)

        # If the key is larger that all previous keys, go to last child
        return self._find_leaf(node.children[-1], key)

    def split_node(self, node: Node, parent: Node = None) -> Node:
        print(f"splitting node with keys {node.keys}")

        midpoint = len(node.keys) // 2
        middlekey = node.keys[midpoint]

        left_node = Node(keys=node.keys[:midpoint], is_leaf=node.is_leaf)
        right_node = Node(keys=node.keys[midpoint + 1 :], is_leaf=node.is_leaf)

        if not node.is_leaf:
            # Assign children to the new nodes if node is not a leaf
            left_node.children = node.children[:midpoint + 1]
            right_node.children = node.children[midpoint + 1:]

        if node == self.node:  # node to split is the root
            self.node = Node(
                keys=[middlekey], children=[left_node, right_node], is_leaf=False
            )
            return self.node
        else:
            parent.keys.append(middlekey)
            parent.keys.sort()

            left_index = parent.children.index(node)
            parent.children[left_index] = left_node
            parent.children.insert(left_index + 1, right_node)

            if len(parent.keys) > self.order:
                grandparent = self._find_parent(self.node, parent)
                self.split_node(node=parent, parent=grandparent)
        return node

    def _find_parent(self, current: Node, target: Node) -> Node:
        if (current.is_leaf) or (target in current.children):
            return current
        for child in current.children:
            parent = self._find_parent(child, target)
            if parent:
                return parent
        return None

    def print_tree(self, node: Node = None, level: int = 0):
        if node is None:
            node = self.node
        print(" " * (level * 4) + f"Level {level} | Keys: {node.keys}")
        for child in node.children:
            self.print_tree(child, level + 1)


def main() -> None:
    tree = BPlusTree(3)
    for key in [5, 10, 20, 21, 22, 6, 23, 7, 24, 25, 26, 27]:
        tree.insert([key])

    print("Final tree structure:")
    tree.print_tree()


if __name__ == "__main__":
    main()
