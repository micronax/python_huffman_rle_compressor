#!/usr/bin/env python3


print('Testground EPR_05')
print('Welchen Aufgabenteil moechten Sie testen?');
print('[1|2|3]');
which = input(">> ")

######### AUFGABE 5.2 TESTS #########
if (which == "3"):
	from huffman import Huffman
	from omega import omega
	Huff = Huffman()
	Huff.setOmega(omega)
	Huff.buildList()


######### AUFGABE 5.2 TESTS #########
if (which == "2"):
	from compression import RunLenghtEncoding
	rle = RunLenghtEncoding();

	print('Geben Sie einen Text zum codieren ein!');
	text = input('>> ');
	res = rle.encode(text)

	print("Der Komprimierte Text lautet:")
	print(res)
	print("Der Rück-Kodierte Text lautet:")
	print(rle.decode(res))
	rle.verbose()


######### AUFGABE 5.1 TESTS #########
if (which == "1"):
	from bintree import Node

	# Create Nodes
	n1 = Node('a', 1)
	n2 = Node('b', 2)

	# Create parent Node
	n3 = n1+n2

	# Traverse the tree as postorder
	print(n3.traverseTree('postorder'));