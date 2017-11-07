'''
This module lists all the basic Linked List interview questions
'''
class Node:
    '''Class to define Linked List Node'''
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        self.child = None

class LinkedList:
    '''Linked List class'''
    def __init__(self):
        self.head = None

    def add(self, data):
        '''Adds a linked list node to the front of the list'''
        node = Node(data)
        if self.head is not None:
            node.next = self.head
            self.head = node
        else:
            self.head = Node(data)

    def reverse(self):
        '''Reverse a Linked List'''
        current = self.head
        prev = None
        while current:
            nxt = current.next
            current.next = prev
            prev, current = current, nxt
        self.head = prev

    def mergesorted(self, list2):
        '''Merge two sorted linked list'''
        list1 = self.head
        mergedlist = dummy = LinkedList()
        while list1 and list2:
            if list1.data < list2.data:
                mergedlist.add(list1.data)
                list1 = list1.next
            else:
                mergedlist.add(list2.data)
                list2 = list2.next
        remnodes = list1 or list2
        while remnodes:
            mergedlist.add(remnodes.data)
            remnodes = remnodes.next
        return dummy

    def getlistlength(self):
        '''Get the length of the linked list'''
        counter = 0
        if hasattr(self, 'head'):
            start = self.head
        else:
            start = self
        if start is not None:
            while start:
                counter += 1
                start = start.next
        return counter

    def printlinkedlist(self):
        '''Print the Linked List'''
        if hasattr(self, 'head'):
            start = self.head
        else:
            start = self
        while start:
            print(start.data, end=' ')
            start = start.next
        print(flush=True)

    def printnthnodefromtail(self, n):
        '''Print the Nth node from the tail of the Linked List'''
        if self.head is not None:
            ptr1 = self.head
            ptr2 = self.head
            while n > 0:
                ptr1 = ptr1.next
                n -= 1
            while ptr1:
                ptr1 = ptr1.next
                ptr2 = ptr2.next
            return ptr2.data
        return -1

    def sort(self):
        '''Given an unsorted list, sort the list'''
        if self.head is not None:
            tmp = []
            root = self.head
            while root:
                tmp.append(root.data)
                root = root.next
            tmp.sort()
            tmplist = LinkedList()
            for v in tmp:
                tmplist.add(v)
            self.head = tmplist.head

    def add2numbers(self, num1):
        '''Given two linked list with numbers, add and return the result in a Linked List'''
        num2 = self.head
        if num1 is None and num2 is None:
            return None
        if num1 is None:
            return num2
        if num2 is None:
            return num1
        result = LinkedList()
        carry = 0
        while num1 or num2:
            num1_val = num1.data if num1 else 0
            num2_val = num2.data if num2 else 0
            add = num1_val + num2_val + carry
            if add >= 10:
                carry = 1
                add = add % 10
            else:
                carry = 0
            result.add(add)
            if num1:
                num1 = num1.next
            if num2:
                num2 = num2.next
        if carry:
            result.add(carry)
        return result

    def detectloop(self):
        '''Given a Linked List, if the list has cycle, return node else return -1'''
        slowptr = self.head
        fastptr = self.head
        while fastptr.next is not None and fastptr.next.next is not None:
            fastptr = fastptr.next.next
            slowptr = slowptr.next
            if fastptr == slowptr:
                return fastptr.data
        return -1

    def removeloop(self):
        '''Given a Linked List with loop, remove the loop'''
        slowptr = self.head
        fastptr = self.head
        while fastptr.next is not None and fastptr.next.next is not None:
            fastptr = fastptr.next.next
            slowptr = slowptr.next
            if fastptr == slowptr:
                break
        ptr = self.head
        while ptr and ptr != fastptr:
            ptr = ptr.next
        ptr.next = None

def test_add_list():
    '''Call to populate a list'''
    root = LinkedList()
    #Add sample nodes to root
    root.add(1)
    root.add(3)
    root.add(2)
    root.printlinkedlist()#prints 2 3 1

def test_print_nth_node_from_tail():
    '''Call to print nth node from tail'''
    root = LinkedList()
    #Add sample nodes to root
    root.add(1)
    root.add(3)
    root.add(2)
    #print nth node from tail of the list
    print(root.printnthnodefromtail(1))#prints 1

def test_reverse_list():
    '''Call to reverse a list'''
    root = LinkedList()
    #Add sample nodes to root
    root.add(1)
    root.add(3)
    root.add(2)
    #reverse list
    root.reverse()
    root.printlinkedlist()#prints 1 3 2

def test_merge_list():
    '''Call to merge two sorted list'''
    #merge 2 sorted lists
    root = LinkedList()
    root.add(3)
    root.add(2)
    root.add(1)
    second_list = Node(4)
    second_list.next = Node(5)
    second_list.next.next = Node(6)
    merged = root.mergesorted(second_list)
    merged.printlinkedlist()#print 6 5 4 3 2 1

def test_sort_list():
    '''Call to sort an unsorted linked list'''
    root = LinkedList()
    root.add(9)
    root.add(4)
    root.add(12)
    root.add(3)
    root.sort()
    root.printlinkedlist()#print 12 9 4 3

def test_add_two_list():
    #add two linked list numbers
    root = LinkedList()
    root.add(1)
    root.add(2)
    root.add(3)
    list2 = LinkedList()
    list2.add(7)
    list2.add(7)
    add_2_nos = root.add2numbers(list2.head)
    add_2_nos.printlinkedlist()#print 200 -> 123 + 77

def test_detect_loop():
    '''Call to detect loop in list'''
    #detect loop in linked list and remove loop
    root = LinkedList()
    l1 = Node(5)
    l2 = Node(4)
    l3 = Node(3)
    l4 = Node(2)
    l5 = Node(1)
    l5.next = l4
    l4.next = l3
    l3.next = l2
    l2.next = l1
    l1.next = l4 #loop creation
    root.head = l5
    print(root.detectloop())#prints 5

def test_remove_loop():
    '''Call to detect loop in linked list and remove loop'''
    root = LinkedList()
    l1 = Node(5)
    l2 = Node(4)
    l3 = Node(3)
    l4 = Node(2)
    l5 = Node(1)
    l5.next = l4
    l4.next = l3
    l3.next = l2
    l2.next = l1
    l1.next = l4 #loop creation
    root.head = l5
    print(root.detectloop())#prints 5
    root.removeloop()
    root.printlinkedlist()#print 1 2 3 4 5

def main():
    '''Entry point to Linked List routine'''
    test_add_list()
    test_print_nth_node_from_tail()
    test_reverse_list()
    test_merge_list()
    test_sort_list()
    test_add_two_list()
    test_detect_loop()
    test_remove_loop()

if __name__ == "__main__":
    main()
