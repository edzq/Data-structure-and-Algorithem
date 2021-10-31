import numpy as np
import time


class TreeNode(object):
    # 定义每个节点的数据，左孩子右孩子，平衡因子
    def __init__(self):
        self.key = 0
        self.left = None
        self.right = None
        self.height = 0


class BTree(object):

    def __init__(self):
        self.root = None

    def __Max(self, h1, h2):
        if h1 > h2:
            return h1
        elif h1 <= h2:
            return h2

    # 左左情况，向右旋转
    def __LL(self, r):
        node = r.left
        r.left = node.right
        node.right = r
        r.height = self.__Max(self.getHeight(r.right), self.getHeight(r.left)) + 1
        node.height = self.__Max(self.getHeight(node.right), self.getHeight(node.left)) + 1
        return node

    # 右右，左旋
    def __RR(self, r):
        node = r.right
        r.right = node.left
        node.left = r
        r.height = self.__Max(self.getHeight(r.right), self.getHeight(r.left)) + 1
        node.height = self.__Max(self.getHeight(node.right), self.getHeight(node.left)) + 1
        return node

    # 左右，先左旋再右旋
    def __LR(self, r):
        r.left = self.__RR(r.left)
        return self.__LL(r)

    # 右左，先右旋再左旋
    def __RL(self, r):
        r.right = self.__LL(r.right)
        return self.__RR(r)

    # r是self.root
    def __insert(self, data, r):
        if r == None:
            node = TreeNode()
            node.data = data
            return node
        elif data == r.data:
            return r
        elif data < r.data:
            r.left = self.__insert(data, r.left)
            # 左高右低
            if self.getHeight(r.left) - self.getHeight(r.right) >= 2:
                if data < r.left.data:
                    r = self.__LL(r)
                else:
                    r = self.__LR(r)
        else:
            r.right = self.__insert(data, r.right)
            if self.getHeight(r.right) - self.getHeight(r.left) >= 2:
                if data > r.right.data:
                    r = self.__RR(r)
                else:
                    r = self.__RL(r)

        r.height = self.__Max(self.getHeight(r.left), self.getHeight(r.right)) + 1
        return r

    # 删除data节点
    def __delete(self, data, r):
        if r == None:
            return r

        elif r.data == data:
            # 如果只有右子树，直接将右子树赋值到此节点
            if r.left == None:
                return r.right
            # 如果只有左子树，直接将左子树赋值到此节点
            elif r.right == None:
                return r.left
            # 如果同时有左右子树
            else:
                # 左子树高度大于右子树
                if self.getHeight(r.left) > self.getHeight(r.right):
                    # 找到最右节点 返回节点值 并删除该节点
                    node = r.left
                    while(node.right != None):
                        node = node.right
                    r = self.__delete(node.data, r)
                    r.data = node.data
                    return r
                # 右子树高度大于左子树
                else:
                    node = r.right
                    while node.left != None:
                        node = node.left
                    r = self.__delete(node.data, r)
                    r.data = node.data
                    return r

        elif data < r.data:
            # 在左子树中删除
            r.left = self.__delete(data, r.left)
            # 右子树高度与左子树高度相差超过1
            if self.getHeight(r.right) - self.getHeight(r.left) >= 2:
                if self.getHeight(r.right.left) > self.getHeight(r.right.right):
                    r = self.__RL(r)
                else:
                    r = self.__RR(r)

        elif data > r.data:
            # 右子树中删除
            r.right = self.__delete(data, r.right)
            # 左子树与右子树高度相差超过1
            if self.getHeight(r.left)-self.getHeight(r.right) >= 2:
                if self.getHeight(r.left.right)>self.getHeight(r.left.left):
                    r = self.__LR(r)
                else:
                    r = self.__LL(r)
        # 更新高度
        r.height = self.__Max(self.getHeight(r.left), self.getHeight(r.right))+1
        return r

    # 先序遍历
    def __show(self, root):
        if root != None:
            # print (root.data)
            self.__show(root.left)
            self.__show(root.right)
        else:
            return 0

    def Insert(self, data):
        self.root = self.__insert(data, self.root)
        return self.root

    def Delete(self, data):
        self.root = self.__delete(data, self.root)

    # 求结点的高度
    def getHeight(self, node):
        if node == None:
            return -1
        # print node
        return node.height

    def Show(self):
        self.__show(self.root)

    def Walk(self, root):
        if root != None: 
            self.Walk(root.left) 
            print(root.key)  
            self.Walk(root.right)


if __name__ == '__main__':
    op = BTree()
    root = None
    wordList = ['NIPS', 'EMNLP','NAACL','ICML','KDD','AAAI','ACL','ICCV','CVPR','SIGIR','IJCAI','CIKM','ICDE','WWW']

    for i in wordList:
        root = op.Insert(i)
    
    op.Walk(root)
    



    # insert_time = []
    # delete_time = []
    # for right_interval in range(1000, 500000, 50000):
    #     array = np.random.randint(1, 100, right_interval)
    #     since = time.time()
    #     for i in array:
    #         bi.Insert(i)
    #     end = time.time() - since
    #     insert_time.append(end)
    #     print('AVL insert : ' + str(right_interval) + ' Data: ' + str(end) + 's')

    # for right_interval in range(1000, 500000, 50000):
    #     array = np.random.randint(1, 100, right_interval)
    #     since = time.time()
    #     for i in array:
    #         bi.Delete(i)
    #     end = time.time() - since
    #     delete_time.append(end)
    #     print('AVL delete : ' + str(right_interval) + ' Data: ' + str(end) + 's')
    #     for i in array:
    #         bi.Insert(i)