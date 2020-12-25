from math import log2
from random import randrange

class Heap:
    def __init__(self, a, HeapType=None):
        self.heap = a
        self.type = HeapType

    def heapify(self, index):
        ltson = 2 * index + 1
        rtson = 2 * index + 2
        father = index

        if self.type == 'maxheap':
            if ltson < len(self.heap) and self.heap[ltson] > self.heap[father]:
                    father = ltson

            if rtson < len(self.heap) and self.heap[rtson] > self.heap[father]:
                    father = rtson

        else:
            if ltson < len(self.heap) and self.heap[ltson] < self.heap[father]:
                father = ltson

            if rtson < len(self.heap) and self.heap[rtson] < self.heap[father]:
                father = rtson

        if father != index:
            self.heap[index], self.heap[father] = self.heap[father], self.heap[index]
            self.heapify(father)

    @staticmethod
    def parent(i):
        return (i-1)//2

    @staticmethod
    def left_child(i):
        return 2 * i + 1

    @staticmethod
    def right_child(i):
        return 2 * i + 2

    def delete(self, index):
        if index == 0:
            self.heap.insert(0, self.heap.pop(-1))
            del self.heap[1]
        else:
            del self.heap[index]
        self.heapify(0)

    def heappush(self, value):
        if type(value) == list or type(value) == tuple:
            self.heap += value
        else:
            self.heap.append(value)
        index = len(self.heap) - 1
        while index > 0:
            parent_index = self.parent(index)

            if self.heap[index] > self.heap[parent_index] and self.type == 'maxheap':
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                index = parent_index

            elif self.heap[index] < self.heap[parent_index] and self.type == 'minheap':
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                index = parent_index

            else:
                index = -1

    def heappop(self):
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        value = self.heap.pop()
        self.heapify(0)
        return value

    def print(self, big=None):
        if len(self.heap) > 0:
            lines = int(log2(len(self.heap))) + 1
            t = len(str(max(self.heap)))

            for i in range(lines):
                index_to_print = [2**i - 1 + _ for _ in range(2**i) if 2**i - 1 + _ < len(self.heap)]

                sp = ' ' * t * (2**(lines - i) - 1)
                header = ' ' * t * 2**(lines - i - 1)

                print(f"\"{i}\":", end='')
                print(header, end='')

                if big in index_to_print:
                    to_print = ""

                    for j in index_to_print:
                        if big == j:
                            to_print += "\"{0:^{1}}\"".format(self.heap[j], t)
                        else:
                            to_print += "{0:^{1}}".format(self.heap[j], t)

                        to_print += sp

                    print(to_print)

                else:
                    print(sp.join(["{0:^{1}}".format(self.heap[j], t) for j in index_to_print]))
            
                print('\n')

class MaxHeap(Heap):
    def __init__(self, a):
        super().__init__(a, 'maxheap')
        for i in range(len(self.heap)//2 - 1, -1, -1):
            self.heapify(i)

    def isInHeap(self, el, heap=self.heap):
        if el > heap[0]:
            return False
        else:
            return el in heap

class MinHeap(Heap):
    def __init__(self, a):
        super().__init__(a, 'minheap')
        for i in range(len(self.heap)//2 - 1, -1, -1):
            self.heapify(i)

    def isInHeap(self, el, heap=self.heap):
        if el < heap[0]:
            return False
        else:
            return el in heap

data = [randrange(0, 200) for _ in range(30)]
heap = MaxHeap(data.copy())