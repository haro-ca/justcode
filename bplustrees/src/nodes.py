from typing import List


class Node:
    def __init__(self, keys: List = None, children: List = None, is_leaf: bool = True):
        self.keys = keys if keys is not None else []
        self.children = children if children is not None else []
        self.is_leaf = is_leaf


class BPlusTree:
    def __init__(self, order: int):
        self.order = order
        self.root = Node()

    def insert(self, key):
        leaf = self._find_leaf(self.root, key)

        leaf.keys.append(key)
        leaf.keys.sort()

        if len(leaf.keys) >= self.order:
            promoted_key, new_node = self._split_leaf(leaf, key)
            print("splitting node...")

            if self.root == leaf:
                new_root = Node([promoted_key], is_leaf=False)
                new_root.children = [leaf, new_node]
                self.root = new_root

    def _find_leaf(self, node, key):
        if node.is_leaf:
            return node

        for i in range(len(node.keys)):
            if key < node.keys[i]:
                return self._find_leaf(node.children[i], key)

        return self._find_leaf(node.children[-1], key)

    def _split_leaf(self, leaf, key):
        leaf.keys.append(key)
        leaf.keys.sort()

        middle_index = len(leaf.keys) // 2

        right_node = Node(keys=leaf.keys[middle_index:], is_leaf=True)

        leaf.keys = leaf.keys[:middle_index]

        promoted_key = right_node.keys[0]

        return promoted_key, right_node


def main():
    tree = BPlusTree(order=3)

    tree.insert(10)
    tree.insert(5)
    tree.insert(20)  # At this point, splitting isn't handled yet.

    print("Root keys:", tree.root.keys)  # [10]
    print("Leaf keys:", [child.keys for child in tree.root.children])  # [[5], [20]]


if __name__ == "__main__":
    main()
