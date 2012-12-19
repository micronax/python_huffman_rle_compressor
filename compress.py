#!/usr/bin/env python3

__author__ = "Fabian Golle <me@fabian-golle.de>, Veronika Schoepf <veronika-s@hotmail.de>"
__copyright__ = "Fabian Golle <me@fabian-golle.de>, Veronika Schoepf <veronika-s@hotmail.de>"
__version__ = "1.0"
__revision__ = "cf25435f11"
__status__ = "Production"


import argparse
import pickle
import os

try:
	os.system('clear')
except Exception:
	pass                                                                

# compress.py -i[source] -o[target] -c|u[h|r] [-v]
parser = argparse.ArgumentParser(description='Compression Unit')
parser.add_argument('-i','--source', help='Input Filename', required=True)
parser.add_argument('-o','--output', help='Output Filename', required=True)

parser.add_argument('-c','--compression', choices='hr', help='Compression Method', required=False)
parser.add_argument('-u','--uncompression', choices='hr', help='Uncompression Method', required=False)

parser.add_argument('-v','--verbose', help='Verbose output', required=False, action='count')
parser.add_argument('-d','--dictionary', choices='bg', default='g', help='Choose between built-in dictionary or generate own', required=False)

args = vars(parser.parse_args())

if ((args['compression'] == None and args['uncompression'] == None) or (args['compression'] != None and args['uncompression'] != None)):
    parser.error('either -c or -u must be set')

if (args['verbose']):
	print("""
   _____ ____  __  __ _____  _____  ______  _____ _____  ____  _____  
  / ____/ __ \|  \/  |  __ \|  __ \|  ____|/ ____/ ____|/ __ \|  __ \ 
 | |   | |  | | \  / | |__) | |__) | |__  | (___| (___ | |  | | |__) |
 | |   | |  | | |\/| |  ___/|  _  /|  __|  \___  \___ \| |  | |  _  / 
 | |___| |__| | |  | | |    | | \ \| |____ ____) |___) | |__| | | \ \ 
  \_____\____/|_|  |_|_|    |_|  \_\______|_____/_____/ \____/|_|  \_\

COMPRESSION / UNCOMPRESSION SCRIPT FOR EPR_05
(c) 2012 Fabian Golle, Veronika Schoepf. All rights reserved.

-- LET THE FUN START!
""");   


# Read input file
# ================

if (args['verbose']):
	print('Reading input-file...')
inputFile = open ('./'+args['source'], 'r')
inputData = inputFile.read()
inputFile.close()

# Determine compression-method
# =============================

# HUFFMAN-ENCODING
if (args['compression'] == 'h' or args['uncompression'] == 'h'):
	if (args['verbose']):
		print('Encoding-mode is set to HUFFMAN.')
	from huffman import Huffman
	coder = Huffman()

	# Choose built-in omega or generate own?
	if (args['dictionary'] == 'b'):
		if (args['verbose']):
			print('Using build-in dictionary!')
		coder.buildOwn = False
	else:
		if (args['verbose']):
			print('We need to generate / use our own dictionary!')
		if (args['uncompression'] != None):
			try:
				f = open('./'+args['source']+'.huff', 'rb')
				coder.setOmega(pickle.load(f))
			except Exception:
				print('Unable to read huffman-dictionary!')
				print('Please recover it with filename: '+args['source']+'.huff')
				quit()

# RUN-LENGHT-ENCODING
elif (args['compression'] == 'r' or args['uncompression'] == 'r'):
	if (args['verbose']):
			print('Encoding-mode is set to RLE.')
	from rle import RunLenghtEncoding
	coder = RunLenghtEncoding()
else:
	print('ERROR')
	quit()


# COMPRESSION / UNCOMPRESSION
# ============================

# We need to compress
if (args['compression'] != None):
	if (args['verbose']):
		print('Coding-Mode is set to COMPRESSION!')
	outputData = coder.encode(inputData)
	if (args['compression'] == 'h' and args['dictionary'] == 'g'):
		if (args['verbose']):
			print('Dumping huffman-dictionary to file...')
		try:
			f = open('./'+args['output']+'.huff', 'wb')
			pickle.dump(coder.omega, f)
		except Exception:
			print('Error while writing huffman-dictionary to file!')
			quit()
		
# We need to uncompress
elif (args['uncompression'] != None):
	if (args['verbose']):
		print('Coding-Mode is set to UN-COMPRESSION!')
		print('Uncompressing data...')
	outputData = coder.decode(inputData)

# WRITE TO OUTPUT FILE
# =====================
if (args['verbose']):
	print('Writing output to file...')
try:
	f = open("./"+args['output'], "w+")
	try:
		f.writelines(outputData)
	finally:
		f.close()
except IOError:
	print('Error wile writing to output file!')
	quit()

if (args['verbose']):
	if (args['compression'] != None):
		coder.verbose()
	print('EVERYTHING WENT BETTER THAN EXCEPTED!')