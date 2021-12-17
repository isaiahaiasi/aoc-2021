from typing import TypeVar, Callable

T = TypeVar("T")

# sortfn = (a, b) => -1, 0, or 1


class Heap:
    def __init__(self, values: list[T], sortfn: Callable[[T, T], int]):
        self.arr = values
        self.sortfn = sortfn
        self._heapify()

    def push(self, n: T):
        self.arr.append(n)
        self.percolate(self._getlastbranching())
        pass

    def pop(self) -> T:
        popnode, self.arr[0] = self.arr[0], self.arr[-1]
        self.arr.pop()
        self.arr[0].heappos = 0
        self.percolate(0)
        return popnode

    def updatepos(self, i: int):
        parent = self._getparent(i)
        self.percolate(parent)

    def percolate(self, i: int):
        greatest = i
        left = self._getleft(i)
        right = self._getright(i)

        if left < len(self.arr):
            if self.sortfn(self.arr[left], self.arr[greatest]) > 0:
                greatest = left

        if right < len(self.arr):
            if self.sortfn(self.arr[right], self.arr[greatest]) > 0:
                greatest = right

        # if left or right are greater than root, swap & recurse
        if greatest != i:
            node_a = self.arr[i]
            node_b = self.arr[greatest]
            print(
                f"moving {node_b.coords}({node_b.tc}) above {node_a.coords}({node_a.tc})")
            self.arr[i].heappos = greatest
            self.arr[greatest].heappos = i
            self.arr[i], self.arr[greatest] = self.arr[greatest], self.arr[i]
            self.percolate(greatest)

    def _heapify(self):
        # build heap from unsorted list by percolating every non-leaf node
        for i in range(self._getlastbranching(), -1, -1):
            self.percolate(i)
        for i in range(len(self.arr)):
            self.arr[i].heappos = i
        print("done heapifying")

    def _getleft(self, i: int) -> int:
        return (2 * i) + 1

    def _getright(self, i: int) -> int:
        return (2 * i) + 2

    def _getparent(self, i: int) -> int:
        return (i - 1)//2

    def _getlastbranching(self) -> int:
        return (len(self.arr)//2) - 1

    def rendertree(self, attr="coords"):
        depth = 0
        i = 0
        out = str(getattr(self.arr[0], attr)) + '\n'
        children = [self._getleft(i), self._getright(i)]
        while (len(children) > 0):
            grandchildren = []
            for child in children:
                # render
                out += str(getattr(self.arr[child], attr)) + ','
                # add children to grandchildren
                left = self._getleft(child)
                right = self._getright(child)
                validchildren = [i for i in [left, right] if i < len(self.arr)]
                for c in validchildren:
                    grandchildren.append(c)
            children = grandchildren
            out += '\n'
        return out
