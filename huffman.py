#!/usr/bin/env python3

__author__ = "Fabian Golle <me@fabian-golle.de>, Veronika Schoepf <veronika-s@hotmail.de>"
__copyright__ = "Fabian Golle <me@fabian-golle.de>, Veronika Schoepf <veronika-s@hotmail.de>"
__version__ = "0.1"
__revision__ = ""
__status__ = "Production"

from compression import Compress
from collections import Counter
from bintree import Node
import heapq

class Huffman(Compress):
	omega = {}
	forrest = []

	def encode(self, text):
		raise NotImplementedError

	def decode(self, text):
		raise NotImplementedError

	def verbose(self, text):
		raise NotImplementedError

	def setOmega(self, omega):
		 if (type(omega) is not dict):
		 	raise TypeError
		 self.omega = omega

	def buildTree(self):
		lst = []

		# Convert Omega dictionary to list for smarter handling with heapq
		for k in self.omega:
			lst.append([k, self.omega[k]])

		# Create leaf-Nodes for all characters
		for e in lst:
			self.forrest.append(Node(e[0], e[1]))

		heapq.heapify(self.forrest)
		# Build Tree
		while(len(self.forrest) > 1):
			leftNode = heapq.heappop(self.forrest)
			rightNode = heapq.heappop(self.forrest)
			heapq.heappush(self.forrest, leftNode + rightNode)

	def generateCode(self):
		pass