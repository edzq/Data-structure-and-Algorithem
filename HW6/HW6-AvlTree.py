class Node:   
    def __init__(self, key):  
        self.key = key 
        self.left = None
        self.right = None
        self.height = 0

class AvlTree():
    def TreeHeight(self, root):
        if not root:
            return 0
        else:
            return root.height
    
    def Insert(self, root, key):
        if not root:
            return Node(key)
        
        #cur = root
        while True:
            if key > root.key:
                if not root.right:
                    root.right = Node(key)
                    break
                else:
                    root = root.right
            elif key < root.key:
                if not root.left:
                    root.left = Node(key)
                    break
                else:
                    root = root.left
            else:
                raise ValueError('Value is exist')
        
        self.reBalance(root)
    
    def getHeight(self, root):
        def aux(root):
            if not root:
                return 0
            left = aux(root.left)
            right = aux(root.right)
            root.height = max(left, right) + 1
            return root.height
        aux(root)

    def currentBalance(self, root):
        if root.left or root.right:
            temp = root.right or root.left
            temp = temp.height
        elif root.left and root.right:
            temp = abs(root.left.height - root.right.height)
        else:
            temp = 0
        return temp <= 1
        
    
    def isBalance(self, root):
        self.getHeight(root)
        def aux(root):
            if not root:
                return True
            return aux(root.left) and aux(root.right) and self.currentBalance(root)
        return aux(root)


    def reBalance(self, root):
        def balanceCurrentTree(root):
            temp = None
            if not root.left and root.right:
                temp = 'l'
            


            
