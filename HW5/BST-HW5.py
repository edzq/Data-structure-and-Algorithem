class NodeBSTCount:   
    def __init__(self, key):  
        self.key = key 
        self.count = 1
        self.left = None
        self.right = None

class NodeBSTDulplicate:
    def __init__(self,key):
        self.key = key
        self.count = 1
        self.left = None
        self.right = None


class CountOperation:
    def __init__(self) -> None:
        self.DelegeFlag = 0
        self.SearccCounter = 0
    
    def Search(self, root, key):
        if root == None:
            return 0
        if root.key == None:
            return 0
        if key == root.key:
            self.SearccCounter = root.count
            return self.SearccCounter
        
        if key < root.key:
            return self.Search(root.left, key)

        return self.Search(root.right, key)
    
    def Insert(self, root, key):
        if root == None:
            root = NodeBSTCount(key)
            return root

        if key == root.key:
            root.count += 1
            return root
        
        if key < root.key:  
            root.left = self.Insert(root.left, key)  
        else: 
            root.right = self.Insert(root.right, key) 
        
        return root

    def Delete(self, root, key):
        if self.Search(root, key) == 0:
            self.DelegeFlag = 0
        else:
            self.DelegeFlag = 1

        if root == None:
            return 0
        
        if key < root.key:
            root.left = self.Delete(root.left, key)
        elif key > root.key:
            root.right = self.Delete(root.right, key)
        else:
            if root.count > 1:
                root.count -= 1
                return root
            if root.left == None:
                temp = root.right
                #self.DelegeFlag = 1
                return temp
            elif root.right ==None:
                temp = root.left
                #self.DelegeFlag = 1
                return temp
            temp = self.TreeMinimum(root.right)

            root.key = temp.key
            root.right = self.Delete(root.right, temp.key)
        return root

    def Walk(self, root):
        if root != None: 
            self.Walk(root.left) 
            print(root.key,'(', root.count,')')  
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
        string = preString + str(node.key) + '('+ str(node.count) +')'
        leftLen = (length - len(string)) // 2
        rightLen = length - len(string) - leftLen
        res = " "*leftLen + string + ""*rightLen
        print(" "*height*length+res)
        self.PrintInOrder(node.left, height+1, 'L-', length)
    
    def TreeMinimum(self, root):
        while root.left != None:
            root = root.left
        return root


class DuplicateOperation:
    def __init__(self) -> None:
        self.DelegeFlag = 0
        self.SearccCounter = 0
    
    def Search(self, root, key):
        if root == None:
            return 0
        if root.key == None:
            return 0
        if root.key == key:
            self.SearccCounter = 1
            self.SearchCount(root.left, key)
            return self.SearccCounter

        elif key < root.key:
            return self.Search(root.left, key)
        elif key > root.key:
            return self.Search(root.right, key)
    
    def SearchCount(self, root, key):
        if root != None:
            if root.key == key:
                self.SearccCounter += 1
            self.SearchCount(root.left, key)
            self.SearchCount(root.right, key)

    def Insert(self, root, key):
        if root == None:
            root = NodeBSTDulplicate(key)
        elif key <= root.key:
            if key == root.key:
                root.count += 1
            root.left = self.Insert(root.left, key)
        elif key > root.key:
            root.right = self.Insert(root.right, key)
        return root
    
    def Delete(self, root, key):

        if self.Search(root, key) == 0:
            self.DelegeFlag = 0
        else:
            self.DelegeFlag = 1

        if root == None:
            return
        if key < root.key:
            root.left = self.Delete(root.left, key)
        elif key > root.key:
            root.right = self.Delete(root.right, key)
        else:
            if root.count > 1: 
                root.count -= 1

            if root.left and root.right:
                temp = self.TreeMin(root.right)
                root.key = temp.key

                root.right = self.Delete(root.right, temp.key)
            elif root.right == None and root.left == None:
                root = None
            elif root.right == None:
                root = root.left
            elif root.left == None:
                root = root.right
        return root
    

    def Walk(self, root):
        if root == None:
            return
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
    
    def TreeMin(self, root):
        if root.left:
            return self.TreeMin(root.left)
        else:
            return root

    def TreeMax(self, root):
        if root.right:
            return self.TreeMax(root.right)
        else:
            return root


def UserOperations():
    print('Operations Menu:')
    #print("1. Create(option)")
    print("1. Search(word)")
    print("2. Insert(word)")
    print("3. Delete(word)")
    print("4. Walk()")
    print("5. Print()")
    print("6. Exit()")



if __name__ == '__main__':


    print('Select one kind of duplicted words BST a or b:')
    print('a. adding an occurrence counter to each word')
    print('b. allowing duplicated "keys" in the tree')
    print('c. exit()')
    CreateSelection = input('input an operation:\n')
    while CreateSelection != 'c':
        if CreateSelection == 'a':
            op = CountOperation()
            operation = True
            print('Word BST created!')
            break
        elif CreateSelection == 'b':
            op = DuplicateOperation()
            operation = True
            print('Word BST created')
            break
        elif CreateSelection == 'c':
            break
        else:
            print('Invalid input, please  again!')
        CreateSelection = input('Input an Operation:\n')

    
    #Initial BST
    wordList = ['NIPS','NIPS', 'EMNLP','NAACL','ICML','KDD','KDD','AAAI','ACL','ACL','ACL','ICCV','CVPR','SIGIR','IJCAI','CIKM','ICDE','WWW', 'NIPS','ACL']
    root = None

    if operation:
        #Initial BST
        for i in wordList:
            root = op.Insert(root, i)
        UserOperations()
        UserOp = int(input('Choose an Operation:\n'))
        while UserOp != 6:
            if UserOp == 1:
                word = input('Input the English word you want to search:\n')
                print(op.Search(root, word))
            elif UserOp == 2:
                word = input('Input the English word you want to insert:\n')
                op.Insert(root, word)
            elif UserOp == 3:
                word = input('Input the English word you want to delete:\n')
                op.Delete(root, word)
                print(op.DelegeFlag)
            elif UserOp == 4:
                op.Walk(root)
            elif UserOp == 5:
                op.Print(root)
            elif UserOp == 6:
                break
            else:
                print('Invalid input, please check again')
            UserOp = int(input('Choose an Operation:\n'))
        print('Good Bye!-:)')





