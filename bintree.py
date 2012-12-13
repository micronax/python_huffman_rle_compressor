#!/usr/bin/env python3

__author__ = "Fabian Golle <me@fabian-golle.de>, Veronika Schoepf <veronika-s@hotmail.de>"
__copyright__ = "Fabian Golle <me@fabian-golle.de>, Veronika Schoepf <veronika-s@hotmail.de>"
__version__ = "0.1"
__revision__ = "f070213204"
__status__ = "Staging"

class Node(object):
	"""Represents a Node in a binary tree"""

	weight	= 0
	value	= ''
	left	= None
	right	= None


	def __init__(self, arg):
		super(Node, self).__init__()
		self.arg = arg
		
	def is_leaf(self):
		"""Checks, if the current node is a leaf"""
		pass;

	def __lt__(self, other):
		"""Performs a real less than comparision between current and other Node"""
		return (self.weight < other.weight)

	def __gt__(self, other):
		"""Performs a real greater than comparision between current and other Node"""
		return (self.weight > other.weight)

	def __eq__(self, other):
		"""Checks, if current Node equals other Node"""
		return (self.weight == other.weight)

	def __add__ (self, other):
		"""Links two Nodes to a new parent one"""
		
		newNode = Node();
		newNode.weight = self.weight + other.weight;
		newNode.value = self.value + other.value;
		newNode.left = self;
		newNode.right = other;
		return newNode;

	def get(self, key):
		""" Get Node Information"""
		if (key == 'weight'):
			return self.weight;
		elif (key == 'value'):
			return self.value;
		else:
			raise NotImplementedError;

	def set(self, key, value):
		""" Set Node Information"""
		if (key == 'weight'):
			self.weight = value;
		elif (key == 'value'):
			self.value = value;
		else:
			raise NotImplementedError;

	def traverseTree(self, method='preorder'):
		if (method not in ['preorder', 'inorder', 'postorder', 'front']):
			raise NotImplementedError

		if (self.left != None):
			lft = getattr(self.left, method);
		if (self.right != None):
			rght = getattr(self.right, method);

		cur = [self.value, self.weight];

		if (method == 'preorder'):
			return cur + lft + rght
		elif (method == 'inorder'):
			return lft + cur + rght
		elif (method == 'postorder'):
			return lft + rght + cur
		elif (method == 'front'):
			return cur if self.is_leaf() else None







