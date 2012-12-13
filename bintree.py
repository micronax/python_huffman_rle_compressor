"""
 _   _           _      
| \ | |         | |     
|  \| | ___   __| | ___ 
| . ` |/ _ \ / _` |/ _ \
| |\  | (_) | (_| |  __/
\_| \_/\___/ \__,_|\___|
                                             
"""

class Node(object):
	"""Stellt einen Knoten in einem Binärbaum dar"""
	def __init__(self, arg):
		super(Node, self).__init__()
		self.arg = arg
		