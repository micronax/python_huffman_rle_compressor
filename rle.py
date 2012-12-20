#!/usr/bin/env python3

__author__ = "Fabian Golle <me@fabian-golle.de>"
__copyright__ = "Fabian Golle <me@fabian-golle.de>"
__version__ = "1.0"
__revision__ = "f0b3ab7"
__status__ = "Production"

import re
from compression import Compress

class RunLenghtEncoding(Compress):
	""" Suply methods for compressing / uncompressing text using RLE-Algorithm """
	
	regex_zero	= '^0+'
	regex_one	= '^1+'

	def encode(self, text):
		""" Encode text using RLE-Algorithm """
		if (len(text.strip()) == 0):
			return '';
		# Encode text to binary
		binary = ''.join(['%08d'%int(bin(ord(s))[2:]) for s in text])
		bin_lenght = len(binary)

		output = '';	
		while (len(binary) > 0):
			zero = re.match(self.regex_zero, binary)
			one = re.match(self.regex_one, binary)
			if (zero):
				count = zero.group(0).count('0');
				if (count > 2):
					output += str(count)+'0';
				else:
					output += zero.group(0);
				binary = re.sub(self.regex_zero, '', binary, 1);
			elif(one):
				count = one.group(0).count('1');
				if (count > 2):
					output += str(count)+'1';
				else:
					output += one.group(0);
				binary = re.sub(self.regex_one, '', binary, 1);

		self.ratio = str(len(output) / bin_lenght)
		return output;

	def decode(self, text):
		""" Decode text using RLE-Algorithm """
		output = '';	
		while (len(text) > 0):
			if (text[0] == '1' or text[0] == '0'):
				output += text[0]
				text = text[1:]
			else:
				# Is compressed, need to decode
				output += str(text[1]) * int(text[0])
				text = text[2:]
		# Re-encode to ASCII	
		return ''.join([chr(int(output[i*8:i*8+8],2)) for i in range(0,int(len(output))//8)])

	def verbose(self, text=''):
		""" Print verbose information about encoding process """
		print('The compression ratio values: '+str(round(float(self.ratio),2))+" %");