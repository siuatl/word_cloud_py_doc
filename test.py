import unittest
from pdwc import normalize_size


class checking(unittest.TestCase):
    def test_funcion(self):
        normalized = normalize_size(count=83, upper=83, lower=1)
        self.assertEqual(normalized, 100)

    def test_out_of_range(self):
        my_exception = False
        try:
            normalize_size(count=90, upper=83, lower=1)
        except Exception as error:
            my_exception = True
        self.assertTrue(my_exception)


if __name__ == '__main__':
    unittest.main()
