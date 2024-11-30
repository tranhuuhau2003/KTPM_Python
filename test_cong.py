import unittest

# Hàm cần kiểm tra
def cong(a, b):
    return a + b

# Test case
class TestCong(unittest.TestCase):
    def test_cong(self):
        self.assertEqual(cong(1, 2), 3)
        self.assertEqual(cong(-1, 1), 0)
        self.assertEqual(cong(0, 0), 0)

if __name__ == '__main__':
    unittest.main()
