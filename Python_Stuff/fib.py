# This calculates the Fibanacci Sequence
# Maybe some graphics will be added later

import numpy as np

class Fibber():
	# Fibber vars
	seq = []
	
	def __init__(self, lim):
		self.limit = lim
		return
	
	def get_limit(self):
		return self.limit
	
	def set_limit(self, lim):
		self.limit = lim
		return

	def how(self):
		print("How the fibanacci sequence is calculated:")
		print("\t a2 + a1 = a0")
		print("\t where \'a2\' is the number from two steps ago, \'a1\' is the previous number, and \'a0\' is the current number in the sequence.")
		return

	def create_sequence(self):
		Fibber.seq.clear()
		a2 = 0
		a1 = 1
		Fibber.seq.append(a2)
		Fibber.seq.append(a1)
		a0 = -1
		while a0 < self.limit:
			a0 = a1 + a2
			print("{} + {} = {}".format(a2, a1, a0))
			a2 = a1
			a1 = a0
			Fibber.seq.append(a0)
		return

	def uno_card(self, sym1, sym2=sym1):
		if len(Fibber.seq) < 1:
			print("Please run \'create_sequence()\' first.")
		else:
			print("\n")
			lenny = len(Fibber.seq)
			max_lenny = Fibber.seq[-1]
			for f in range lenny:
				part1 = ''
				part2 = ''
				for i in range(Fibber.seq[f]):
					part1 += sym1
				for j in range(Fibber.seq[l-f-1]):
					part2 += sym2
			print("{:{<}}".format(part1, max_lenny), end='', "{:{>}}".format(part2, max_lenny))
		return

	def twist(self, sym1):
		if len(Fibber.seq) < 1:
			print("Please run \'create_sequence()\' first")
		else:
			lenny = len(Fibber.seq)
			print("\n")
			for f in range(-l, l):
				line = ''
				for i in range(f):
					line += sym1
				print(line)
		return

# end of Fibber class

