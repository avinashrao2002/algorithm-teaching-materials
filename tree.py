import heapq
myHeap = []
# [("build landing page", 1), ("build login", 3), ("build api", 2)]
heapq.heappush(myHeap, (-5, 'write code'))
print(myHeap)
heapq.heappush(myHeap,  (-7,'release product'))
print(myHeap)
heapq.heappush(myHeap, (-1,'write spec'))
print(myHeap)
heapq.heappush(myHeap, (-3,'create tests'))
print(myHeap)

heapq.heap
print(heapq.heappop(myHeap))
print(heapq.heappop(myHeap))
print(heapq.heappop(myHeap))
print(heapq.heappop(myHeap))
# heap cost.
# push -> O(log(n) -> number of layers of the tree/heap)


# lst = [1,2,6,2,4] 
# lst.append(7)
# lst = [1,2,6,2,4,7]
#lst.pop(0) -> 1

#priority:
#lst.pop(0) -> 7
#O(n)

#Appendix
# class Node:
#    def __init__(self, data):
#       self.left = None
#       self.right = None
#       #self.children = [Me, yuhong, nikhil, vinay]
#       self.data = data
#    def PrintTree(self):
#       print(self.data)

# ####
# ####   my boss (fatih)
# ####  |         |
# ####  me        yuhong



# obj = Node("My Boss")
# me = Node("Me")
# obj.left = me
# obj.right = Node("Yuhong")