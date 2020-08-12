import unittest

from binary_search import binary_search

class TestBinarySearch(unittest.TestCase):
    def test_right_index(self):
        """
        Test that checks if Binary Search finds the proper index
        """
        data = [1, 2, 3, 4, 5]
        result = binary_search(data, 2)
        self.assertEqual(result, 1)

    def test_non_found_index(self):
        """
        Test that checks if Binary Search returns -1 when the value is not found
        """
        data = [1, 2, 3, 4, 5]
        result = binary_search(data, 100)
        self.assertEqual(result, -1)

if __name__ == '__main__':
    unittest.main()