# -*- coding: utf-8 -*-
'''
name: Rogfel Thompson Martinez
date: 04/07/2018
'''

from ICombinationGenerator import ICombinationGenerator

class CombinationGenerator(ICombinationGenerator):

	
	def __init__(self, n, k=-1, avoidAllZero = False, avoidAllOne = False):
		ICombinationGenerator.__init__(self, n, k)
	
		self.__matrix = []
		row = [0] * n
		if avoidAllZero:
			self.__matrix.append(row)

		if k > 0:			
			self.__do_matrix(k, 0, n, row)
		else:	
			for i in xrange(1, n):
				self.__do_matrix(i, 0, n, row)

		if avoidAllOne:
			self.__matrix.append([1] * n)

	def at(self, pos):
		"""
		attribute:
			pos: position in row
		return:
			value in this position
		"""
		return self.__matrix[0][pos]

	def depleted(self):
		"""
		return:
			False: when the matrix isn't empty
			True: when the matrix is empty
		"""
		if len(self.__matrix) > 0:			
			return False
		else:
			return True
		

	def next(self):
		"""
		Delete the first row in the matrix
		"""
		self.__matrix.pop(0) 
		

	def printForDebug(self, prefix = "", suffix="\n"):
		"""
		Print one row item
		attribute:
			prefix: the first item to print in row
			suffix: the last item to print in row			
		"""
		row = self.__matrix[0]
		str_row = prefix+"( "
		for item in row:
			str_row += str(item)+" "
		str_row+= ")"+suffix	
		print(str_row)

	def __do_matrix(self, level, start_column, end_column, row):


		if level > 1:
			for i in xrange(start_column, end_column-level+1):
				temp_row = row[:]
				temp_row[i] = 1
				start_column = i
				self.__do_matrix(level-1, start_column+1, end_column, temp_row)
		else:
			for i in xrange(start_column, end_column):
				temp_row = row[:]
				temp_row[i] = 1
				self.__matrix.append(temp_row)


if __name__ == "__main__":

	print("Prints:")

	comb = CombinationGenerator(3)

	while not comb.depleted():
		comb.printForDebug("", "\n")
		comb.next();

	print("Prints:")

	comb = CombinationGenerator(5,3)	

	while not comb.depleted():
		comb.printForDebug("", "\n")
		comb.next();	

	print("Prints:")

	comb = CombinationGenerator(5,3)
	comb.printForDebug("", "")
	print("TRUE" if comb.at(0)  else "FALSE")
	print("TRUE" if comb.at(3)  else "FALSE")
