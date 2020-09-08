class MyStack:

    def __init__(self, val=None, next=None):
        """
        Initialize your data structure here.
        """
        # 큐를 이용하기 위해서 큐를 데크자료구조형으로 선
        self.q = collections.deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q.append(x)

        # 요소삽입한 뒤에 삽입한 요소가 가장 앞에 있게하기 위해 정렬
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.q.popleft()

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.q[0]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.q) == 0