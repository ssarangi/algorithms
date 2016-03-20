class Node:
	def __init__(self, data):
		self.data = data

	def __lt__(self, other):
		return self.data < other.data

	def __str__(self):
		return str(self.data)

	__repr__ = __str__

from random import randint

a = [randint(0, 20) for i in range(0, 20)]

nodes = [Node(i) for i in a]

nodes = sorted(nodes)

print(nodes)


g = [(randint(0, 20), randint(0, 20)) for i in range(0, 20)]

print(g)

lt = lambda x, y: x[0] < y[0]
g = sorted(g, key=lambda x: x[0])

print(g)