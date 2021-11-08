class Evaluator():
	def zip_evaluate(coefs, words):
		out = 0
		if (len(coefs) != len(words)):
			return (-1)

		for c, w in zip(coefs, words):
			out += c * len(w)
		
		return (out)


	def enumerate_evaluate(coefs, words):
		out = 0
		if (len(coefs) != len(words)):
			return (-1)

		for ci, w in enumerate(words):
			out += coefs[ci] * len(w)

		return (out)