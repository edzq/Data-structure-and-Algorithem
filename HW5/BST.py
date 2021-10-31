# class BSTNode(object):
#     def __init__(self, key, value, left=None, right=None):
#         self.key = key
#         self.lfet = left
#         self.right = right

class Node(object):
    def __init__(self,val=None):
        self.val = val
        self.left = None
        self.right = None
 
def printTree(root):
    if not root :
        return
    print('Binary Tree:')
    printInOrder(root ,0,'Root-',17)
 
def printInOrder(root,height,preStr,length):
    if not root:
        return
    printInOrder(root.right,height+1,'R-',length)
    string = preStr + str(root.val)
    leftLen = (length - len(string))//2
    rightLen = length - len(string) - leftLen
    res = " "*leftLen+string+" "*rightLen
    print(" "*height*length+res)
    printInOrder(root.left,height+1,'L-',length)
 
head = Node('zq')
head.left = Node('geyan')
head.right = Node('beijing')
head.left.left = Node('shanghai')
head.right.left = Node('jiangxi')
head.right.right =  Node('hangzhou')
head.left.left.right = Node('philly')
printTree(head)