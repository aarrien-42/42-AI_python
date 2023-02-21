
class Account(object):

	ID_COUNT = 1

	def __init__(self, name, **kwargs):
		self.__dict__.update(kwargs)
		self.id = self.ID_COUNT
		Account.ID_COUNT += 1
		self.name = name
		if not hasattr(self, 'value'):
			self.value = 0
		if self.value < 0:
			raise AttributeError("Attribute value cannot be negative.")
		if not isinstance(self.name, str):
			raise AttributeError("Attribute name must be a str object.")
	def transfer(self, amount):
		self.value += amount

def check_corrupted(account):
	key_count = 0
	za = 0
	for key in account.__dict__.keys():
		key_count += 1
		if key.startswith('b'):
			return True
		if key.startswith('zip') == True or key.startswith('addr') == True:
			za = 1
	if za == 0:
		return True
	if not hasattr(account, 'name'):
		return True
	elif type(account.__dict__['name']) != str:
		return True
	if not hasattr(account, 'id'):
		return True
	elif type(account.__dict__['id']) != int:
		return True
	if not hasattr(account, 'value'):
		return True
	elif type(account.__dict__['value']) != int and type(account.__dict__['value']) != float :
		return True
	if key_count%2 == 0:
		return True
	return False

def fix(bank, account):
	count = 0
	zip_addr = 0
	for ac in bank.accounts:
		if ac.name == account:
			if hasattr(ac.__dict__.items(), 'name') == True:
				ac.__setattr__('name', 'Unknown')
				count += 1
			if hasattr(ac.__dict__.items(), 'id') == True:
				ac.__setattr__('id', 0)
				count += 1
			if hasattr(ac.__dict__.items(), 'value') == True:
				ac.__setattr__('value', 0)
				count += 1
			for key, value in ac.__dict__.items():
				count += 1
				if key.startswith('zip') or key.startswith('addr'):
					zip_addr += 1
				if key.startswith('b'):
					ac.__delattr__(key)
				if key == 'name' and type(value) != str:
					ac.__setattr__('name', 'Unknown')
				if key == 'id' and type(value) != int:
					ac.__setattr__('id', 0)
				if key == 'value' and type(value) != int and type(value) != float:
					ac.__setattr__('value', 0)
			if zip_addr == 0:
				ac.__setattr__('zip', 0)
				count+=1
			if count%2 == 0:
				ac.__setattr__('X', 'x')


class Bank():
	def __init__(self):
		self.accounts = []
	def __str__(self):
		print("Bank accounts:")
		for ac in self.accounts:
			if hasattr(ac, 'name'):
				print(f" -{ac.name}")
			else:
				print(f" -None")
		return ""
	def add(self, new_account):
		if isinstance(new_account, Account) == False:
			return print("Not the right object")
		self.accounts.append(new_account)
		print(f"account {new_account.name} added")
	def transfer(self, origin, dest, amount):
		o = 0
		d = 0
		if amount < 0:
			return False
		for account in self.accounts:
			if account.name == origin:
				o = account
			if account.name == dest:
				d = account
			if account.name == origin and check_corrupted(account) == True:
				return False
			if account.name == dest and check_corrupted(account) == True:
				return False
		if o == 0 or d == 0:
			return False
		if o.value < amount:
			return False
		o.value -= amount
		d.value += amount
		print(f"{amount} transferred from {o.name} to {d.name}")
		return True
	def fix_account(self, name):
		if type(name) != str:
			return False
		for account in self.accounts:
			if name == account:
				return False
		fix(self, name)
		return True