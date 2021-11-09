class Account(object):
	ID_COUNT = 1

	def __init__(self, name, **kwargs):
		self.id = self.ID_COUNT
		self.name = name
		self.__dict__.update(kwargs)
		Account.ID_COUNT += 1


	def transfer(self, amount):
		self.value += amount


	def __eq__(self, other):
		if (type(other) != Account):
			return False

		try:
			return (self.name == other.name or self.id == other.id)
		except:
			return (False)


def is_corrupted(account: Account):
	if (len(account.__dict__) % 2 == 0):
		return True
	zip = True

	attr_names = account.__dict__.keys()

	if ("name" not in attr_names or "id" not in attr_names or "value" not in attr_names):
		return True

	for k in account.__dict__.keys():
		try:
			if (k[0] == "b"):
				return True
		except:
			pass

		try:
			if (k[0:3] == "zip"):
				zip = False
		except:
			pass

		try:
			if (k[0:4] == "addr"):
				zip = False
		except:
			pass
	
	return zip

		

	

class Bank(object):
	"""
	The bank
	"""
	def __init__(self):
		self.accounts = []


	def add(self, account):
		if (len(list(filter(lambda x: x.name == account.name, self.accounts))) == 0):
			self.accounts.append(account)
		else:
			print("Another account with the same name already exists, the account was not added")


	def find_account(self, info):
		try:
			return(self.accounts[self.accounts.index(Account(info, id = info))])
		except:
			return None


	def transfer(self, origin, dest, amount):
		"""
		@origin: int(id) or str(name) of the first account
		@dest: int(id) or str(name) of the destination account
		@amount: float(amount) amount to transfer
		@return True if success, False if an error occured
		"""
		origin = self.find_account(origin)
		dest = self.find_account(dest)
		if (type(origin) != Account or type(dest) != Account):
			return False
		
		self.fix_account(origin)
		self.fix_account(dest)
		if (is_corrupted(origin) or is_corrupted(dest)):
			return False
		if (amount < 0 or amount > origin.value):
			return False

		origin.value -= amount
		dest.value += amount

		return True



	def fix_account(self, account: Account):
		"""
		fix the corrupted account
		@account: int(id) or str(name) of the account
		@return True if success, False if an error occured
		"""
		d = account.__dict__

		if ("value" not in d.keys()):
			account.__setattr__("value", 0)
		
		if ("addr" not in d.keys()):
			account.__setattr__("addr", "lol street")
		
		if ("zip" not in d.keys()):
			account.__setattr__("zip", 72500)

		if ("name" not in d.keys()):
			account.__setattr__("name", "john doe")

		if ("id" not in d.keys()):
			account.__setattr__("name", "john doe")

		key = None
		for k in account.__dict__.keys():
			try:
				if (k[0] == "b"):
					key = k
			except:
				pass
		if (key is not None):
			account.__delattr__(key)

		if (len(d) % 2 == 0):
			if ("zoub" in d):
				account.__delattr__("zoub")
			else:
				account.__setattr__("zoub", "evening out")
