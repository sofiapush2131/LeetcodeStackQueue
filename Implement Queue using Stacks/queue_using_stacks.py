class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Stack:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def push(self, item):
        self.head = Node(item, next=self.head)

    def pop(self):
        if self.head is None:
            return
        val = self.head.val
        self.head = self.head.next
        return val

    def peek(self):
        return self.head.val

class MyQueue(object):

    def __init__(self):
        self.in_stack = Stack()
        self.out_stack = Stack()


    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.in_stack.push(x)


    def pop(self):
        """
        :rtype: int
        """
        if self.out_stack.is_empty():
            while not self.in_stack.is_empty():
                self.out_stack.push(self.in_stack.pop())

        return self.out_stack.pop()


    def peek(self):
        """
        :rtype: int
        """
        if self.out_stack.is_empty():
            while not self.in_stack.is_empty():
                self.out_stack.push(self.in_stack.pop())

        return self.out_stack.peek()

    def empty(self):
        """
        :rtype: bool
        """
        return self.in_stack.is_empty() and self.out_stack.is_empty()




# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
