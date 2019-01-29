import unittest
from app.src.app import my_function

class MyTest2(unittest.TestCase):
    def test_my_function(self):
         self.assertEqual(my_function(1, 2), 3)
         self.assertEqual(my_function(1, 1), 4)
        
        
        
if __name__ == '__main__':
    unittest.main()  