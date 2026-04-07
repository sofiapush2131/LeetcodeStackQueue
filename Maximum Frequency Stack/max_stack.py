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


class FreqStack(object):

    def __init__(self):
        self.counts = {}
        self.shelves = {}
        self.top_shelf = 0

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if val in self.counts:
            self.counts[val] += 1
        else:
            self.counts[val] = 1

        current_freq = self.counts[val]

        if current_freq > self.top_shelf:
            self.top_shelf = current_freq

        if current_freq not in self.shelves:
            self.shelves[current_freq] = Stack()

        self.shelves[current_freq].push(val)


    def pop(self):
        """
        :rtype: int
        """
        target_stack = self.shelves[self.top_shelf]
        val = target_stack.pop()

        self.counts[val] -= 1

        if target_stack.is_empty():
            self.top_shelf -= 1

        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
