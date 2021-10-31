
from random import randint


class Node:
    def __init__(self, word: str=None, left=None, right=None) -> None:
        self.word: str = word
        self.left:Node = left
        self.right:Node = right



    # def __init__(self, word: str=None, left=None, right=None) -> None:
    #     super().__init__(word=word, left=left, right=right)

    #     self.count = 0

class NodeDupCount:
    def __init__(self, word: str=None, left=None, right=None) -> None:
        self.word: str = word
        self.left = left
        self.right = right
        self.count = 1

class BSTDupCount():
    def __init__(self) -> None:
        self.root: NodeDupCount = NodeDupCount()


    def insert(self, word: str) -> int:
        BSTDupCount.insert_aux(self.root, word)

    @staticmethod
    def insert_aux(node: NodeDupCount, word: str):
        if node.word == None:
            node.word = word
            node.left = NodeDupCount()
            node.right = NodeDupCount()
        elif word == node.word:
            node.count += 1
        elif word < node.word:
            BSTDupCount.insert_aux(node.left, word)
        elif word > node.word:
            BSTDupCount.insert_aux(node.right, word)

    def search(self, word: str) -> int:
        return BSTDupCount.search_aux(self.root, word)

    @staticmethod
    def search_aux(node: NodeDupCount, word: str) -> int:
        if node.word == None:
            return 0
        elif word == node.word:
            return node.count
        elif word < node.word:
            return BSTDupCount.search_aux(node.left, word)
        else:
            return BSTDupCount.search_aux(node.right, word)

    def delete(self, word: str) -> int:
        return BSTDupCount.delete_aux(self.root, word)

    @staticmethod
    def delete_aux(node: NodeDupCount, word: str) -> int:
        if node.word == None:
            return 0
        elif word == node.word:
            if node.count > 0:
                node.count -= 1
                return 1
            else:
                return 0
        elif word < node.word:
            return BSTDupCount.delete_aux(node.left, word)
        elif word > node.word:
            return BSTDupCount.delete_aux(node.right, word)

    def walk(self):
        BSTDupCount.walk_aux(self.root)

    @staticmethod
    def walk_aux(node: NodeDupCount):
        if node.word == None:
            return
        
        if node.left != None:
            BSTDupCount.walk_aux(node.left)
        if node.count > 0:
            print("%s(%d)" % (node.word, node.count))
        if node.right != None:
            BSTDupCount.walk_aux(node.right)

    def print(self):
        BSTDupCount.print_aux(self.root, 0)

    @staticmethod
    def print_aux(node: NodeDupCount, depth: int):
        if node.word == None:
            print(" " * depth + "None")
            return

        print(" " * depth + node.word + "(" + str(node.count) + ")")
        BSTDupCount.print_aux(node.left, depth+2)
        BSTDupCount.print_aux(node.right, depth+2)


class BSTDupKey():
    def __init__(self) -> None:
        self.root: Node = Node()
        
        self.delete_flag = 0
        self.walking_word = None
        self.walking_count = 0


    def search(self, word: str) -> int:
        return  BSTDupKey.search_aux(self.root, word)

    @staticmethod
    def search_aux(node: Node, word: str) -> int:
        if node == None:
            return 0
        elif word == node.word:
            count = 1
            if node.left != None:
                count += BSTDupKey.search_aux(node.left, word)
            if node.right != None:
                count += BSTDupKey.search_aux(node.right, word)
            return count
        elif word < node.word:
            return BSTDupKey.search_aux(node.left, word)
        else:
            return BSTDupKey.search_aux(node.right, word)

    def insert(self, word: str):
        r"""
        repeat keys can be inserted in either left or right
        this makes the tree more ballanced
        when the number of repeated keys is large
        """
        if self.root.word == None:
            self.root.word = word
        else:
            BSTDupKey.insert_aux(self.root, word)

    @staticmethod
    def insert_aux(node: Node, word: str):
        if word == node.word:
            # try to make the tree somehow balanced
            if node.left == None:
                node.left = Node(word, None, None)
            elif node.right == None:
                node.right = Node(word, None, None)
            else:
                if word == node.left.word and word == node.right.word: 
                    insert_left = randint(0, 1)
                    if insert_left == 1:
                        BSTDupKey.insert_aux(node.left, word)
                    else:
                        BSTDupKey.insert_aux(node.right, word)
                elif word == node.left.word and word != node.right.word:
                    node.right = Node(word, None, node.right)
                elif word != node.left.word and word == node.right.word:
                    node.left = Node(word, node.left, None)
                else:
                    insert_left = randint(0, 1)
                    if insert_left == 1:
                        node.left = Node(word, node.left, None)
                    else:
                        node.right = Node(word, None, node.right)
        elif word < node.word:
            if node.left == None:
                node.left = Node(word, None, None)
            else:
                BSTDupKey.insert_aux(node.left, word)
        elif word > node.word:
            if node.right == None:
                node.right = Node(word, None, None)
            else:
                BSTDupKey.insert_aux(node.right, word)

    def delete(self, word: str) -> int:
        self.delete_flag = 0

        if self.root.left == None and self.root.right == None:
            if self.root.word == word:
                self.root.word = None
                self.delete_flag = 1
        else:
            self.root = self.delete_aux(self.root, word)

        return self.delete_flag

    def delete_aux(self, node: Node, word: str) -> Node:
        if node == None:
            return None
        if word == node.word:
            if node.left == None:
                self.delete_flag = 1
                return node.right
            elif node.right == None:
                self.delete_flag = 1
                return node.left
            else:
                # balanced deletion
                if word == node.left.word and word == node.right.word:
                    delete_left = randint(0, 1)
                    if delete_left == 1:
                        node.left = self.delete_aux(node.left, word)
                    else:
                        node.right = self.delete_aux(node.right, word)
                    self.delete_flag = 1
                elif word == node.left.word:
                    node.left = self.delete_aux(node.left, word)
                elif word == node.right.word:
                    node.right = self.delete_aux(node.right, word)
                else:
                # delete current node by setting it as right_min
                    right_min = node.right
                    if right_min.left == None:
                        node.word = right_min.word
                        node.right = right_min.right
                    else:
                        while right_min.left.left != None:
                            right_min = right_min.left
                        node.word = right_min.left.word
                        right_min.left = right_min.left.right
                    self.delete_flag = 1
        elif word < node.word:
            node.left = self.delete_aux(node.left, word)
        elif word > node.word:
            node.right = self.delete_aux(node.left, word)

        return node

    def walk(self):
        if self.root.word == None:
            print("None")
        else:
            BSTDupKey.walk_aux(self.root)

    @staticmethod
    def walk_aux(node: Node):
        print(node.word)
        if node.left != None:
            BSTDupKey.walk_aux(node.left)
        if node.right != None:
            BSTDupKey.walk_aux(node.right)

    def print(self):
        if self.root.word == None:
            print("None")
        else:
            BSTDupKey.print_aux(self.root, 0)

    @staticmethod
    def print_aux(node: Node, depth: int):
        if node == None:
            print(" " * depth + "None")
        else:
            print(" " * depth + node.word)
            BSTDupKey.print_aux(node.left, depth+2)
            BSTDupKey.print_aux(node.right, depth+2)


def display_menu():
    print("Operation Menu:")
    print("1. Create")
    print("2. Search")
    print("3. Insert")
    print("4. Delete")
    print("5. Walk")
    print("6. Print")
    print("7. Exit")

if __name__ == "__main__":


    BST = BSTDupKey()
    wordList = ['NIPS', 'NIPS','NIPS', 'EMNLP','NAACL','ICML','KDD','KDD','AAAI','ACL','ACL','ACL','ACL','ICCV','CVPR','SIGIR','IJCAI','CIKM','ICDE','WWW']
    for i in wordList:
        root = BST.insert(i)
    BST.walk()
    BST.print()
    print(BST.search('ICML'))
    print(BST.delete('ICML'))
    BST.print()
    BST.delete('NIPS')
    BST.delete('NIPS')
    BST.delete('NIPS')
    BST.walk()
    BST.print()
    # bst = None
    # display_menu()
    # userChoice = int(input("Choose an operation:\n"))
    # while userChoice != 7:
    #     if userChoice == 1:
    #         tree_type = input("Please choose the tree type:\n" + 
    #                           "0.Repeat by count\n" + 
    #                           "1.Repeat by key\n")
        #     tree_type = int(tree_type)
        #     bst = BSTDupCount() if tree_type == 0 else BSTDupKey()
        #     print("BST created.")
        # elif userChoice == 2:
        #     word = input("Input the word to search:\n")
        #     print(bst.search(word))
        # elif userChoice == 3:
        #     word = input("Input the word to insert:\n")
        #     bst.insert(word)
        # elif userChoice == 4:
        #     word = input("Input the word to delete:\n")
        #     print(bst.delete(word))
        # elif userChoice == 5:
        #     bst.walk()
        # elif userChoice == 6:
        #     bst.print()
        # elif userChoice == 7:
        #     break
        # else:
        #     print("Invalid choice.")
        
        # userChoice = int(input("Choose an operation:\n"))
