import collections as c

kolejka = c.deque([])


def push(x):
    kolejka.appendleft(x)


def pop():
    kolejka.popleft()


def show():
    print(kolejka)


def clear():
    kolejka.clear()
