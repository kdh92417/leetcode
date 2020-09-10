class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.q = [None] * k
        self.maxlen = k
        self.head = 0
        self.tail = 0

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.q[self.tail] is None:
            self.q[self.tail] = value
            self.tail = (self.tail + 1) % self.maxlen
            return True
        else:
            return False

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.q[self.head] is None:
            return False
        else:
            self.q[self.head] = None
            self.head = (self.head + 1) % self.maxlen
            return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        return -1 if self.q[self.head] is None else self.q[self.head]

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """

        return -1 if self.q[self.tail - 1] is None else self.q[self.tail - 1]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.q[self.head] == None and self.q[self.tail] == None

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return None not in self.q