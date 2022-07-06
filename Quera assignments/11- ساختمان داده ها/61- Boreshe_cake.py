class Node:
    def __init__(self, key):
        self.key = key
        self.skew = 0
        self.height = 0
        self.left = self.right = self.parent = None

    def getParent(self):
        return self.parent

    def setParent(self, parent):
        self.parent = parent

    def setHeight(self, height):
        self.height = height

    def getHeight(self):
        return self.height

    def setSkew(self, skew):
        return self.skew

    def getSkew(self):
        return self.skew

    def getKey(self):
        return self.key

    def setKey(self, key):
        self.key = key

    def setLeft(self, left):
        self.left = left

    def getLeft(self):
        return self.left

    def setRight(self, right):
        self.right = right

    def getRight(self):
        return self.right

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        node = Node(key)
        if self.root is None:
            self.root = node
            return
        #if self.__findNode(self.root, key) is not None:
        #    return

        self.__insertRecursive(self.root, node)

    def __insertRecursive(self, curr, node):
        if node.getKey() < curr.getKey():
            if curr.getLeft() is None:
                node.setParent(curr)
                curr.setLeft(node)
                self.__fix(curr)
                return
            self.__insertRecursive(curr.getLeft(), node)
        else:
            if curr.getRight() is None:
                node.setParent(curr)
                curr.setRight(node)
                self.__fix(curr)
                return
            self.__insertRecursive(curr.getRight(), node)

    def delete(self, key):
        if self.root is None:
            return
        if self.root.getLeft() is None and self.root.getRight() is None and self.root.getKey() == key:
            self.root = None
            return
        node = self.__findNode(self.root, key)
        if node is None:
            return

        self.__deleteRecursive(node)

    def __deleteRecursive(self, node):
        if node.getLeft() is None:
            right = node.getRight()
            self.__mixWithParent(node, right)
        elif node.getRight() is None:
            left = node.getLeft()
            self.__mixWithParent(node, left)
        else:
            succ = self.__getMin(node.getRight())
            node.setKey(succ.getKey())
            self.__deleteRecursive(succ)

    def getMinimum(self):
        if self.root is None:
            return None
        return self.__getMin(self.root).getKey()

    def getMaximum(self):
        if self.root is None:
            return None
        return self.__getMax(self.root).getKey()

    def __getMin(self, curr):
        if curr.getLeft() is None:
            return curr
        return self.__getMin(curr.getLeft())

    def __getMax(self, curr):
        if curr.getRight() is None:
            return curr
        return self.__getMax(curr.getRight())

    def __mixWithParent(self, node, child):
        if node == self.root:
            self.root = child
            self.root.setParent(None)
            return
        parent = node.getParent();
        if parent.getLeft() == node:
            parent.setLeft(child)
        else:
            parent.setRight(child)
        if child is not None: child.setParent(parent)
        self.__fix(parent)

    def __findNode(self, curr, key):
        if curr is None:
            return None
        if curr.getKey() == key:
            return curr
        if curr.getKey() > key:
            return self.__findNode(curr.getLeft(), key)
        else:
            return self.__findNode(curr.getRight(), key)

    def __rotateLeft(self, node):
        right = node.getRight()
        A = node.getLeft();
        B = right.getLeft();
        C = right.getRight()

        x = node.getKey();
        y = right.getKey()

        node.setKey(y);
        right.setKey(x)

        node.setLeft(right);
        right.setParent(node)

        node.setRight(C)
        if C is not None: C.setParent(node)

        right.setLeft(A)
        if A is not None:
            A.setParent(right)

        right.setRight(B)
        if B is not None: B.setParent(right)

        self.__update(right)
        self.__update(node)

    def __rotateRight(self, node):
        left = node.getLeft()
        A = left.getLeft();
        B = left.getRight();
        C = node.getRight()

        x = node.getKey();
        y = left.getKey()

        node.setKey(y);
        left.setKey(x)

        node.setRight(left);
        left.setParent(node)

        node.setLeft(A)
        if A is not None: A.setParent(node)

        left.setLeft(B)
        if B is not None: B.setParent(left)

        left.setRight(C)
        if C is not None: C.setParent(left)

        self.__update(left)
        self.__update(node)

    def __getHeight(self, node):
        if node is None: return -1
        return node.getHeight()

    def __update(self, node):
        node.setSkew(self.__getHeight(node.getRight()) - self.__getHeight(node.getLeft()))
        node.setHeight(max(self.__getHeight(node.getRight()), self.__getHeight(node.getLeft())) + 1)

    def __fix(self, node):
        if node is None: return
        self.__update(node)
        if node.getSkew() == 2:
            if node.getRight().getSkew() == -1: self.__rotateRight(node.getRight())
            self.__rotateLeft(node)
        elif node.getSkew() == -2:
            if node.getLeft().getSkew() == -1: self.__rotateLeft(node.getLeft())
            self.__rotateRight(node)
        self.__fix(node.getParent())

    def minimumNumberGreaterThan(self, key):
        return self.__MNG(self.root, key)

    def __MNG(self, node, key):
        if node is None: return None
        if node.getKey() <= key:
            return self.__MNG(node.getRight(), key)
        else:
            result = self.__MNG(node.getLeft(), key)
            if result is not None:
                return result
            return node.getKey()

    def maximumNumberLessThan(self, key):
        return self.__MNL(self.root, key)

    def has(self, key):
        if self.__findNode(self.root, key) is not None:
            return True
        else:
            return False

    def __MNL(self, node, key):
        if node is None: return None
        if node.getKey() >= key:
            return self.__MNL(node.getLeft(), key)
        else:
            result = self.__MNL(node.getRight(), key)
            if result is not None:
                return result
            return node.getKey()

    def printTree(self):
        self.__print(self.root)
        print()

    def sortedOrder(self):
        if self.root is None: return []
        result = []
        self.__inOrder(self.root, result)
        return result

    def __inOrder(self, node, result):
        if node is None: return
        self.__inOrder(node.getLeft(), result)
        result.append(node.getKey())
        self.__inOrder(node.getRight(), result)

    def __print(self, node):
        if node is None: return
        self.__print(node.getLeft())
        print(node.getKey(), end=" ")
        self.__print(node.getRight())
import string

h,w,n = map(int, input().split())
cuts = [input().translate({ord(c): None for c in string.whitespace}) for i in range(n)]


cutlocs_h = BST()
pieces_h = BST()
cutlocs_w = BST()
pieces_w = BST()

pieces_h.insert(h)
pieces_w.insert(w)
cutlocs_h.insert(0)
cutlocs_h.insert(h)
cutlocs_w.insert(0)
cutlocs_w.insert(w)

for op in cuts:
    ax = int(op[1])
    if op[0] == 'H':
        r = cutlocs_h.minimumNumberGreaterThan(ax)
        if r == None:
            r = h
        l = cutlocs_h.maximumNumberLessThan(ax)
        if l == None:
            l = 0

        pl, pr = ax - l, r - ax

        cutlocs_h.insert(ax)
        pieces_h.delete(r-l)
        pieces_h.insert(pl)
        pieces_h.insert(pr)

    elif op[0] == 'V':
        r = cutlocs_w.minimumNumberGreaterThan(ax)
        if r == None:
            r = w
        l = cutlocs_w.maximumNumberLessThan(ax)
        if l == None:
            l = 0

        pl, pr = ax - l, r - ax

        cutlocs_w.insert(ax)
        pieces_w.delete(r - l)
        pieces_w.insert(pl)
        pieces_w.insert(pr)

    print(pieces_h.getMaximum() * pieces_w.getMaximum())
