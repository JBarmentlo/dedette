class Account(object):
	ID_COUNT = 1

	def __init__(self, name, **kwargs):
		self.id = self.ID_COUNT
		self.name = name
		self.__dict__.update(kwargs)
		if hasattr(self, 'value'):
			self.value = 0
		Account.ID_COUNT += 1

	def transfer(self, amount):
		self.value += amount

# in the_bank.py
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


	def transfer(self, origin, dest, amount):
		"""
		@origin: int(id) or str(name) of the first account
		@dest: int(id) or str(name) of the destination account
		@amount: float(amount) amount to transfer
		@return True if success, False if an error occured
		"""
		raise NotImplementedError


	def fix_account(self, account):
		"""
		fix the corrupted account
		@account: int(id) or str(name) of the account
		@return True if success, False if an error occured
		"""
		raise NotImplementedError
		

b = Bank()
a1 = Account("test")
a2 = Account("test")
b.add(a1)
b.add(a2)

