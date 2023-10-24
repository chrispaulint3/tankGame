from collections import deque

a = deque([1,2,3])
print(a.popleft())
print(a)

class A:
    def __init__(self):
        self._a = 1

    @property
    def get_a(self):
        return self._a

a = A()
a.get_a = 2
print(a.get_a)
