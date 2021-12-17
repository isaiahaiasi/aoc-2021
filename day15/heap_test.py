import unittest
from heap import Heap


class TestHeap(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def test_inits_valid_heap(self):
        arr = [7, 3, 5, 4, 6, 1, 10, 9, 8, 15, 17]
        def sortfn(a, b): return 1 if a < b else -1
        Heap(arr, sortfn)
        self.assertEqual(1, arr[0])
