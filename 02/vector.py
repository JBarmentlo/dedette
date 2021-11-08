def is_scalar(v):
	return (type(v) == float or type(v) == int)

class Vector():
	def __init__(self, val):
		self.values = val
		self.shape = self.calc_shape()


	def is_col(self):
		r, c = self.shape
		if (c == 1):
			return True
		return False


	def calc_shape(self):
		if (type(self.values[0]) == list):
			row = len(self.values)
			col = 1
		else:
			col = len(self.values)
			row = 1
		return (row, col)


	def dot(self, other):
		if (type(other) != Vector):
			raise ValueError

		out = 0.0
		for s, o in zip(self.values, other.values):
			if (type(s) == float):
				out += s * o
			else:
				out += s[0] * o[0]
		
		return out


	def T(self):
		out = Vector(self.values)
		out.values = []
		for s in self.values:
			if (type(s) == float):
				out.values.append([s])
			else:
				out.values.append(s[0])
		
		out.shape = out.calc_shape()

		return (out)


	def __add__(self, other):
		if (type(other) != Vector):
			raise ValueError
		if (self.shape != other.shape):
			raise(ValueError)
		
		out = Vector(self.values)
		out.values = []
		for s, o in zip(self.values, other.values):
			if (type(s) == float):
				out.values.append(s + o)
			else:
				out.values.append([s[0] + o[0]])

		out.shape = out.calc_shape()
		return out						
		

	def __radd__(self, other):
		return self.__add__(other)


	def __sub__(self, other):
		if (type(other) != Vector):
			raise ValueError
		if (self.shape != other.shape):
			raise(ValueError)
		
		out = Vector(self.values)
		out.values = []
		for s, o in zip(self.values, other.values):
			if (type(s) == float):
				out.values.append(s - o)
			else:
				out.values.append([s[0] - o[0]])

		out.shape = out.calc_shape()
		return out		


	def __rsub__(self, other):
		if (type(other) != Vector):
			raise ValueError
		if (self.shape != other.shape):
			raise(ValueError)
		
		out = Vector(self.values)
		out.values = []
		for s, o in zip(self.values, other.values):
			if (type(s) == float):
				out.values.append(o - s)
			else:
				out.values.append([o[0] - s[0]])

		out.shape = out.calc_shape()
		return out	


	def __truediv__(self, other):
		if (not is_scalar(other)):
			raise(ValueError)
		
		out = Vector(self.values)
		out.values = []
		for s in self.values:
			if (type(s) == float):
				out.values.append(s / other)
			else:
				out.values.append([s[0] / other])

		out.shape = out.calc_shape()
		return out	


	def __rtruediv__(self, other):
		pass


	def __mul__(self, other):
		if (not is_scalar(other)):
			raise(ValueError)
		
		out = Vector(self.values)
		out.values = []
		for s in self.values:
			if (type(s) == float):
				out.values.append(s * other)
			else:
				out.values.append([s[0] * other])

		out.shape = out.calc_shape()
		return out	


	def __rmul__(self, other):
		return (self.mul(other))


	def __str__(self):
		return (f"Vector of shape: {self.shape} and values: {self.values}")


	def __repr__(self):
		return (f"Vector of shape: {self.shape} and values: {self.values}")

		
