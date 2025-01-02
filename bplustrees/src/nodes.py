from typing import List

class Nodes:
    def __init__(self, keys: List = None, children: List = None, is_leaf: bool = True):
        self.keys = keys if keys is not None else []
        self.children = children if children is not None else []
        self.is_leaf = is_leaf


