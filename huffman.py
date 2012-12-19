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

	def buildList(self):
		lst = []
		for k in self.omega:
			lst.append([k, self.omega[k]])

		lst = sorted(lst, key=lambda p: p[1])

		print(lst)

		for e in lst:
			self.forrest.append(Node(e[0], e[1]))

		while(len(self.forrest) > 1):
			n1 = self.forrest.pop(0)
			n2 = self.forrest.pop(0)
			n3 = n1 + n2
			self.forrest.append(n3)
			self.forrest = sorted(self.forrest, key=lambda n: n.weight)

		print(self.forrest)