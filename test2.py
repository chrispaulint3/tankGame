from collections import deque

a = deque([1,2,3])
print(a.popleft())
print(a)

class A:
    def __init__(self):
        self._a = 1

a = A()
print()
