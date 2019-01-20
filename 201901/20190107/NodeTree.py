class Node:
    def __init__(self, elem, lchild=None, rchild=None):
        self.name = elem
        self.rchild = rchild
        self.lchild = lchild

class NodeTree:
    def __init__(self):
        self._node = None
    def append(self, elem):
        if self._node is None:
            self._node = Node(elem)
            return
        node = self._node
        L = []
        while node is not None:
            if node.lchild is None:
                node.lchild = Node(elem)
                break
            if node.rchild is None:
                node.rchild = Node(elem)
                break
            L.append(node.lchild)
            L.append(node.rchild)
            node = L.pop(0)
    def traverse(self):
        """层次遍历"""
        if self._node is None:
            return []
        L = []
        Lnode = [self._node]
        while Lnode != []:
            node = Lnode.pop(0)
            L.append(node.name)
            if node.lchild is not None:
                Lnode.append(node.lchild)
            if node.rchild is not None:
                Lnode.append(node.rchild)
        return L
    def ftraverse(self, node):
        """先序遍历"""
        if node is None:
            return []
        L = []
        pl = self.ftraverse(node.lchild)
        pr = self.ftraverse(node.rchild)
        L.append(node.name)
        return L + pl + pr
    def mtraverse(self, node):
        """中序遍历"""
        if node is None:
            return  []
        L = []
        pl = self.mtraverse(node.lchild)
        pr = self.mtraverse(node.rchild)
        L.append(node.name)
        return pl + L + pr
    def ltraverse(self, node):
        """后序遍历"""
        if node is None:
            return []
        L = []
        pl = self.ltraverse(node.lchild)
        pr = self.ltraverse(node.rchild)
        L.append(node.name)
        return pl + pr + L

import string
L = [i for i in string.ascii_uppercase]
nodetree = NodeTree()
print(L)
for i in L:
    nodetree.append(i)
print('层次遍历:', nodetree.traverse())
print('先序遍历:', nodetree.ftraverse(nodetree._node))
print('中序遍历:', nodetree.mtraverse(nodetree._node))
print('后序遍历:', nodetree.ltraverse(nodetree._node))
