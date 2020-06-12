# 1. return a list first element. If the list is empty – raise an exception.
def head(List):
    def judge():
        if List is None:
            print("the List is None")
            raise NameError
        return Node(List.value, None)

    return judge


# 2. return tail of the list
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


# 3. return the length of the List
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


# 4. map the value of the List by rule f
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


# 5. Reduce each value in the linkedlist
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


# 6. return a empty object
def empty():
    return None


# 7. connect List1 and List2.
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


# 8. change the python list to linked list
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


# 9. change linked list to the python list
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


# 10. iterate each value in the List.
def iterator(List):
    cur = List

    def foo():
        nonlocal cur
        if cur is None: raise StopIteration
        tmp = cur.value
        cur = cur.next
        return tmp

    return foo


# 11. connect List1 and List2;
def cons(List1, List2):
    def judge():
        return Node(List1, List2)

    return judge


# 12. natural number sequence below k
def natural_seq(k):
    def judge():
        n = 0
        res = None
        while n <= k:
            res = cons(n, res)()
            n += 1
        return res

    return judge


# 13. Hofstadter Figure-Figure sequences as two mutually recursive functions (s_res and r_res)
# that return two infinite lazy lists
def hofstadter_seq(k):
    def judge():
        n = 0
        s_res = None
        r_res = None
        while n < k:
            if n == 0:
                s_res = cons(0, s_res)()
                r_res = cons(1, r_res)()
            else:
                tmp_s_res = r_res
                for _ in range(n - s_res.value - 1):
                    tmp_s_res = tmp_s_res.next
                tmp_s_value = n - tmp_s_res.value

                tmp_r_res = s_res
                for _ in range(n - r_res.value - 1):
                    tmp_r_res = tmp_r_res.next
                tmp_r_value = n - tmp_r_res.value

                s_res = cons(tmp_s_value, s_res)()
                r_res = cons(tmp_r_value, r_res)()

            n += 1
        return s_res, r_res

    return judge


# define class Node and its properties(value,next),its print format
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
    n1 = Node(4, Node(5, None))
    res = cons(3, n1)
    res1, res2 = hofstadter_seq(3)()
    print(hofstadter_seq(3)())
