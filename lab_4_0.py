class SelfDeque:
    def __init__(self):
        self.deque = []

    def isEmpty(self):
        if self.deque == []:
            return True
        else:
            return False

    def pushR(self, n):
        self.deque.append(n)

    def pushL(self, n):
        self.deque.insert(0, n)

    def popR(self):
        if not self.isEmpty():
            return self.deque.pop()

    def popL(self):
        if not self.isEmpty():
            return self.deque.pop(0)

    def size(self):
        return len(self.deque)

    def outR(self):
        if self.isEmpty():
            return "Empty"
        else:
            return self.deque[len(self.deque) - 1]

    def outL(self):
        if self.isEmpty():
            return "Empty"
        else:
            return self.deque[0]

    def clear(self):
        self.deque.clear()
        print('ok')

class SelfStack:
    def __init__(self) -> None:
        self.stack = []

    def isEmpty(self):
        if self.stack == []:
            return True
        else:
            return False

    def push(self, n):
        self.stack.append(n)
        
    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            print('error')

    def back(self):
        if len(self.stack) > 0:
            print(self.stack[len(self.stack) - 1])
        else:
            print('error')

    def size(self):
        print(len(self.stack))

    def clear(self):
        self.stack.clear()
        print('ok')