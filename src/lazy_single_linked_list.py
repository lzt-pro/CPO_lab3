def head(List):
    def judge():
        if List is None:
            print("the List is None")
            raise NameError
        return Node(List.value, None)

    return judge


def tail(List):
    def judge():
        if List is None:
            return "the List is None"
        elif List:
            cur = List
            while cur.next is not None:
                cur = cur.next
            return cur
        return "the List is empty"

    return judge


def length(List):
    def judge():
        if List is None:
            return 0
        cur = List
        k = 1
        while cur.next is not None:
            cur = cur.next
            k += 1
        return k

    return judge


def map(List, f):
    def judge():
        if List is None:
            return "List is None"
        else:
            cur = List
            while cur is not None:
                cur.value = f(cur.value)
                cur = cur.next
        return List

    return judge


def reduce(List, f, InitialState):
    def judge():
        if List is None:
            return None
        else:
            state = InitialState
            cur = List
            while cur is not None:
                if cur.value is None:
                    state = f(0, state)
                else:
                    state = f(cur.value, state)
                cur = cur.next
        return state

    return judge


def empty():
    return None


def mconcat(List1, List2):
    def judge():
        if List1 is None:
            if List2 is None:
                return None
            return List2
        else:
            cur = tail(List1)
            cur().next = List2
            return List1

    return judge


def from_list(pylist):
    def judge():
        res = None
        for e in pylist:
            if res is None:
                res = Node(e, None)
                cur = res
            else:
                cur.next = Node(e, None)
                cur = cur.next
        return res

    return judge


def to_list(List):
    def judge():
        res = []
        if list is None:
            return "List is None"
        cur = List
        while cur is not None:
            res.append(cur.value)
            cur = cur.next
        return res

    return judge


def iterator(lst):
    cur = lst

    def foo():
        nonlocal cur
        if cur is None: raise StopIteration
        tmp = cur.value
        cur = cur.next
        return tmp

    return foo


class Node(object):
    def __init__(self, value, next):
        """ node constructor"""
        self.value = value
        self.next = next

    def __str__(self):
        if type(self.next) is Node:
            return "{} -> {}".format(self.value, self.next)
        return str(self.value)

    def __eq__(self, other):
        """for write assertion, we should be abel for check list equality (list are equal, if all elements are equal)."""
        if other is None:
            return False
        if self.value != other.value:
            return False
        return self.next == other.next


if __name__ == '__main__':
    n1 = Node(1, Node(2, None))
    n2 = None
    func1 = tail(n1)
    List1 = Node(1, Node(2, None))
    List2 = None
    List3 = Node(5, None)
    print(mconcat(List1, List3)())
    # print(func1())
    # list = [1, 2, 3, 4]
    # func2 = to_list(n1)
    # print(func2())
    # print(type(n1.value))
    # func2 = head(n2)
    # print(func2())
