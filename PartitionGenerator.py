# -*- coding: utf-8 -*-
'''
name: Rogfel Thompson Martinez
date: 04/07/2018
'''
import copy

from IPartitionGenerator import IPartitionGenerator


class PartitionGenerator(IPartitionGenerator):

    def __init__(self, n, includeTrivial=False):
        self.__list_partitions = []
        if n > 2:
            n = int(n)
            IPartitionGenerator.__init__(self, n, includeTrivial)
            self.__list_structures = []
            self.__array_cardi = []
            for i in xrange(0, n):
                self.__array_cardi.append(i)
            self.__partition_structures(1, 1, n)
            for index in self.__list_structures:
                index_len, _ = self.__index_length(
                    index[0])
                self.__list_comb = []
                self.__do_combination(index_len, 0, n, [])
                self.__list_part = []
                self.__do_struct_combination(
                    index[0], self.__list_comb, self.__array_cardi)
                self.__list_partitions += self.__list_part
            if includeTrivial:
                self.__list_partitions.append([self.__array_cardi])
                self.__list_partitions.insert(0, [None])
        else:
            print('O valor de n tem que ser maior ou mesmo que 2')

    def depleted(self):
        """
        return:
                        False: when the matrix isn't empty
                        True: when the matrix is empty
        """
        if len(self.__list_partitions) > 0:
            return False
        else:
            return True

    def next(self):
        """
        Delete the first row in the matrix
        """
        self.__list_partitions.pop(0)

    def printForDebug(self, prefix="", suffix="\n"):
        """
        Print one row item
        attribute:
                        prefix: the first item to print in row
                        suffix: the last item to print in row
        """
        prefix = str(prefix)
        suffix = str(suffix)
        str_chain = ''
        for chain in self.__list_partitions[0]:
            if chain is None:
                str_chain += '{}'
            else:
                str_chain += str(chain)
        str_chain = str_chain.replace('[[', ' { ')
        str_chain = str_chain.replace(']]', ' } ')
        str_chain = str_chain.replace('[', ' { ')
        str_chain = str_chain.replace(']', ' } ')
        str_row = prefix + str_chain + suffix
        print(str_row)

    def __index_length(self, index):
        """
                index are the positions before the last
                index_length is the number of elements that the index has
        """
        total = 0
        max_len = 0
        for i in xrange(0, len(index)):
            total += len(index[i])
            if max_len < len(index[i]):
                max_len = len(index[i])
        return total, max_len

    def __reduction(self):
        """
        reduction of repeated combinations
        """
        flag = False
        for row in self.__list_part:
            for i, rowb in enumerate(self.__list_part):
                if row[0][0] == rowb[1]:
                    del self.__list_part[i]

        for i, rowb in enumerate(self.__list_part):
            if len(rowb[1]) == 1 and flag:
                del self.__list_part[i]
            if len(rowb[1]) == 1:
                flag = True

    def __do_struct_combination(self, structure, list_comb, array_cardi):
        """
                Put the combination list in the especific structure
                attribute
                        structure: define structure. Example {}{}{ , }
                        list_comb: combination list for this structure
                        array_cardi: number list of input cardinality
        """
        for comb in list_comb:
            index_id = 0
            temp_array = array_cardi[:]
            temp_structure = structure[:]
            for x in xrange(0, len(structure)):
            	temp_structure[x] = structure[x][:]
                for y in xrange(0, len(structure[x])):
                    temp_structure[x][y] = comb[index_id]
                    temp_array.remove(temp_structure[x][y])
                    index_id += 1
            self.__list_part.append(
                (copy.deepcopy(temp_structure), temp_array))
            self.__reduction()

    def __do_combination(self, num_indi, start, cardinality, comb_indexs):
        """
                It make combinations for especific index length
                This method is recursive
                Attribute:
                         num_indi: the index level. Exemplo {1} {,} level 1; {2}{1}{,} level 2
                         start: start position  of cardinality list
                         cardinality: cardinality value
                         comb_indexs: combination values in construction
        """
        if num_indi > 1:
            for val in xrange(start, cardinality - 1):
                combination_indexs = comb_indexs[:]
                combination_indexs.append(val)
                self.__do_combination(
                    num_indi - 1,
                    val + 1,
                    cardinality,
                    combination_indexs)
        else:
            for val in xrange(start, cardinality):
                combination_indexs = comb_indexs[:]
                combination_indexs.append(val)
                self.__list_comb.append(copy.deepcopy(combination_indexs))

    def __partition_structures(self, start_x, start_y, cardinality):
        """
                It make particions structure
                This method is recursive
                Attribute
                        start_x: start values of amount of the index column
                        start_y: start values of amount of the index column index deep column
                        cardinality: cardinality value
        """
        x = start_x
        flag = True
        y = start_y
        while x < cardinality and flag:
            index = [[-1] * y] * x
            total, max_len = self.__index_length(index)
            other = [-1] * (cardinality - total)
            if len(other) >= max_len:
                if not ((index, other) in self.__list_structures):
                    self.__list_structures.append((index, other))
                    self.__partition_structures(start_x + 1, y, cardinality)
            else:
                flag = False
            y += 1


if __name__ == "__main__":

    print("Prints: n = 1")

    part = PartitionGenerator(1)

    while not part.depleted():
        part.printForDebug("", "\n")
        part.next()

    print("Prints: n = 2.5")

    part = PartitionGenerator(2.5)
    # para valores decimais se converte o número a entero
    while not part.depleted():
        part.printForDebug("", "\n")
        part.next()

    print("Prints: n = 4")

    part = PartitionGenerator(4)

    while not part.depleted():
        part.printForDebug("", "\n")
        part.next()
