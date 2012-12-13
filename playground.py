#!/usr/bin/env python3

from bintree import Node


n1 = Node('a', 1)
n2 = Node('b', 2)

n3 = n1+n2

print(n3.traverseTree('postorder'));