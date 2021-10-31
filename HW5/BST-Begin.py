class BSTCountNode:
    def __init__(self, key = None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
        self.count = 0


class BSTCount():
    def __init__(self):
        self.root = BSTCountNode()
        self.delete_sign = 0

    def Insert(self, key):
        BSTCount.add(self.root, key)

    def add(node, key):
        if node.key == None:
            node.key = key
            node.left = BSTCountNode()
            node.right = BSTCountNode()

        if node.key == key:
            node.count += 1
        
        if node.key > key:
            BSTCount.add(node.left, key)
        
        if node.key < key:
            BSTCount.add(node.right, key)
    
    def Walk(self):
        if self.root.key == None:
            print("None")
        else:
            BSTCount.inorder(self.root)

    def inorder(node):
        if node.key != None:
            BSTCount.inorder(node.left)
            print(node.key, '(',node.count,')')
            BSTCount.inorder(node.right)

    def Search(self, key):
       return BSTCount.find(self.root, key)

    def find(node, key):
        if node.key == None:
            return 0
        
        if key == node.key:
            ret = node.count
            return ret
            
        if key < node.key:
            return BSTCount.find(node.left, key)
        else:
            return BSTCount.find(node.right, key)

    def Print(self):
        if not self.root:
            return
        print('Binary Search Word Tree:')
        #print(self.root)
        BSTCount.PrintInorder(self.root, 0,'Root-',17)

    def PrintInorder(node, height, preString, length):
        if node.key == None:
            return
        BSTCount.PrintInorder(node.right, height + 1, 'R-', length)
        string = preString + str(node.key) + '('+ str(node.count) +')'
        leftLen = (length - len(string)) // 2
        rightLen = length - len(string) - leftLen
        res = " "*leftLen + string + ""*rightLen
        print(" "*height*length+res)
        BSTCount.PrintInorder(node.left, height+1, 'L-', length)

    def Delete(self, key):
        self.delete_sign = 0
        if self.root == None:
            return self.root
        else:
            print('Iam here')
            self.root = self.remove(self.root, key)
        return self.delete_sign



    def remove(self, node, key):
        if key < node.key:
            node.left = self.remove(node.left, key)
            #return BSTCount.remove(node.left, key)
        elif key > node.key:
            node.right = self.remove(node.right, key)
        else:
            if node.count > 1:
                node.count -= 1
                #self.delete_sign = 1
                return node

            if node.left == None:
                temp = node.right
                return temp
            elif node.right == None:
                temp = node.left
                return temp

            temp = BSTCount.minNode(node.right)

            node.key = temp.key

            if temp.key == None:
                return node
            else:
                node.right = self.remove(node.right, temp.key)
            #self.delete_sign = 1
        return node


        # if node.key > key:
            
        
        # if node.key < key:
        #     return BSTCount.remove(node.right, key)

        # if node.key == key:
        #     if node.count > 1:
        #         node.count -= 1
        #         return 1
        #     else:
        #         return 0

    def minNode(node:BSTCountNode):
        current = node

        while current.left != None:
            current = current.left
        return current


if __name__ == '__main__':

    #Operation-3-Insert
    print('Test Insert:')
    WordBST = BSTCount()
    WordBST.Insert('NIPS')
    WordBST.Insert('NIPS')
    WordBST.Insert('NIPS')
    WordBST.Insert('EMNLP')
    WordBST.Insert('NAACL')
    WordBST.Insert('ICML')
    WordBST.Insert('KDD')
    WordBST.Insert('KDD')
    WordBST.Insert('AAAI')
    WordBST.Insert('ACL')
    WordBST.Insert('ACL')
    WordBST.Insert('ACL')
    WordBST.Insert('ACL')
    WordBST.Insert('CVPR')
    WordBST.Insert('ICCV')
    WordBST.Insert('SIGIR')
    WordBST.Insert('SIGIR')
    WordBST.Insert('ICWSM')
    WordBST.Insert('WWW')
    WordBST.Insert('ICDE')
    WordBST.Insert('CIKM')
    WordBST.Insert('IJCAI')

    #Operation-2-Search
    print('Test Search:')
    result = WordBST.Search('ACL')
    print(result)

    print('Test Search:')
    result = WordBST.Search('ada')
    print(result)


    #Operation-5-Walk
    print('Test Walk:')
    WordBST.Walk()

    #Operation-6-Print
    print('Test Print:')
    WordBST.Print()

    #Operation-4-Delete
    WordBST.Walk()
    print('Test Delete:')
    WordBST.Delete('NIPS')
    WordBST.Delete('NIPS')
    WordBST.Delete('NIPS')
    WordBST.Walk()

    # WordBST.Delete('WWW')
    # print(WordBST.delete_sign)
    # print('after delete')
    # WordBST.Walk()

    # print('walk')
    # WordBST.Walk()
    # WordBST.Delete('ACL')
    # print(WordBST.delete_sign)
    # WordBST.Print()

    # WordBST.Delete('ACL')
    # print(WordBST.delete_sign)
    # WordBST.Print()

    # WordBST.Delete('ACL')
    # print(WordBST.delete_sign)
    # WordBST.Print()
    