#!/usr/bin/env python3

__author__ = "Fabian Golle <me@fabian-golle.de>, Veronika Schoepf <veronika-s@hotmail.de>"
__copyright__ = "Fabian Golle <me@fabian-golle.de>, Veronika Schoepf <veronika-s@hotmail.de>"
__version__ = "0.1"
__revision__ = "f0b3ab7"
__status__ = "Production"

from compression import Compress
from bintree import Node

from collections import Counter
from math import log
import heapq

class Huffman(Compress):
	""" Supplies methods to encode / decode data using huffman-algorithm """
	# Built-in OMEGA Dictionary
	omega = {\
		" ":0.133997441804692,      "´":5.49865771142231e-06,   "^":3.03427330294172e-06, \
		"_":1.50584155626533e-05,   "-":0.00217000342261921,    ",":0.00722946675937681, \
		";":0.000162325920506106,   ":":0.000415536284343302,   "!":1.61211813388105e-05, \
		"?":6.1322098697692e-05,    ".":0.00182721781966793,    '"':0.00116373365902638, \
		"(":0.00126210880413241,    ")":0.00126242712045184,    "{":4.38455059342171e-06, \
		"}":4.48209914292407e-06,   "§":1.35027729047999e-05,   "*":5.47606752101124e-05, \
		"/":0.000168450942588017,   "\\":7.1467147845937e-06,   "&":4.29470324519586e-05, \
		"#":1.02785366370378e-05,   "%":5.87344950687873e-05,   "°":2.77551294005126e-05, \
		"+":1.45501362784041e-05,   "=":3.16570713806069e-05,   "~":2.36683585897823e-06, \
		"$":3.27557760960545e-06,   "0":0.00184490491193296,    "1":0.00282005155410036, \
		"2":0.00116537144783118,    "3":0.000767917584085104,   "4":0.000754892285659447, \
		"5":0.000806172017892581,   "6":0.000673172271847394,   "7":0.000677972687309747, \
		"8":0.000894992539281569,   "9":0.00160293830195946,    "a":0.0442517134967475, \
		"ä":0.0044199504486227,     "A":0.00405886679143845,    "Ä":7.77924011610372e-05, \
		"á":2.87100783587988e-05,   "â":5.93505911709075e-06,   "ã":3.7735886254859e-06, \
		"à":3.19856559684043e-06,   "å":2.89051754578036e-06,   "Á":1.16031432565961e-06, \
		"Å":1.08843644707893e-06,   "b":0.0137559935369055,     "B":0.003763592466229, \
		"c":0.0225711479073824,     "C":0.00104321499318331,    "ç":5.54999905326566e-06, \
		"d":0.0383632979887214,     "D":0.00435996835894712,    "ð":3.79412516222324e-06, \
		"Ð":7.70120127650184e-08,   "e":0.133149056935536,      "E":0.00287459146154055, \
		"é":7.9830652432218e-05,    "è":1.20036057229742e-05,   "ë":3.17802906010309e-06, \
		"É":2.89565167996469e-06,   "ê":2.808371398831e-06,     "f":0.0113837308980944, \
		"F":0.00233172351529157,    "g":0.0219064007497315,     "G":0.00261738674130794, \
		"h":0.0334595580759089,     "H":0.00199846686538641,    "i":0.0660944355801906, \
		"I":0.00193267806994835,    "í":1.84212734533924e-05,   "î":1.25272874097763e-06, \
		"ï":8.88205213889878e-07,   "J":0.00133382752455338,    "j":0.000888379774452146, \
		"k":0.00962843716421479,    "K":0.00267724047762891,    "l":0.0295530826553298, \
		"L":0.00181227748919152,    "m":0.0190864775489857,     "M":0.00296996827228293, \
		"n":0.0796043860045802,     "N":0.00164286646351103,    "ñ":3.92761265101594e-06, \
		"o":0.0223662189414146,     "ö":0.00229521468710676,    "O":0.000918573617590217, \
		"Ö":8.8271169031264e-05,    "ó":1.85085537345261e-05,   "ô":4.95957362206718e-06, \
		"Ó":3.28584587797412e-07,   "ø":6.07368074006778e-06,   "Ø":5.1854755261779e-07, \
		"p":0.00616645454477871,    "P":0.00229404410451274,    "q":0.000162536420007663, \
		"Q":0.000123506731938352,   "r":0.0615366233604502,     "R":0.00200605511571086, \
		"s":0.0477802242269442,     "S":0.00562045477667728,    "ß":0.00137399699041161, \
		"t":0.0501713958819562,     "T":0.00194419906705799,    "u":0.0312255371341452, \
		"ü":0.00453638234365504,    "U":0.000987227259903139,   "Ü":0.000147981149595075, \
		"ú":4.80554959653715e-06,   "v":0.00625188140347185,    "V":0.00178563646690901, \
		"w":0.00999649810975555,    "W":0.00216668677193613,    "x":0.000612147952932394, \
		"X":5.79592408069528e-05,   "y":0.00140278921491736,    "Y":6.74060477061284e-05, \
		"z":0.00885066204249576,    "Z":0.00119139637401157,    "µ":9.75485495023566e-07 \
	}

	buildOwn = True
	entropy = 0
	forrest = []
	codeTranslation = {}
	setown = True

	def encode(self, text):
		""" Encode text using huffman-algorithm """
		if (len(text.strip()) == 0):
			return '';

		if (self.buildOwn == True):
			# Build own OMEGA Tree
			self.generateOmega(text)

		# Convert input text to binary for comparision
		binary_lenght = len(''.join(['%08d'%int(bin(ord(s))[2:]) for s in text]))

		# Build huffman-tree
		self.buildTree()

		# Build Translation Table
		self.buildTranslationTable()

		# Encode input text
		encodedText = ''
		for c in text:
			try:
				encodedText += self.codeTranslation[c]
			except Exception:
				print('The build-in dictionary cannot be used for this input-file because it contains unsupported characters')
				quit()

		huffman_lenght = len(encodedText)
		self.ratio = huffman_lenght/binary_lenght

		return encodedText

	def decode(self, text):
		""" Decode text using huffman-algorithm """
		if (self.buildOwn == True and self.setown != True):
			print('Cannot read input dictionary. Aborting!')
			quit()

		# Build huffman-tree
		self.buildTree()

		nodePointer = self.forrest[0]

		# Decode input binary
		decodedText = ''
		for b in text:
			if (b == "0"):
				# Left
				nodePointer = nodePointer.left
			elif (b == "1"):
				# Right
				nodePointer = nodePointer.right
			if (nodePointer.value != None):
				decodedText += nodePointer.value
				# Reset nodePointer
				nodePointer = self.forrest[0]

		return decodedText

	def generateOmega(self, text):
		""" Generate OMEGA-Dictionary based on input-text """
		charCounter = Counter(text)
		omega = {}
		entropy = 0
		for char, weight in Counter(charCounter).items():
			omega[char] = weight
			entropy += weight/len(text)*log(weight,2)

		self.entropy = entropy*(-1)
		self.omega = omega

	def setOmega(self, omega):
		""" Set / Import OMEGA-Dictionary as dictionary """
		if (type(omega) is not dict):
			raise TypeError
		self.omega = omega
		self.setown = True

	def buildTree(self):
		""" Build huffman-tree using input-text """
		self.forrest = []
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

	def buildTranslationTable(self, node=None, code=''):
		""" Build translation-table based on the huffman-tree """
		if (node == None):
			node = self.forrest[0]

		# Save translation in global translation dictionary
		if (node.value != None):
			self.codeTranslation[node.value] = code

		# Iterate recursively through the left children-tree
		if (node.left != None):
			code += "0"
			self.buildTranslationTable(node.left, code)
			code = code[0:len(code)-1]

		# Iterate recursively through the right children-tree
		if (node.right != None):
			code += "1"
			self.buildTranslationTable(node.right, code)
			code = code[0:len(code)-1]
		return None

	def verbose(self, text=''):
		""" Output verbose information about compression ratio and entropy """
		print('The compression ratio values: '+str(round(float(self.ratio),2))+" %");
		print('The entropy values '+str(self.entropy))