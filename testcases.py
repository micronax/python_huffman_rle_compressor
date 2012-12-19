#!/usr/bin/env python3

__author__ = "Fabian Golle <me@fabian-golle.de>, Veronika Schoepf <veronika-s@hotmail.de>"
__copyright__ = "Fabian Golle <me@fabian-golle.de>, Veronika Schoepf <veronika-s@hotmail.de>"
__version__ = "1.0"
__revision__ = "f0b3ab7"
__status__ = "Production"

def abort(message):
	print(message)
	quit()

try:
	from huvorffman import Huffman
	from rle import RunLenghtEncoding
except Exception:
	abort('Import-failure')


testcases = [
	'abcdefghijklmnopqrstuvwxyz',
	'äüöß',
	'!"§$%&/()=?=)(/&%$§"',
	'¡“¶¢[]|{}≠¿',
	'1234567890',
];

i = 0
for t in testcases:
	try:
		huff = Huffman()
		rl = RunLenghtEncoding()

		encoded = huff.encode(t)
		if (t != huff.decode(encoded)):
			raise Exception

		encoded = rl.encode(t)
		decoded = rl.decode(encoded)
		if (t != decoded):
			raise Exception
			
	except Exception as e:
		print("Testcase failed!")
		print("Input: "+str(t))
		print("Output: "+str(decoded))
		if (len(str(e)) > 0):
			print('Exception: ' + str(e))
	else:
		i += 1

print(str(i)+' of '+str(len(testcases))+' Testcases succeed')