from typing import List, Union


Comparable = Union[int, str, float]


class PQueue:
    def __ini__(self):
        self._heap: List[Comparable] = []
        self._heapSize: int = 0
        self._heapCapacity: int = 0
        self._map: dict = {}

    def __str__(self):
        return str(self._heap)


    """
    min heap
    

    [1, 2, 3, 4, 3, 5, 5, 9, 7, 15, 2]
     0  1  2  3   4  5  6  7  8  9  10
     
                     1(0)                               *(x) 2  
                 /           \                       /             \
              2(1)             3(2)              *(x*2 + 1)     *(x*2 + 2)
         /           \        /     \                       
       4(3)         3(4)    5(5)   5(6)                   
       /  \        /    \
     9(7) 7(8)    15(9) 6(10)
     
    
    2
    """

    def add(self, elem):
        self._heap.append(elem)

    def _swim(self, k):
        parent = (k - 1) // 2

        while k > 0 and self.__less(k, parent):
            print(f'    inside: {pqueue._heap}')
            self.__swap(parent, k)
            k = parent
            parent = (k - 1) // 2
        print(f'end inside: {pqueue._heap}')

    def __sink(self, k):
        pass

    def __swap(self, i, j):
        i_elem = self._heap[i]
        j_elem = self._heap[j]
        self._heap[i] = j_elem
        self._heap[j] = i_elem

    def __less(self, i, j):
        i_elem = self._heap[i]
        j_elem = self._heap[j]
        return i_elem < j_elem


if __name__ == '__main__':
    pqueue = PQueue()

    pqueue._heap = [1, 3, 3, 4, 6, 5, 5, 9, 7, 15, 2]

    k = len(pqueue._heap) - 1

    print(k)
    parent = (k - 1) // 2

    pqueue._swim(k)

    print(pqueue._heap)




