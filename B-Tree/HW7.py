import bisect

class Node(object):
    def __init__(self, values=None, children=None):
        self.parent = None
        self.values = values or []
        self.children = children
       
        if self.children:
            for i in self.children:
                i.parent = self

    def search(self, val):
        i = bisect.bisect_left(self.values, val)
        if (i != len(self.values) and not val < self.values[i]):
            if(self.values[i] == val):
                return (True, self, i) 

        if self.children != None:
            if len(self.children)>= i and self.children[i]:
                return self.children[i].search(val)
        else:
            return (False, self, i)


    def AuxInsert(self, tree, val, position=None, childrenNode=None):
        if position == None:
            position = bisect.bisect_left(self.values, val)

        if len(self.values) < tree.maxLength:
            self.values.insert(position, val)
            
            if childrenNode:
                for i in childrenNode:
                    i.parent = self
                self.children[position:position + 1] = childrenNode
            return True
        
        # current node is full, split it
        self.Split(tree, val, position, childrenNode)
        return True

    def Split(self, tree, values=None, position=None, childrenNode=None):
        if values == None:
            midList = []
        else:
            midList = [values]

        if position == None:
            position = 0

        splitSet = self.values[0:position] + midList + self.values[position:]
        medianPosition = len(splitSet) // 2
        leftSet = splitSet[0:medianPosition]
        medianSet = splitSet[medianPosition]
        rightSet = splitSet[medianPosition + 1:]

        if self.children != None:
            if childrenNode is not None:
                splitChildren = (self.children[0:position] + list(childrenNode) + self.children[position + 1:])
            else:
                splitChildren = self.children
            leftChildren = splitChildren[0:len(leftSet) + 1]
            rightChildren = splitChildren[len(leftSet) + 1:]
        else:
            leftChildren = None
            rightChildren = None

        leftNode = Node(leftSet, leftChildren)
        rightNode = Node(rightSet, rightChildren)

        if self.parent:
            self.parent.AuxInsert(tree, medianSet, None,(leftNode, rightNode))
        else:
            newRoot = Node([ medianSet ], [leftNode, rightNode])
            leftNode.parent = newRoot
            rightNode.parent = newRoot
            tree.root = newRoot
            


    def MinValue(self, position=0):
        if self.children:
            return self.children[position].MinValue()
        return self.values[0], self, 0


    def Delete(self, tree, val, position=None):
        #get position
        if position == None:
            position = bisect.bisect_left(self.values, val)
        
        #delete from leaf Node
        if self.children == None:
            del self.values[position]
            #underflow in leaf node--->re-balance
            if len(self.values) < tree.minLength:
                self.ReBalance(tree)
        else:
            #delete from non-Leaf Node
            separation, node, i = self.MinValue(position + 1)
            self.values[position] = separation
            del node.values[i]
            #underflow in leaf node--->re-balance
            if len(node.values) < tree.minLength:
                node.ReBalance(tree)

    def ReBalance(self, tree):
        rightSibling, leftSibling, indexing = self.Sibling()
        #check non-root Node
        if self.parent == None:
            return
        if self.children == None:
            #re-balance by moving left Sibling
            if leftSibling and len(leftSibling.values) > tree.minLength:
                separation = indexing - 1
                separationValue = self.parent.values[separation]
                self.parent.values[separation] = leftSibling.values[-1]
                del leftSibling.values[-1]
                self.values.insert(0, separationValue)
                return
            #re-balance by moving right Sibling
            elif rightSibling and len(rightSibling.values) > tree.minLength:
                separation = indexing
                separationValue = self.parent.values[separation]
                self.parent.values[separation] = rightSibling.values[0]
                del rightSibling.values[0]
                self.values.append(separationValue)
                return
        #merge
        if leftSibling != None:
            separation = indexing - 1
            leftNode = leftSibling
            rightNode = self
        elif rightSibling != None:
            separation = indexing
            leftNode = self
            rightNode = rightSibling
        separationValue = self.parent.values[separation]
        leftNode.values.append(separationValue)
        leftNode.values.extend(rightNode.values)
        del rightNode.values[:]
        del self.parent.values[separation]
        del self.parent.children[separation + 1]
        if rightNode.children:
            leftNode.children.extend(rightNode.children)
            for i in rightNode.children:
                i.parent = leftNode

        if len(leftNode.values) > tree.maxLength:
            leftNode.Split(tree)

        if len(self.parent.values) < tree.minLength:
            self.parent.ReBalance(tree)     

        if self.parent.parent == None:
            if not self.parent.values:
                tree.root = leftNode
                tree.root.parent = None

    def Sibling(self):

        # root Node without Slibing
        if self.parent == None:
            return (None, None, 0)
        
        rightSibling = None
        leftSibling = None
        for i, j in enumerate(self.parent.children):
            if j == self:
                if (i + 1) < len(self.parent.children):
                    rightSibling = self.parent.children[i + 1]
                if i != 0:
                    leftSibling = self.parent.children[i - 1]
                indexing = i  
                break
        return (rightSibling, leftSibling, indexing)

class BTree(object):

    def __init__(self, order):
        self.root = Node()
        self.order = order
        self.maxLength = order - 1
        self.minLength = self.maxLength // 2
        

    def Insert(self, val):
        # find the leaf node where the value should be added
        found, node, position = self.root.search(val)
        if found:
            print("The key values already exists. Try insert other key!")
            return False
        else:
            return node.AuxInsert(self, val, position, None)

    def Delete(self, val):
        
        found, node, position = self.root.search(val)
        if found:
            return node.Delete(self, val, position)
        else:
            print("The key doesn't exist. Try Delete other key!")
            return False

    def BTreePrint(self):
        current = [self.root]
        floor = 0
        while current:
            next_cur = []
            output = ""
            for node in current:
                if node != None and node.children:
                    next_cur.extend(node.children)
                if node != None:
                    output +='[' + ','.join(str(v) for v in node.values[0:len(node.values)]) + "] "
            
            print('Level ' + str(floor)+ ':' +output)
            floor += 1
            current = next_cur

    def VisHelper(self, values, x=None, l=0):
        if not x:
            x = self.root

        if l > (len(values) - 1):
            values.append(l)
            values[l] = []

        vals = []
        for i in x.values:
            vals.append(i)
        values[l].append(vals)

        l += 1
        if x.children != None:
            for i in x.children:
                self.VisHelper(values, i, l)

    def Visualize(self):
        vals = []
        self.VisHelper(vals)

        spaces = '\t'
        i = len(vals) - 1
        print(" ")
        for level in vals:
            print(spaces * i, end=" ")
            for node in level:
                print(node, spaces * (i + 1), end=" ")
            print()
            i -= 1

if __name__ == '__main__':

    m = int(input("Please input order m:"))
    if m != None:
        op = BTree(m)
    #m = 5
    op = BTree(m)
    NumList = [10,15,20,25,28,30,32,34,42,44,55]
    for i in NumList:
        op.Insert(i)
    op.Visualize()
    print("B-Tree with order m ="+ str(m) +"-------") 
    print("Insert [8, 18, 26, 36, 39, 43]:")
    Numlist2 = [8, 18, 26, 36, 39, 43]
    for i in Numlist2:
        op.Insert(i)
    op.Visualize()
    print("B-Tree with order m ="+ str(m) +"-------")
    print("Insert 37:") 
    op.Insert(37)
    op.Visualize()
    print("B-Tree with order m ="+ str(m) +"-------") 
    print("Insert 12:") 
    op.Insert(12)
    op.Visualize()
    print("B-Tree with order m ="+ str(m) +"-------")
    print("Delerte 44 in a leaf:") 
    op.Delete(44)
    op.Visualize()
    print("B-Tree with order m ="+ str(m) +"-------") 
    print("Delerte 18 in a leaf:") 
    op.Delete(18)
    op.Visualize()
    print("B-Tree with order m="+ str(m) +"-------") 
    print("Delerte 36:") 
    op.Delete(36)
    op.Visualize()
    
    # print("B-Tree with order m ="+ str(m) +"-------")  
    # print("Delerte 36:") 
    # op.Insert(12)
    # op.Visualize()
    # print("B-Tree with order m ="+ str(m) +"-------") 
    # op.Delete(12)
    # op.Visualize()
    # op.Visualize()


    # m = 3
    # op = BTree(m)
    # NumList = [5,10,15,20,30,35,70]
    # for i in NumList:
    #     op.Insert(i)
    # op.Visualize()
    # print("B-Tree with order m ="+ str(m) +"-------") 
    # op.Insert(10)
    # op.Visualize()
    # print("B-Tree with order m ="+ str(m) +"-------") 
    # op.Insert(12)
    # op.Visualize()
    # print("B-Tree with order m ="+ str(m) +"-------")
    # op.Insert(17)
    # op.Visualize()
    # print("B-Tree with order m ="+ str(m) +"-------") 
    # op.Insert(14)
    # op.Visualize()
    # print("B-Tree with order m ="+ str(m) +"-------") 
    # op.Insert(100)
    # op.Visualize()
    # print("B-Tree with order m ="+ str(m) +"-------") 
    # op.Delete(100)
    # op.Visualize()
    # print("B-Tree with order m ="+ str(m) +"-------") 
    # op.Delete(15)
    # op.Visualize()
    # print("B-Tree with order m ="+ str(m) +"-------") 
    # op.Delete(14)
    # op.Visualize()
    # print("B-Tree with order m ="+ str(m) +"-------") 
    # op.Delete(20)
    # op.Visualize()
