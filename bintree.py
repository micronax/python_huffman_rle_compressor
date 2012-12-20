#!/usr/bin/env python3

__author__ = "Fabian Golle <me@fabian-golle.de>"
__copyright__ = "Fabian Golle <me@fabian-golle.de>"
__version__ = "1.0"
__revision__ = "f0b3ab7"
__status__ = "Production"

class Node(object):
	"""Represents a Node in a binary tree"""

	weight	= 0
	value	= ''
	left	= None
	right	= None


	def __init__(self, value, weight):
		super(Node, self).__init__()
		self.value = value
		self.weight = weight
		
	def is_leaf(self):
		"""Checks, if the current node is a leaf"""
		return ((self.left == None) and (self.right == None))

	def __lt__(self, other):
		"""Performs a real less than comparision between current and other Node"""
		return (self.weight < other.weight)

	def __gt__(self, other):
		"""Performs a real greater than comparision between current and other Node"""
		return (self.weight > other.weight)

	def __eq__(self, other):
		"""Checks, if current Node equals other Node"""
		return (self.weight == other.weight) if (self and other) else False
		
	def __repr__(self):
		return repr(self.value) + ", " + repr(self.weight)

	def __add__ (self, other):
		"""Links two Nodes to a new parent one"""
		if(isinstance(other, Node) == False):
			raise NotImplementedError
		#self.value + other.value
		newNode = Node(None, self.weight + other.weight);
		newNode.left = self;
		newNode.right = other;
		return newNode;

	def traverseTree(self, method='preorder'):
		if (method not in ['preorder', 'inorder', 'postorder', 'front']):
			raise NotImplementedError

		lft = self.left.traverseTree(method) if self.left is not None else [];
		rght = self.right.traverseTree(method) if self.right is not None else [];

		#cur = [self.value, self.weight];
		cur = [self.weight];

		if (method == 'preorder'):
			return cur + lft + rght
		elif (method == 'inorder'):
			return lft + cur + rght
		elif (method == 'postorder'):
			return lft + rght + cur
		elif (method == 'front'):
			return cur if self.is_leaf() == True else [] + lft + rght
