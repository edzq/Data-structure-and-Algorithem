class NodeBST:   
    def __init__(self, key):  
        self.key = key 
        self.left = None
        self.right = None
        self.height = 0


class AVLOperation:
    # def __init__(self) -> None:
    #     pass

    def __Max(self, h1, h2):
        if h1 > h2:
            return h1
        elif h1 <= h2:
            return h2
    


    #used for RR case
    def LeftRotation(self, root):
        node = root.right  #set node, which is y in the textbook
        root.right = node.left #turn node's left subtree into root's right subtree
        node.right = root
        root.height = self.__Max(self.TreeHeight(root.right), self.TreeHeight(root.left)) + 1

        return node

    #used for LL case
    def RightRotation(self, root):
        node = root.left
        root.left = node.right
        node.right = root

        root.height = self.__Max(self.TreeHeight(root.right), self.TreeHeight(root.left)) + 1

        return node

    #LR case, left rotation-->right rotation
    def __LR(self, root):
        root.left = self.LeftRotation(root.left)
        return self.RightRotation(root)
    
    #RL case, right rotation --> left rotation
    def __RL(self, root):
        root.right = self.RightRotation(root.right)
        return self.LeftRotation(root)

    def Insert(self, root, key):
        if root == None:
            root = NodeBST(key)
            return root

        elif key == root.key:
            return root
        elif key < root.key:
            root.left = self.Insert(root.left, key)
            if self.TreeHeight(root.left) - self.TreeHeight(root.right) >= 2:
                if key < root.left.key:
                    root = self.RightRotation(root)
                else:
                    root = self.__LR(root)
        else:
            root.right = self.Insert(root.right, key)
            if self.TreeHeight(root.right) - self.TreeHeight(root.left) >= 2:
                if key > root.right.key:
                    root = self.LeftRotation(root)
                else:
                    root = self.__RL(root)
        
        root.height = self.__Max(self.TreeHeight(root.left), self.TreeHeight(root.right)) + 1

        return root
    


    def TreeMinimum(self, root):
        while root.left != None:
            root = root.left
        return root

    def TreeMaxmum(self, root):
        while root.right != None:
            root = root.right
        return root
    
    def TreeHeight(self, root):
        if root is None:
            return -1
        else:
            return root.height
    

    def Walk(self, root):
        if root != None: 
            self.Walk(root.left) 
            print(root.key)  
            self.Walk(root.right)

    def Print(self, root):
        if not root:
            return
        print('Binary Search Word Tree:')
        self.PrintInOrder(root, 0, 'Root-', 17)

    def PrintInOrder(self, node, height, preString, length):
        if node == None:
            return
        self.PrintInOrder(node.right, height + 1, 'R-', length)
        string = preString + str(node.key)
        leftLen = (length - len(string)) // 2
        rightLen = length - len(string) - leftLen
        res = " "*leftLen + string + ""*rightLen
        print(" "*height*length+res)
        self.PrintInOrder(node.left, height+1, 'L-', length)
    


if __name__ == '__main__':

    #Initial BST
    wordList = ['EMNLP', 'ACL','NAACL','COLING','AAAI','SIGKDD','SIGIR','CIKM','ICDE','IJCAI','WWW','ICWSM']
    root = None

    op = AVLOperation()
    for i in wordList:
        root = op.Insert(root, i)
    op.Walk(root)
    op.Print(root)
    


    




