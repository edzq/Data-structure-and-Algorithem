class AvlTree:

    class Node:
        def __init__(self,val,height=0):
            self.val = val
            self.left = None
            self.right = None
            self.height = height

    def __init__(self,val):
        self.head = self.Node(val)

    def add(self,val):
        cur = self.head
        while True:
            if val > cur.val:
                if not cur.right:
                    cur.right = self.Node(val)
                    break
                else:
                    cur = cur.right
            elif val < cur.val:
                if not cur.left:
                    cur.left = self.Node(val)
                    break
                else:
                    cur = cur.left
            else:
                raise ValueError('Value is exzist')
        self.reBalance()

    def remove(self,num):
        def deleteNode(node):
            if not node.left:
                return node.right
            if not node.right:
                return node.left
            cur = node.right
            while cur.left:
                cur = cur.left
            cur.left = node.left
            return node.right

        def aux(root):
            if not root:
                return None
            if root.val == num:
                return deleteNode(root)
            root.left = aux(root.left)
            root.right = aux(root.right)
            return root

        self.head = aux(self.head)
        self.reBalance()

    def getHiehgt(self):
        def aux(root):
            if not root:
                return 0

            left = aux(root.left)
            right = aux(root.right)
            root.height = max(left,right) + 1
            return root.height
        aux(self.head)

    def currentNodeBalance(self,root):
        if root.left or root.right:
            item = root.right or root.left
            item = item.height
        elif root.left and root.right:
            item = abs(root.left.height - root.right.height)
        else:
            item = 0
        return item <= 1

    def isBalanced(self):
        self.getHiehgt()
        def aux(root):
            if not root:
                return True
            return aux(root.left) and aux(root.right) and self.currentNodeBalance(root)
        return aux(self.head)

    def reBalance(self):

        def balanceCurrentNode(root):
            temp = None
            if not root.left and root.right:
                temp = 'l'
            elif not root.right and root.left:
                temp = 'r'
            else:
                if root.left.height < root.right.height:
                    temp = 'l'
                elif root.left.height > root.right.height:
                    temp = 'r'

            if temp == 'r':
                head = root.left
                root.left = None
                cur = head
                while cur.right:
                    cur = cur.right
                cur.right = root
                return head
            else:
                head = root.right
                root.right = None
                cur = head
                while cur.left:
                    cur = cur.left
                cur.left = root
                return head

        def aux(root):
            if not root:
                return None
            root.left = aux(root.left)
            root.right = aux(root.right)
            if not self.currentNodeBalance(root):
                root = balanceCurrentNode(root)
            return root

        if not self.isBalanced():
            self.getHiehgt()
            self.head = aux(self.head)
            self.getHiehgt()

    def __str__(self):
        def aux(root):
            if not root:
                return ' '
            return aux(root.left) + str(root.val) + aux(root.right)
        return aux(self.head)

if __name__ == '__main__':
    avlTree = AvlTree('ACL')
    avlTree.add('EMNLP')
    avlTree.add('NAACL')
    avlTree.add('KDD')
    avlTree.add('SIGIR')
    avlTree.remove('SIGIR')
    avlTree.add('AAAI')
    avlTree.add('WWW')
    avlTree.add('CVPR')
    avlTree.remove('CVPR')

    print(avlTree)