# -*- coding: utf-8 -*-
'''
name: Rogfel Thompson Martinez
date: 04/07/2018
'''

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
            # for index in self.__list_structures:
            #     self.__do_combination(
            # len(index['index']), 0, index['index'], self.__array_cardi, 0)
            for x in xrange(0, n):
                self.__do_combination(
                    len(
                        self.__list_structures[0]['index']),
                    x,
                    self.__list_structures[0]['index'],
                    self.__array_cardi,
                    0)
            print(self.__list_structures[0])
            print(self.__list_partitions)
            # if includeTrivial:
            # 	self.__list_partitions.append()
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
        str_row = prefix + self.__list_partitions[0] + suffix
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

    def __do_combination(self, level, start_x, index, index_values, index_id):

        if level > 1:
            for x in xrange(start_x, len(index)):
                for y in xrange(0, len(index[x])):
                    index[x][y] = index_values[index_id + y]
                    self.__do_combination(
                        level - 1,
                        start_x + 1,
                        index,
                        index_values,
                        index_id + y + 1)
        else:
            for x in xrange(start_x, len(index)):
                for y in xrange(0, len(index[x])):
                    index[x][y] = index_values[index_id + y]
                    print(index[x][y])
            temp_array = index_values[:]
            for x in xrange(0, len(index)):
                for y in xrange(0, len(index[x])):
                    temp_array.remove(index[x][y])
            self.__list_partitions.append((index, temp_array))

    def __partition_structures(self, start_x, start_y, cardinality):
        x = start_x
        flag = True
        y = start_y
        while x < cardinality and flag:
            index = [[-1] * y] * x
            total, max_len = self.__index_length(index)
            other = [-1] * (cardinality - total)
            if len(other) >= max_len:
                self.__list_structures.append(
                    {'index': index, 'other': other})
                self.__partition_structures(start_x + 1, y, cardinality)
            else:
                flag = False
            y += 1


if __name__ == "__main__":

    print("Prints:")

    part = PartitionGenerator(4)

    # while not part.depleted():
    #     part.printForDebug("", "\n")
    #     part.next()

    # print("Prints:")

    # part = CombinationGenerator(4)

    # while not part.depleted():
    #     part.printForDebug("", "\n")
    #     part.next()

    # print("Prints:")
