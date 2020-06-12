# CPO_lab3

Computational Process Organization lab13

## title: Lazy single-linked lists by closures

## list of group members

- Zhentao Liu 

  - ID: 192050212
  - Email : lztkystu@163.com

- Shuo Cui

  -  ID: 192050212
  -  Email:13652027261@163.com

  

## laboratory work number: 1

## variant description

In this variant, we  implement a lazy library for a single-linked list. For that, we use closures. Usage of generators (yieldstatement) or async (async, await statements) is not allowed.



## synopsis 

work of Zhentao Liu &Shuo Cui :

1. implement the following API:
   - head(List) – return a list first element. If the list is empty – raise an exception. Only at this step head element should be evaluated. Each element should be evaluated only one time.
   - tail(List) – return tail of the list.
   - length(List).
   - map(List, Function) and reduce(List, Function, Initial State).
   - mempty().
   - mconcat(List1, List2) – should not force list evaluation.
   - from_list(pythonList) and to_list(List).
   - it should be an iterator.
2. To proof correctness, we write unit tests, properties-based tests.





##  descriptions of  modules

in the module of lazy_single_linked_list: we define the class Node and its main properties;the main properties and method of List



- class Node(object):
      def __init__(self, value, next):
          """node constructor"""
          self.value = value
          self.next = next
- def head(List):return a list first element. If the list is empty – raise an exception.
- def tail(List):return tail of the list.
- def length(List):return the length of the List.
- def map(List,f):map the value of the List by rule f.
- def reduce(List,f,InitialState):reduce each value in the List.
- def empty():return a empty object.
- def mconcat(List1,List2):connect List1 and List2.
- def from_list(pylist):change the python list to linked list.
- def to_list(List):change linked list to the python list.
- def iterator(List):iterate each value in the List.
- def cons(head,tail):connect List1 and List2;
- def natural_seq(k):genetate natural number sequence below k
- def hofstadter_seq(k):Hofstadter Figure-Figure sequences as two mutually recursive functions (s_res and r_res) that return two infinite lazy lists



```
# 1. return a list first element. If the list is empty – raise an exception.
def head(List):
   

# 2. return tail of the list
def tail(List):
   

# 3. return the length of the List
def length(List):
   

# 4. map the value of the List by rule f
def map(List, f):
   

# 5. Reduce each value in the linkedlist
def reduce(List, f, InitialState):
   


# 6. return a empty object
def empty():
    return None


# 7. connect List1 and List2.
def mconcat(List1, List2):
   

# 8. change the python list to linked list
def from_list(pylist):
   


# 9. change linked list to the python list
def to_list(List):
    

# 10. iterate each value in the List.
def iterator(List):

# 11. connect List1 and List2;
def cons(List1, List2):


# 12. natural number sequence below k
def natural_seq(k):


# 13. Hofstadter Figure-Figure sequences as two mutually recursive functions (s_res and r_res)
# that return two infinite lazy lists
def hofstadter_seq(k):


# define class Node and its properties(value,next),its print format
class Node(object):
    def __init__(self, value, next):
        """ node constructor"""
        self.value = value
        self.next = next
```





## conclusion 

After this lab work, we can realize the infinite sequence of expression, like all the natural Numbers (endless), without the need for a really calculated in memory all the natural Numbers (that it was impossible, because the memory is not infinite), which number, but need to calculate to which number, or need what number and calculation to the number (for example, the first 1000).

In large-scale data processing to play the role of delay calculation. When you're dealing with large amounts of data, it's often inconvenient to do it all at once. Lazy sequences solve this problem by deferring the computation to the actual use of the data.
A lazy sequence can be thought of as a "stream" from which to take a drop of water when needed.