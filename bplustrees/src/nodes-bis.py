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
        print(f"Inserting {key}...")
        self.node.keys.append(key)
        self.node.keys.sort()

        if len(self.node.keys) >= self.order:
            self.node = self.split_node(self.node)

    def split_node(self, node: Node) -> Node:
        print("splitting node...")

        midpoint = len(node.keys) // 2
        middlekey = node.keys[midpoint]

        left_node = Node(keys=node.keys[:midpoint])
        right_node = Node(keys=node.keys[midpoint+1:])

        if node == self.node: # node to split is the root
            new_root = Node(keys=[middlekey], children=[left_node, right_node], is_leaf=False)
            return new_root
        else:
            pass

        print("Done...")

        return node


def main() -> None:
    tree = BPlusTree(3)
    tree.insert([5])
    tree.insert([10])
    tree.insert([20])

    print("Final tree:")
    print(tree.node.keys)
    print([childrennode.keys for childrennode in tree.node.children])


if __name__ == "__main__":
    main()
