from random import shuffle

class Market:
	def __init__(self):
		self.x = ['E', 'E', 'E', 'E', 'C', 'C', 'R', 'R', 'V', 'V', 'S', 'S', 'F']
		shuffle(self.x)

	def print_cmd(self):
		print('+---+---+---+---+')
		print('| {} | {} | {} | {} | < 0'.format(self.x[0], self.x[1], self.x[2], self.x[3]))
		print('+---+---+---+---+')
		print('| {} | {} | {} | {} | < 1'.format(self.x[4], self.x[5], self.x[6], self.x[7]))
		print('+---+---+---+---+')
		print('| {} | {} | {} | {} | < 2'.format(self.x[8], self.x[9], self.x[10], self.x[11]))
		print('+---+---+---+---+')
		print('  ^   ^   ^   ^ ')
		print('  3   4   5   6 ')
		print('outside : {}'.format(self.x[12]))

	# 0 ~ 2 : push row from right side, 3 ~ 6 : push column from bottom side
	def operation(self, num: int):
		assert(num >= 0 and num < 7)
		if num < 3:
			ret = [self.x[num * 4 + i] for i in range(4)]
			outside = self.x[num * 4]
			for i in range(3):
				self.x[num * 4 + i] = self.x[num * 4 + i + 1]
			self.x[num * 4 + 3] = self.x[12]
			self.x[12] = outside
		else:
			ret = [self.x[num - 3 + i * 4] for i in range(3)]
			outside = self.x[num - 3]
			for i in range(2):
				self.x[num - 3 + i * 4] = self.x[num - 3 + (i + 1) * 4]
			self.x[num - 3 + 8] = self.x[12]
			self.x[12] = outside
		return ret