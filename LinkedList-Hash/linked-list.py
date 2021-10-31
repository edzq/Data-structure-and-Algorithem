#learn for link
class Node:
    def __init__(self, value):
        self.value =value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.value)
            temp = temp.next


if __name__ == '__main__':
    llinst = LinkedList()

    llinst.head = Node(1)
    second = Node(2)
    third = Node(3)

    llinst.head.next = second
    second.next = third

    llinst.printList()
    