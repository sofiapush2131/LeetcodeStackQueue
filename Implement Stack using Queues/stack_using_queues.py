class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Queue:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def push(self, item):
        new_node=Node(item)
        if self.head is None:
            self.head =new_node
        else:
            probe=self.head
            while probe.next:
                probe=probe.next
            probe.next=new_node

    def pop(self):
        if self.head is None:
            return
        val = self.head.val
        self.head = self.head.next
        return val

    def peek(self):
        return self.head.val


class MyStack(object):

    def __init__(self):
        self.queue = Queue()


    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        count = 0
        probe = self.queue.head
        while probe:
            count += 1
            probe = probe.next

        self.queue.push(x)

        for _ in range(count):
            old_item = self.queue.pop()
            self.queue.push(old_item)

    def pop(self):
        """
        :rtype: int
        """
        value = self.queue.pop()
        return value

    def top(self):
        """
        :rtype: int
        """
        val = self.queue.peek()
        return val


    def empty(self):
        """
        :rtype: bool
        """
        return self.queue.is_empty()



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
