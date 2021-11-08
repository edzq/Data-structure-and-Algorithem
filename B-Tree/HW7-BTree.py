
from typing import KeysView


class BTreeNode:
    def __init__(self, leaf=False):
        self.leaf = leaf
        self.keys = []
        self.c = []


class BTree:
    def __init__(self, m):
        self.root = BTreeNode(True)
        self.m = m
        self.max_key = 2 * self.m - 1
        self.max_child = self.max_key + 1

    def BTreePrint(self):
        current = [self.root]
        floor = 0
        while current:
            next_cur = []
            output = ""
            for node in current:
                if node != None and node.c:
                    next_cur.extend(node.c)
                if node != None:
                    output +='[' + ','.join(str(v) for v in node.keys[0:len(node.keys)]) + "] "
            # print(floor)
            
            print('Level ' + str(floor)+ ':' +output)
            floor += 1
            current = next_cur

    # def printTree(self, x, lvl=0):
    #     """
    #     Prints the complete B-Tree
    #     :param x: Root node.
    #     :param lvl: Current level.
    #     """
    #     # print("Level ", lvl, " --> ", len(x.keys), end=": ")
    #     # for i in x.keys:
    #     #     print(i, end=" ")
    #     print(x.keys)
    #     print()
    #     lvl += 1
    #     if len(x.c) > 0:
    #         for i in x.c:
    #             print(i.keys)
    #         #self.printTree()

    def insert(self, k):

        root = self.root
        n = len(root.keys)
        # Full, split child
        if n == 2 * self.m - 1:
            node = BTreeNode()
            self.root = node
            node.c.insert(0, root)
            self.Split(node, 0)
            self.InsertNonFull(node, k)
        else:
            self.InsertNonFull(root, k)

    def InsertNonFull(self, x, k):

        i = len(x.keys) - 1
        # print(k)
        if x.leaf:
            x.keys.append((None, None))
            while i >= 0 and k < x.keys[i]:
                x.keys[i + 1] = x.keys[i]
                i -= 1
            x.keys[i + 1] = k
            
        else:
            while i >= 0 and k < x.keys[i]:
                i -= 1
            i += 1
            if len(x.c[i].keys) == 2 * self.m - 1:
                self.Split(x, i)
                if k > x.keys[i]:
                    i += 1
            self.InsertNonFull(x.c[i], k)

    def Split(self, x, i):
        m = self.m

        #i-th child node of x
        y = x.c[i]
        # new node
        z = BTreeNode(y.leaf)

        x.c.insert(i + 1, z)
        x.keys.insert(i, y.keys[m - 1])
        # for j in range(m - 1):
        #     z.keys[j] = y.keys[m + j]
        z.keys = y.keys[m: (2 * m) - 1]
        y.keys = y.keys[0: m - 1]
        if y.leaf != None:
            z.c = y.c[m: 2 * m]
            y.c = y.c[0: m - 1]

    def Delete(self, x, k):
        
        i = 0
        n = len(x.keys)
        #compare the number of keys 
        while i < n and k > x.keys[i]:
            i += 1
        # case1: Delete leaf
        if x.leaf:
            if i < n and x.keys[i] == k:
                x.keys.pop(i)
                return 
            return 
        
        if len(x.c[i].keys) >= self.m:
            self.Delete(x.c[i], k)
        elif i < n and x.keys[i] == k:
            return self._deleteInternalNode(x, k, i)
        else:
            if i != 0 and i + 2 < len(x.c):
                if len(x.c[i + 1].keys) >= self.m:
                    self._deleteSibling(x, i, i + 1)
                elif len(x.c[i - 1].keys) >= self.m:
                    self._deleteSibling(x, i, i - 1)
                else:
                    self._deleteMerge(x, i, i + 1)

            elif i == 0:
                if len(x.c[i + 1].keys) >= self.m:
                    self._deleteSibling(x, i, i + 1)
                else:
                    self._deleteMerge(x, i, i + 1)
            elif i + 1 == len(x.c):
                if len(x.c[i - 1].keys) >= self.m:
                    self._deleteSibling(x, i, i - 1)
                else:
                    self._deleteMerge(x, i, i - 1)
            self.Delete(x.c[i], k)

    def _deleteInternalNode(self, x, k, i):
        """
        Deletes internal node
        :param x: The internal node in which key 'k' is present.
        :param k: The key to be deleted.
        :param i: The index position of key in the list
        """
        t = self.m
        # Deleting the key if the node is a leaf
        if x.leaf:
            if x.keys[i] == k:
                x.keys.pop(i)
                return
            return

        # Replacing the key with its predecessor and deleting predecessor
        if len(x.c[i].keys) >= t:
            x.keys[i] = self._deletePredecessor(x.c[i])
            return
        # Replacing the key with its successor and deleting successor
        elif len(x.c[i + 1].keys) >= t:
            x.keys[i] = self._deleteSuccessor(x.c[i + 1])
            return
        # Merging the child, its left sibling and the key 'k'
        else:
            self._deleteMerge(x, i, i + 1)
            self._deleteInternalNode(x.c[i], k, self.m - 1)

    def _deletePredecessor(self, x):
        """
        Deletes predecessor of key 'k' which is to be deleted
        :param x: Node
        :return: Predecessor of key 'k' which is to be deleted
        """
        if x.leaf:
            return x.keys.pop()
        n = len(x.keys) - 1
        if len(x.c[n].keys) >= self.m:
            self._deleteSibling(x, n + 1, n)
        else:
            self._deleteMerge(x, n, n + 1)
        self._deletePredecessor(x.c[n])

    def _deleteSuccessor(self, x):
        """
        Deletes successor of key 'k' which is to be deleted
        :param x: Node
        :return: Successor of key 'k' which is to be deleted
        """
        if x.leaf:
            return x.keys.pop(0)
        if len(x.c[1].keys) >= self.m:
            self._deleteSibling(x, 0, 1)
        else:
            self._deleteMerge(x, 0, 1)
        self._deleteSuccessor(x.c[0])

    def _deleteMerge(self, x, i, j):
        """
        Merges the children of x and one of its own keys
        :param x: Parent node
        :param i: The index of one of the children
        :param j: The index of one of the children
        """
        cNode = x.c[i]

        # Merging the x.c[i], x.c[j] and x.keys[i]
        if j > i:
            rsNode = x.c[j]
            cNode.keys.append(x.keys[i])
            # Assigning keys of right sibling node to child node
            for k in range(len(rsNode.keys)):
                cNode.keys.append(rsNode.keys[k])
                if len(rsNode.c) > 0:
                    cNode.c.append(rsNode.c[k])
            if len(rsNode.c) > 0:
                cNode.c.append(rsNode.c.pop())
            new = cNode
            x.keys.pop(i)
            x.c.pop(j)
        # Merging the x.c[i], x.c[j] and x.keys[i]
        else:
            lsNode = x.c[j]
            lsNode.keys.append(x.keys[j])
            # Assigning keys of left sibling node to child node
            for i in range(len(cNode.keys)):
                lsNode.keys.append(cNode.keys[i])
                if len(lsNode.c) > 0:
                    lsNode.c.append(cNode.c[i])
            if len(lsNode.c) > 0:
                lsNode.c.append(cNode.c.pop())
            new = lsNode
            x.keys.pop(j)
            x.c.pop(i)

        # If x is root and is empty, then re-assign root
        if x == self.root and len(x.keys) == 0:
            self.root = new

    @staticmethod
    def _deleteSibling(x, i, j):
        """
        Borrows a key from j'th child of x and appends it to i'th child of x
        :param x: Parent node
        :param i: The index of one of the children
        :param j: The index of one of the children
        """
        cNode = x.c[i]
        if i < j:
            # Borrowing key from right sibling of the child
            rsNode = x.c[j]
            cNode.keys.append(x.keys[i])
            x.keys[i] = rsNode.keys[0]
            if len(rsNode.c) > 0:
                cNode.c.append(rsNode.c[0])
                rsNode.c.pop(0)
            rsNode.keys.pop(0)
        else:
            # Borrowing key from left sibling of the child
            lsNode = x.c[j]
            cNode.keys.insert(0, x.keys[i - 1])
            x.keys[i - 1] = lsNode.keys.pop()
            if len(lsNode.c) > 0:
                cNode.c.insert(0, lsNode.c.pop())


# The main function
def main():
    B = BTree(2)

    # Insert
    # customNo = 10

    NumList = [15,25,30,75,85,90]
    # for i in range(customNo):
    #     B.insert((i, randint(i, 5 * i)))
    for i in NumList:
        B.insert(i)

    #B.printTree(B.root)
    B.BTreePrint()
    #print()

    # Delete
    # toDelete = randint(0, customNo)
    # print("Key {} deleted!".format(toDelete))
    # B.Delete(B.root, (toDelete,))
    # # B.delete(B.root, (4,))
    # B.printTree(B.root)
    # print()

    # # Search
    # toSearch = randrange(0, 2 * customNo)
    # if B.search(toSearch) is not None:
    #     print("Key {} found!".format(toSearch))
    # else:
    #     print("Key {} not found!".format(toSearch))


# Program starts here
if __name__ == '__main__':
    main()