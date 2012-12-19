class Compress(object):
	"""Class Constructor"""
	def __init__(self,):
		self.ratio = 0.0 ## Compression ratio

	def encode(self, text):
		raise NotImplementedError

	def decode(self, text):
		raise NotImplementedError

	def verbose(self, text):
		raise NotImplementedError