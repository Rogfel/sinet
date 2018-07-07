# -*- coding: utf-8 -*-
'''
name: Rogfel Thompson Martinez
date: 04/07/2018
'''
import copy

from IPartitionGenerator import IPartitionGenerator


class PartitionGenerator(IPartitionGenerator):

    def __init__(self, n, includeTrivial=False):
        if n > 0:
            IPartitionGenerator.__init__(self, n, includeTrivial)
            self.__list_partitions = []
            self.__list_structures = []
            self.__array_cardi = []
            for i in xrange(0, n):
                self.__array_cardi.append(i)
            self.__partition_structures(1, 1, n)
            for index in self.__list_structures[1:2]:
                index_len, _ = self.__index_length(
                    index[0])
                self.__list_comb = []
                self.__do_combination(index_len, 0, n, [])
                self.__do_struct_combination(
                    index[0], self.__list_comb, self.__array_cardi)
            if includeTrivial:
                self.__list_partitions.append([self.__array_cardi])
                self.__list_partitions.insert(0, [None])
        else:
            print('O valor de n tem que ser maior que 0')

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
        total = 0
        max_len = 0
        for i in xrange(0, len(index)):
            total += len(index[i])
            if max_len < len(index[i]):
                max_len = len(index[i])
        return total, max_len

    def __do_partitions(self, cardinality):
        values_cardi = []
        if cardinality > 1:
            for i in xrange(0, cardinality):
                values_cardi.append(str(i))

    def __do_struct_combination(self, structure, list_comb, array_cardi):
        for comb in list_comb:
            index_id = 0
            temp_array = array_cardi[:]
            for x in xrange(0, len(structure)):
                for y in xrange(0, len(structure[x])):
                    structure[x][y] = copy.deepcopy(comb[index_id])
                    print(structure)
                    temp_array.remove(structure[x][y])
                    index_id += 1
            self.__list_partitions.append(
                (copy.deepcopy(structure), temp_array))

    def __do_combination(self, num_indi, start, cardinality, comb_indexs):
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
        x = start_x
        flag = True
        y = start_y
        while x < cardinality and flag:
            index = [[-1] * y] * x
            total, max_len = self.__index_length(index)
            other = [-1] * (cardinality - total)
            if len(other) >= max_len:
                self.__list_structures.append((index, other))
                self.__partition_structures(start_x + 1, y, cardinality)
            else:
                flag = False
            y += 1


if __name__ == "__main__":

    print("Prints:")

    part = PartitionGenerator(4)

    while not part.depleted():
        part.printForDebug("", "\n")
        part.next()

    # print("Prints:")

    # part = CombinationGenerator(4)

    # while not part.depleted():
    #     part.printForDebug("", "\n")
    #     part.next()

    # print("Prints:")
