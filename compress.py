#!/usr/bin/env python3

__author__ = "Fabian Golle <me@fabian-golle.de>, Veronika Schoepf <veronika-s@hotmail.de>"
__copyright__ = "Fabian Golle <me@fabian-golle.de>, Veronika Schoepf <veronika-s@hotmail.de>"
__version__ = "1.0"
__revision__ = "cf25435f11"
__status__ = "Production"


import argparse
import pickle

# compress.py -i[source] -o[target] -c|u[h|r] [-v]
parser = argparse.ArgumentParser(description='Compression Unit')
parser.add_argument('-i','--source', help='Input Filename', required=True)
parser.add_argument('-o','--output', help='Output Filename', required=True)

parser.add_argument('-c','--compression', choices='hr', help='Compression Method', required=False)
parser.add_argument('-u','--uncompression', choices='hr', help='Uncompression Method', required=False)

parser.add_argument('-v','--verbose', help='Verbose output', required=False)
parser.add_argument('-d','--dictionary', choices='bg', default='g', help='Choose between built-in dictionary or generate own', required=False)

args = vars(parser.parse_args())

if ((args['compression'] == None and args['uncompression'] == None) or (args['compression'] != None and args['uncompression'] != None)):
    parser.error('either -c or -u must be set')

# Example Output
#  'verbose': None,
#  'dictionary': 'g',
#  'output_compression': 'h',
#  'source': 'test.txt', 
#  'output': 'test.out',
#  'input_compression': 'h'

# ==== Process ArgumentParser ====


# Read input file
inputFile = open ('./'+args['source'], 'r')
inputData = inputFile.read()
inputFile.close()

if (args['compression'] == 'h' or args['uncompression'] == 'h'):
	# Huffman
	from huffman import Huffman
	coder = Huffman()
	# Choose built-in omega or generate own?
	if (args['dictionary'] == 'b'):
		coder.buildOwn = False
	else:
		if (args['uncompression'] != None):
			f = open('./'+args['source']+'.huff', 'rb')
			coder.setOmega(pickle.load(f))

elif (args['compression'] == 'r' or args['uncompression'] == 'r'):
	# Run-lenght
	from rle import RunLenghtEncoding
	coder = RunLenghtEncoding()
else:
	print('ERROR')
	quit()

if (args['compression'] != None):
	# We need to compress
	outputData = coder.encode(inputData)
	if (args['compression'] == 'h' and args['dictionary'] == 'g'):
		f = open('./'+args['output']+'.huff', 'wb')
		pickle.dump(coder.omega, f)

elif (args['uncompression'] != None):
	# We need to uncompress
	outputData = coder.decode(inputData)

# Write to output-file
try:
	f = open("./"+args['output'], "w+")
	try:
		f.writelines(outputData)
	finally:
		f.close()
except IOError:
	print('Error wile writing to output file!')
	quit()